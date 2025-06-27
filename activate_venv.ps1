# Ativa automaticamente a venv do Poetry no PowerShell
$envPath = poetry env info --path 
& "$envPath\Scripts\Activate.ps1"