param(
    [string]$req = 'groups'
)

if($req -eq 'groups') {
    echo "You can specify a different request by passing it as a parameter, e.g. '.\scripts\Test-Request.ps1 -req tickets'"
}

Get-Content .env | ForEach-Object {
    $key, $value = $_ -split '=', 2
    Set-Variable -Name $key -Value $value -Scope Global
}

echo "Sending request to $env:HELPDESK_URL/api/v2/$req"

$response = Invoke-WebRequest -Uri  "$env:HELPDESK_URL`/api/v2/$req" -Headers @{"Authorization"="Basic $([System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($env:API_KEY+":X")))"}
$content = $response | ConvertFrom-Json | ConvertTo-Json

if ($req -match '[\/:*?"<>|]') {
    echo "The request cannot be a valid filename in Windows"
    $response = Read-Host -Prompt 'Do you want to automatically generate a filename? (Y/n)'
    if ($response -eq '' -or $response -eq 'y') {
        $req = $req -replace '[\/:*?"<>|]', '_'
    } elseif ($response -eq 'n') {
        $req = Read-Host -Prompt 'Please enter a custom name'
    }
    $req = $req -replace '[\/:*?"<>|]', '_'
}

Set-Content -Path "scripts/$req`.json" -Value $content
echo "Done! Output is in scripts/$req`.json"