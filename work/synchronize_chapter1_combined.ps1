$source = 'C:\Users\joshu\.codex\attachments\d3c13cd3-8899-4f80-9051-0c176e97d96c\Pasted text.txt'
$destination = 'C:\Users\joshu\Documents\Codex\2026-09-25\files-pasted-by-the-user-the\work\Chapter 1 - Latest Combined Draft.md'

$body = [System.IO.File]::ReadAllText($source).Trim()
$output = "# Chapter 1 - A War Without Sound`r`n`r`n" + $body + "`r`n"
$encoding = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($destination, $output, $encoding)

Write-Output $destination
