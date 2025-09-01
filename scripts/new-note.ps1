Param(
  [Parameter(Mandatory = $true)]
  [string]$Title
)

$ErrorActionPreference = "Stop"

# 今日の日付
$today = Get-Date -Format "yyyy-MM-dd"
$year  = Get-Date -Format "yyyy"
$month = Get-Date -Format "MM"
$day   = Get-Date -Format "dd"

# 年フォルダを作成
$yearDir = $year
if (-not (Test-Path $yearDir)) { New-Item -ItemType Directory -Path $yearDir | Out-Null }

# ファイル名: MM-DD_Title.md
$filename = Join-Path $yearDir ("{0}-{1}_{2}.md" -f $month, $day, $Title)

# 同名があれば連番付与
$counter = 2
while (Test-Path $filename) {
  $filename = Join-Path $yearDir ("{0}-{1}_{2}-{3}.md" -f $month, $day, $Title, $counter)
  $counter++
}

# 本文テンプレート
$body = @"
# $Title — $today

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

# UTF-8 (BOMなし) で保存
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($filename, $body, $utf8NoBom)

try { code $filename | Out-Null } catch {}
Write-Host "Created: $filename"
