$exclude = @("venv", "datapool-examples.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "datapool-examples.zip" -Force