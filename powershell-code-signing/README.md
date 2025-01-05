# Code Signing

## Create Certificate

```powershell
New-SelfSignedCertificate `
    -Type CodeSigningCert `
    -CertStoreLocation "Cert:/CurrentUser/My" `
    -Subject "CN=$Subject" `
    -FriendlyName "$Name"
```

## Sign File

```powershell
Set-AuthenticodeSignature `
    -FilePath $File `
    -Certificate (
        (Get-ChildItem "Cert:/CurrentUser/My" -CodeSigningCert) `
        | Where-Object { $_.Subject -like "CN=*$Certificate*" }
    )
```

## Remove Signature

```powershell
$Content = (Get-Content $File -Raw)
$Content[0..(($Content | Select-String "# SIG").LineNumber - 3)] `
    | Set-Content $File
```
