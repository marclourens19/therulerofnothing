$source = 'C:\Users\joshu\.codex\attachments\7017b388-aee7-4daa-a675-8ba9a0a91983\Pasted text.txt'
$destination = 'C:\Users\joshu\Documents\Codex\2026-09-25\files-pasted-by-the-user-the\work\Chapter 1 - Corrected User Revision.md'

$text = [System.IO.File]::ReadAllText($source)

$oldAffinityRestatement = @'
"So it isn't something I learned," he said slowly, thinking it through out loud because saying it silently hadn't gotten him anywhere all night. "Not like knowing what a spoon is for, without remembering who put one in my hand. You're telling me it's more like — my height. Or the color of my eyes. Something that's just there whether I remember it or not."

"Aye. Close enough."

"Then how could I lose it? If it isn't memory. If it's built into me the way you're saying." His voice caught somewhere in the question and he had to push through it. "How could there be nothing?"
'@

$newAffinityRestatement = @'
"So I should still know it," he said. "Even without my memories."

"Aye."

"Then how could I lose it?" His voice caught somewhere in the question, and he had to push through it. "How could there be nothing?"
'@

if (-not $text.Contains($oldAffinityRestatement)) {
    throw 'The Affinity restatement passage was not found.'
}

$text = $text.Replace($oldAffinityRestatement, $newAffinityRestatement)
$text = $text.Replace(' He reached inward the way he might reach into a dark room, feeling along a wall for a door handle he''d been told was there.', '')
$text = $text.Replace('whatever in the Last Dark those were', 'whatever those things were')

$oldBowl = 'The bowl slipped from his lap and struck the boards, spinning away across a spreading pool of stew. It splashed hot across his knees as he folded forward, both hands flying to his throat.'
$newBowl = 'The bowl slipped from his lap, struck the boards, and spun away. Hot stew splashed across his knees as he folded forward, both hands flying to his throat.'

if (-not $text.Contains($oldBowl)) {
    throw 'The bowl passage was not found.'
}

$text = $text.Replace($oldBowl, $newBowl)
$text = $text.Replace('the spilled bowl', 'the overturned bowl')

$text = $text.Replace('Someone made these. Someone will recognise them.', '*Someone made these. Someone will recognise them.*')
$text = $text.Replace("`r`nHoofbeats.`r`n", "`r`n*Hoofbeats.*`r`n")
$text = $text.Replace("`nHoofbeats.`n", "`n*Hoofbeats.*`n")
$text = $text.Replace("`r`nThey saw me.`r`n", "`r`n*They saw me.*`r`n")
$text = $text.Replace("`nThey saw me.`n", "`n*They saw me.*`n")
$text = $text.Replace('Don''t move, Gerolt mouthed. No sound came with it at all.', '*Don''t move,* Gerolt mouthed. No sound came with it at all.')
$text = $text.Replace("`r`nTock.`r`n", "`r`n*Tock.*`r`n")
$text = $text.Replace("`nTock.`n", "`n*Tock.*`n")
$text = $text.Replace('Opening that door would be the last thing he ever did.', '*Opening that door would be the last thing he ever did.*')

$output = "# Chapter 1 - A War Without Sound`r`n`r`n" + $text.TrimEnd() + "`r`n"
$encoding = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($destination, $output, $encoding)

Write-Output $destination
