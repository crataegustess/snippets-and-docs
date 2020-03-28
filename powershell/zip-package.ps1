$packageName = "package-{0}.zip" -f (Get-Date -Format "yyyy-MM-dd-hh_mm_ss")
$SourcePath = '{bin dotnet core folder}'
$PackagePath = '{package output folder}'

$outputPackage = "$PackagePath\$PackageName"

New-Item -ItemType Directory -Path $PackagePath -Force | Out-Null
Remove-Item -Path "$SourcePath\local.settings.json" -Force -ErrorAction SilentlyContinue | Out-Null
Compress-Archive -Path "$SourcePath\*" -DestinationPath $outputPackage -Force | Out-Null