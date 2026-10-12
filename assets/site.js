// The Ruler of Nothing: night mode, text size on chapters, the chapter list and
// "Recently added", comments, the mobile menu, the reading progress bar, and
// chapter search on the table of contents.
// A reader's choices are kept in their own browser (localStorage).
(function () {
  var root = document.documentElement;

  // Comments under each chapter, with replies (giscus, stored in the
  // repository's GitHub Discussions). To switch them on, paste the two IDs
  // from giscus.app below. README.md has the steps.
  var COMMENTS = {
    repo: 'marclourens19/therulerofnothing',
    repoId: '',
    category: 'Comments',
    categoryId: ''
  };

  // giscus loads its theme from its own server, so it needs the full address.
  // Before the site is online it falls back to giscus's plain light and dark.
  function commentTheme(night) {
    if (location.protocol !== 'https:') return night ? 'dark' : 'light';
    return new URL('assets/giscus-' + (night ? 'dark' : 'light') + '.css', location.href).href;
  }

  function setNight(on) {
    root.classList.toggle('night', on);
    try { localStorage.setItem('ron-theme', on ? 'night' : 'day'); } catch (e) { /* storage blocked */ }
    document.querySelectorAll('.theme').forEach(function (b) {
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    var frame = document.querySelector('iframe.giscus-frame');
    if (frame) frame.contentWindow.postMessage({ giscus: { setConfig: { theme: commentTheme(on) } } }, 'https://giscus.app');
  }

  // One chapter as a list item: its title as a link, then its release date
  function chapterItem(ch) {
    var li = document.createElement('li');
    var link = document.createElement('a');
    link.href = ch.file;
    link.textContent = ch.title;
    var date = document.createElement('span');
    date.className = 'date';
    date.textContent = ch.date;
    li.appendChild(link);
    li.appendChild(date);
    return li;
  }

  // Text size steps for chapter text (1 is the normal size)
  var STEPS = [0.85, 0.92, 1, 1.1, 1.2, 1.32, 1.45];

  document.addEventListener('DOMContentLoaded', function () {
    // Night mode button (the choice is remembered on this device)
    var night = root.classList.contains('night');
    document.querySelectorAll('.theme').forEach(function (b) {
      b.setAttribute('aria-pressed', night ? 'true' : 'false');
      b.addEventListener('click', function () { setNight(!root.classList.contains('night')); });
    });

    // Text size buttons on chapter pages (also remembered on this device)
    var down = document.querySelector('.size-down');
    var up = document.querySelector('.size-up');
    if (down && up) {
      var saved = parseFloat(root.style.getPropertyValue('--text-scale')) || 1;
      var step = 0;
      STEPS.forEach(function (v, k) { if (Math.abs(v - saved) < Math.abs(STEPS[step] - saved)) step = k; });
      var showLimits = function () {
        down.setAttribute('aria-disabled', step === 0 ? 'true' : 'false');
        up.setAttribute('aria-disabled', step === STEPS.length - 1 ? 'true' : 'false');
      };
      var setSize = function (next) {
        if (next < 0 || next >= STEPS.length) return;
        // Keep the paragraph being read in the same place on screen
        var anchor = null;
        var paras = document.querySelectorAll('.prose p');
        for (var k = 0; k < paras.length; k++) {
          if (paras[k].getBoundingClientRect().bottom > 0) { anchor = paras[k]; break; }
        }
        var before = anchor ? anchor.getBoundingClientRect().top : 0;
        step = next;
        root.style.setProperty('--text-scale', STEPS[step]);
        try { localStorage.setItem('ron-size', String(STEPS[step])); } catch (e) { /* storage blocked */ }
        if (anchor) window.scrollBy(0, anchor.getBoundingClientRect().top - before);
        showLimits();
      };
      down.addEventListener('click', function () { setSize(step - 1); });
      up.addEventListener('click', function () { setSize(step + 1); });
      showLimits();
    }

    // Table of contents and "Recently added", both from assets/chapters.js
    var chapters = window.RON_CHAPTERS || [];
    document.querySelectorAll('.toc[data-volume]').forEach(function (list) {
      var volume = parseInt(list.getAttribute('data-volume'), 10);
      chapters.forEach(function (ch) { if (ch.volume === volume) list.appendChild(chapterItem(ch)); });
      var next = window.RON_NEXT;
      if (next && next.volume === volume) {
        var li = document.createElement('li');
        var name = document.createElement('span');
        name.className = 'upcoming-name';
        name.textContent = next.title;
        var chip = document.createElement('span');
        chip.className = 'chip';
        chip.textContent = 'coming soon';
        li.appendChild(name);
        li.appendChild(chip);
        list.appendChild(li);
      }
    });
    var recent = document.querySelector('.recent');
    if (recent && chapters.length) {
      chapters.slice(-3).reverse().forEach(function (ch) { recent.appendChild(chapterItem(ch)); });
      recent.closest('.recent-part').hidden = false;
    }

    // Comments, once the giscus IDs are filled in above
    var thread = document.querySelector('.giscus');
    if (thread && COMMENTS.repoId && COMMENTS.categoryId) {
      var script = document.createElement('script');
      script.src = 'https://giscus.app/client.js';
      var settings = {
        'data-repo': COMMENTS.repo,
        'data-repo-id': COMMENTS.repoId,
        'data-category': COMMENTS.category,
        'data-category-id': COMMENTS.categoryId,
        // One discussion per chapter, named after the file (chapter-1, chapter-2...)
        'data-mapping': 'specific',
        'data-term': location.pathname.split('/').pop().replace(/\.html$/, '') || 'index',
        'data-strict': '1',
        'data-reactions-enabled': '1',
        'data-emit-metadata': '0',
        'data-input-position': 'bottom',
        'data-theme': commentTheme(root.classList.contains('night')),
        'data-lang': 'en',
        'data-loading': 'lazy'
      };
      Object.keys(settings).forEach(function (k) { script.setAttribute(k, settings[k]); });
      script.crossOrigin = 'anonymous';
      script.async = true;
      thread.appendChild(script);
      var soon = document.querySelector('.comments .note');
      if (soon) soon.hidden = true;
    }

    // Menu button on phones
    var toggle = document.querySelector('.menu-toggle');
    if (toggle) {
      toggle.addEventListener('click', function () {
        var open = toggle.closest('.nav').classList.toggle('open');
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    }

    // Reading progress bar on chapter pages
    var bar = document.querySelector('.progress');
    if (bar) {
      var update = function () {
        var max = root.scrollHeight - window.innerHeight;
        var done = max > 0 ? Math.min(1, window.scrollY / max) : 0;
        bar.style.transform = 'scaleX(' + done + ')';
      };
      window.addEventListener('scroll', function () { window.requestAnimationFrame(update); }, { passive: true });
      update();
    }

    // Search: the sidebar form sends ?q= to the table of contents, which filters its list
    var query = new URLSearchParams(window.location.search).get('q');
    var list = document.querySelector('.toc');
    if (query && list) {
      var q = query.trim().toLowerCase();
      var shown = 0;
      list.querySelectorAll('li').forEach(function (li) {
        var match = li.textContent.toLowerCase().indexOf(q) !== -1;
        li.hidden = !match;
        if (match) shown++;
      });
      var none = document.querySelector('.no-match');
      if (none) none.hidden = shown > 0;
      var input = document.querySelector('.search input');
      if (input) input.value = query;
    }
  });
})();
