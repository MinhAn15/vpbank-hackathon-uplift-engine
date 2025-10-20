# Requires: Node.js and @mermaid-js/mermaid-cli (`npm i -g @mermaid-js/mermaid-cli`)
param(
    [string]$InFile = "architecture.mmd",
    [string]$OutFile = "architecture.png",
    [int]$Width = 1600,
    [switch]$Transparent
)

$transparentArg = $null
if ($Transparent) { $transparentArg = "-b transparent" }

$cmd = "mmdc -i $InFile -o $OutFile -w $Width $transparentArg"
Write-Host "Rendering Mermaid diagram: $cmd"
& cmd /c $cmd

if ($LASTEXITCODE -ne 0) {
    Write-Error "Rendering failed. Ensure 'mmdc' is installed: npm i -g @mermaid-js/mermaid-cli"
    exit 1
}

Write-Host "Done → $OutFile"
