# Builds the dissertation: doc/chapters/*.md -> build/thesis.docx
# Usage (from anywhere): powershell -File doc/build.ps1
$ErrorActionPreference = 'Stop'
$doc = $PSScriptRoot
$out = Join-Path (Split-Path $doc) 'build'
New-Item -ItemType Directory -Force $out | Out-Null

$chapters = @(Get-ChildItem (Join-Path $doc 'chapters') -Filter *.md | Sort-Object Name | ForEach-Object FullName)
$pandocArgs = @(
    '--from', 'markdown',
    '--citeproc',
    '--bibliography', (Join-Path $doc 'references.bib'),
    '--csl', (Join-Path $doc 'ieee.csl'),
    '--metadata', 'lang=en-GB',
    '--metadata', 'link-citations=true',
    '--output', (Join-Path $out 'thesis.docx')
)
$ref = Join-Path $doc 'reference.docx'
if (Test-Path $ref) { $pandocArgs += @('--reference-doc', $ref) }
else { Write-Warning 'doc/reference.docx not found; using the Pandoc default styles.' }

& pandoc @pandocArgs @chapters
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Built $(Join-Path $out 'thesis.docx')"
