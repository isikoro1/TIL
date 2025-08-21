# now-note.ps1
Param(
  [Parameter(Mandatory = $true)]
  [string]$Title
)

$ErrorActionPreference = "Stop"

# 今日の日付（YYYY-MM-DD）
$today = Get-Date -Format "yyyy-MM-dd"

# タイトルから slug を作成（半角英数とハイフンのみ）
function To-Slug([string]$s) {
  $n = $s.ToLower()
  $n = $n -replace '\s+', '-'           # 空白→-
  $n = $n -replace '[^a-z0-9\-]', ''    # 許可以外を削除
  $n = $n -replace '-{2,}', '-'         # -- を - に
  $n = $n.Trim('-')                     # 先頭末尾の - 削除
  if ([string]::IsNullOrWhiteSpace($n)) { $n = "note" }
  return $n
}

$slug = To-Slug $Title

# ファイルパス決定（同日複数OK）
$dir = "notes"
if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
$filename = Join-Path $dir ("note-{0}-{1}.md" -f $today, $slug)

# 同名があれば連番付与
$counter = 2
while (Test-Path $filename) {
  $filename = Join-Path $dir ("note-{0}-{1}-{2}.md" -f $today, $slug, $counter)
  $counter++
}

# テンプレ本文（Markdownのコードブロックはチルダで閉じる）
$body = @"
# 学習ノート $today — $Title

## 今日学んだこと
- 

## 疑問点・調べたいこと
- 

## 実験したコード / メモ
~~~bash
# ここに貼る
~~~

## 明日の目標
- 
"@

# 末尾改行ありで保存（UTF-8 with BOM）
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($filename, $body, $utf8NoBom)

try { code $filename | Out-Null } catch {}
Write-Host "Created: $filename"
