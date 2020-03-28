if((Get-PSRepository -Name "PSGallery").InstallationPolicy -eq "Trusted")
{
  Write-Host "PSGallery is Trusted"
}

#Setup Nuget Policy
Set-PSRepository -Name "PSGallery" -SourceLocation "https://www.powershellgallery.com/api/v2/" -InstallationPolicy Trusted