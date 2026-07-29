# ship.ps1 — one-command band ship for Star-Magic-Program
# Usage: .\ship.ps1
# Reads version from pyproject.toml, commit message from SHIP_MESSAGE.txt.
# Encodes every hard-won lesson from 2026-07-28 (see CLAUDE.md).

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "=== ship.ps1 — Star-Magic-Program band ship ===" -ForegroundColor Cyan

# --- 0. Clear stale git lock/temp files (Windows lock lesson) ---
Remove-Item .git\index.lock     -Force -ErrorAction SilentlyContinue
Remove-Item .git\COMMIT_EDITMSG -Force -ErrorAction SilentlyContinue

# --- 1. Read version from pyproject.toml ---
$verLine = Select-String -Path pyproject.toml -Pattern '^version\s*=\s*"([^"]+)"'
if (-not $verLine) { Write-Error "Cannot read version from pyproject.toml"; exit 1 }
$version = $verLine.Matches[0].Groups[1].Value
$tag = "v$version"
Write-Host "Version: $version  (tag: $tag)"

# --- 2. Read commit message from SHIP_MESSAGE.txt ---
if (-not (Test-Path SHIP_MESSAGE.txt)) {
    Write-Error "SHIP_MESSAGE.txt not found. Claude must write it before shipping."; exit 1
}
$msg = Get-Content SHIP_MESSAGE.txt -Raw
if ($msg.Trim().Length -lt 10) { Write-Error "SHIP_MESSAGE.txt is empty/too short."; exit 1 }

# --- 3. Fidelity gate (never ship red) ---
Write-Host "=== Fidelity gate ===" -ForegroundColor Cyan
python uqff_fidelity_tests.py
if ($LASTEXITCODE -ne 0) { Write-Error "FIDELITY GATE RED — ship aborted."; exit 1 }

# --- 4. Refuse to ship if tag already exists (local or remote) ---
$existing = git tag -l $tag
if ($existing) { Write-Error "Tag $tag already exists locally. Bump version first."; exit 1 }

# --- 5. Stage + commit ---
Write-Host "=== Staging ===" -ForegroundColor Cyan
git add -A
$staged = (git status --short | Measure-Object -Line).Lines
Write-Host "Files staged: $staged"
if ($staged -eq 0) { Write-Error "Nothing to commit."; exit 1 }

Write-Host "=== Committing ===" -ForegroundColor Cyan
$before = git rev-parse HEAD
git commit -m $msg
if ($LASTEXITCODE -ne 0) { Write-Error "git commit FAILED — ship aborted."; exit 1 }

# --- 6. Verify HEAD advanced (silent-failure lesson) ---
$after = git rev-parse HEAD
if ($before -eq $after) { Write-Error "HEAD did not advance — commit silently failed."; exit 1 }
git log --oneline -1

# --- 7. Tag the NEW commit and verify tag == HEAD (tag-placement lesson) ---
git tag -a $tag -m $msg.Split("`n")[0]
$tagCommit = git rev-parse "$tag^{commit}"
if ($tagCommit -ne $after) { Write-Error "Tag $tag does not point at HEAD — aborting before push."; exit 1 }
Write-Host "Tag $tag -> $($tagCommit.Substring(0,7))  (== HEAD)" -ForegroundColor Green

# --- 8. Push branch + tag ---
Write-Host "=== Pushing ===" -ForegroundColor Cyan
git push origin master
if ($LASTEXITCODE -ne 0) { Write-Error "Push master failed."; exit 1 }
git push origin $tag
if ($LASTEXITCODE -ne 0) { Write-Error "Push tag failed."; exit 1 }

Write-Host ""
Write-Host "=== SHIPPED $tag ===" -ForegroundColor Green
Write-Host "Watch: https://github.com/Daniel8Murphy0007/Star-Magic-Program/actions"
Write-Host "PyPI:  https://pypi.org/project/star-magic-program/$version/"
