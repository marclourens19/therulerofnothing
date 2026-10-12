// Deletes reader comments that contain a link or a blocked word.
// Called by .github/workflows/moderate-comments.yml for every new or edited comment.
// The blocked words are kept in the repository secret BLOCKED_WORDS, so nobody
// can read them here and find a way around them.

// Only comments in this Discussions category are checked (the one giscus uses)
const CATEGORY = 'Comments';

// Links in any form: web addresses, "www.", bare domains (also written as "site dot com"),
// Markdown links and images, and HTML
const TLDS = '(com|net|org|io|co|gg|ly|me|xyz|info|ru|tk|app|dev|link|site|online|shop|top|biz|us|uk|ca|au|de|in|cc|tv|to|be|ai|so|ws|club|live|store|pro|vip|win|bet|fun|icu|cn|su|ga|ml|cf|gq)';
const LINK_PATTERNS = [
  /https?:\/\//i,
  /\bwww\./i,
  /\]\(/,
  /<\s*a\s/i,
  /<\s*img\s/i,
  new RegExp('\\b[a-z0-9-]+\\.' + TLDS + '\\b', 'i'),
  new RegExp('\\b[a-z0-9-]+\\s*[\\(\\[]\\s*dot\\s*[\\)\\]]\\s*' + TLDS + '\\b', 'i'),
  /\b[a-z0-9-]+\s+dot\s+(com|net|org|io|gg|co|me)\b/i
];

// Turns look-alike spellings back into plain letters: "h4t3", "h.a.t.e", "h a t e"
function normalise(text) {
  let t = text.toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '');
  t = t.replace(/[0@4]/g, (c) => ({ '0': 'o', '@': 'a', '4': 'a' })[c])
       .replace(/[1!|]/g, 'i').replace(/3/g, 'e').replace(/[5$]/g, 's').replace(/7/g, 't');
  // Join letters spelled out one at a time ("s l u r" or "s.l.u.r")
  t = t.replace(/\b(?:[a-z][\s._*\-]+){2,}[a-z]\b/g, (m) => m.replace(/[\s._*\-]+/g, ''));
  return t;
}

// One word or phrase per line (commas work too); lines starting with # are ignored
function loadBlocked() {
  return (process.env.BLOCKED_WORDS || '').split('\n')
    .filter((line) => !line.trim().startsWith('#'))
    .join(',').split(',')
    .map((word) => word.trim().toLowerCase())
    .filter(Boolean);
}

function escape(word) {
  return word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s+');
}

// Returns why a comment breaks the rules, or null if it is fine
function check(body, blocked) {
  if (LINK_PATTERNS.some((re) => re.test(body))) return 'contains a link';
  const text = normalise(body);
  for (const word of blocked) {
    if (new RegExp('\\b' + escape(word) + '(s|es|z)?\\b', 'i').test(text)) return 'contains a blocked word';
  }
  return null;
}

module.exports = async ({ github, context, core }) => {
  const { comment, discussion, repository } = context.payload;
  if (!comment || !discussion) return;
  if (discussion.category && discussion.category.name !== CATEGORY) {
    core.info('Not a chapter comment, skipped.');
    return;
  }
  if (comment.user && comment.user.login === repository.owner.login) {
    core.info('Comment by the author, skipped.');
    return;
  }
  const blocked = loadBlocked();
  if (!blocked.length) core.warning('The BLOCKED_WORDS secret is empty, so only links are being checked.');
  const reason = check(comment.body || '', blocked);
  if (!reason) {
    core.info('Comment is fine.');
    return;
  }
  await github.graphql(
    'mutation($id: ID!) { deleteDiscussionComment(input: { id: $id }) { clientMutationId } }',
    { id: comment.node_id }
  );
  // The log is public, so it names the reason and the account but never repeats the comment
  core.notice(`Deleted a comment by @${comment.user.login} on "${discussion.title}" because it ${reason}.`);
};

module.exports.check = check;
module.exports.normalise = normalise;
module.exports.loadBlocked = loadBlocked;
