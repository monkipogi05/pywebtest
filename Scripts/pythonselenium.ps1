$version = "3.6.4"
$url = "https://www.python.org/ftp/python/$version/python-$version.exe"
$python = "C:\python.exe"
$wc = New-Object System.Net.WebClient
$wc.DownloadFile($url, $python)
Start-Process "C:\python.exe"  -WorkingDirectory "C:\W\" -ArgumentList '/s', '/v', '/qn' -Wait
$pathInstall = "C:\Users\autotest\AppData\Local\Programs\Python\Python36-32"
[Environment]::SetEnvironmentVariable("Path", "$env:Path;$pathInstall\;$pathInstall\Scripts\", "User")
