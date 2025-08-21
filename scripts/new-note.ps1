param([string]$Title = "")
$today = (Get-Date -Format "yyyy-MM-dd")
$slug = if ($Title) { ($Title -replace '\s+','-') } else { "note" }
$path = "notes/note-$today.md"
if (-not (Test-Path "notes")) { New-Item -ItemType Directory notes | Out-Null }
if (-not (Test-Path $path)) {
@"
# 学習ノート $today

## 今日学んだこと
- 

## 疑問点・調べたいこと
- 

## 実験したコード / メモ
```bash
