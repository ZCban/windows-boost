import subprocess
import os
import time

# Definisce il contenuto dello script PowerShell
ps_script_content = """
Write-Host "#######INSTALL WINGET#####"
# Tentativo di eseguire un comando winget per verificare se è installato
$wingetInstalled = $true
try {
    winget --version
} catch {
    $wingetInstalled = $false
}

# Se winget non è installato, procedere con l'installazione
if (-not $wingetInstalled) {
    # Impostare la preferenza di progresso per eseguire i download in modo silenzioso
    $progressPreference = 'silentlyContinue'
    Write-Information "Downloading WinGet and its dependencies..."
    
    # Scaricare WinGet e le sue dipendenze
    Invoke-WebRequest -Uri https://aka.ms/getwinget -OutFile Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
    Invoke-WebRequest -Uri https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx -OutFile Microsoft.VCLibs.x64.14.00.Desktop.appx
    Invoke-WebRequest -Uri https://github.com/microsoft/microsoft-ui-xaml/releases/download/v2.7.3/Microsoft.UI.Xaml.2.7.x64.appx -OutFile Microsoft.UI.Xaml.2.7.x64.appx
    
    # Installare le dipendenze e WinGet
    Add-AppxPackage Microsoft.VCLibs.x64.14.00.Desktop.appx
    Add-AppxPackage Microsoft.UI.Xaml.2.7.x64.appx
    Add-AppxPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle

    # Rimuovere i file scaricati
    Remove-Item Microsoft.VCLibs.x64.14.00.Desktop.appx
    Remove-Item Microsoft.UI.Xaml.2.7.x64.appx
    Remove-Item Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle

    # Accettare i termini del Microsoft Store per WinGet
    winget search --accept-source-agreements

    Write-Information "WinGet and its dependencies have been installed."
} else {
    Write-Information "WinGet is already installed."
}


"""

# Imposta il percorso e il nome del file dello script PowerShell
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
ps_script_filename = "manage_devices.ps1"
ps_script_path = os.path.join(desktop_path, ps_script_filename)

# Scrive lo script PowerShell in un file
with open(ps_script_path, "w") as ps_script_file:
    ps_script_file.write(ps_script_content)

# Comando per eseguire lo script PowerShell come amministratore
run_as_admin_command = f"powershell Start-Process powershell -ArgumentList '-File {ps_script_path}' -Verb RunAs"

# Esegue lo script PowerShell come amministratore
subprocess.run(run_as_admin_command, shell=True)

# [OPZIONALE] Attesa per simulare l'attesa del completamento dello script
# Questo passo è opzionale e dipende da quanto tempo ci si aspetta che lo script impieghi
#time.sleep(3)

# Elimina il file dello script PowerShell dopo l'esecuzione
# Si consiglia di utilizzare questa riga con cautela e di assicurarsi che lo script PowerShell sia effettivamente terminato
#os.remove(ps_script_path)


