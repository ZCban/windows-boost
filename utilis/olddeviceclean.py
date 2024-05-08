import subprocess
import os
import time
import tempfile

# Definisce il contenuto dello script PowerShell
ps_script_content = """
# Importa il modulo PnpDevice
Import-Module PnpDevice

# Ottiene tutti i dispositivi PnP
$allDevices = Get-PnpDevice

# Stampa l'elenco completo dei dispositivi con lo stato di connessione
"Elenco completo dei dispositivi con stato di connessione:"
foreach ($device in $allDevices) {
    $status = if ($device.Present) { "Collegato" } else { "Non collegato" }
    "$($device.FriendlyName) - $status"
}

# Stampa solo i dispositivi non collegati
"`nElenco dei dispositivi Non collegati:"
$nonConnectedDevices = $allDevices | Where-Object { -not $_.Present }
foreach ($device in $nonConnectedDevices) {
    "$($device.FriendlyName) - Non collegato"
}

# Chiede conferma prima di procedere con la rimozione
$confirmRemoval = 'S' #Read-Host "Vuoi procedere con la rimozione dei dispositivi non collegati? (S/N)"
if ($confirmRemoval -eq 'S') {
    "Inizio rimozione dei dispositivi non collegati..."
    foreach ($device in $nonConnectedDevices) {
        "Rimozione del dispositivo: $($device.FriendlyName)"
        & pnputil /remove-device $device.InstanceId
    }
    "Rimozione completata."
} else {
    "Rimozione annullata."
}

# Rimuove il file di log se esiste
$desktopPath = [Environment]::GetFolderPath("Desktop")
$logFile = Join-Path -Path $desktopPath -ChildPath "OldDeviceLog.txt"
Remove-Item -Path $logFile -ErrorAction Ignore
"""

# Ottiene il percorso della directory temporanea del sistema
temp_dir = tempfile.gettempdir()

# Imposta il nome del file dello script PowerShell
ps_script_filename = "manage_devices.ps1"
ps_script_path = os.path.join(temp_dir, ps_script_filename)

# Scrive lo script PowerShell in un file
with open(ps_script_path, "w") as ps_script_file:
    ps_script_file.write(ps_script_content)

# Comando per eseguire lo script PowerShell come amministratore
run_as_admin_command = f"powershell Start-Process powershell -ArgumentList '-File {ps_script_path}' -Verb RunAs"

# Esegue lo script PowerShell come amministratore
subprocess.run(run_as_admin_command, shell=True)

# Elimina il file dello script PowerShell dopo l'esecuzione
# Si consiglia di utilizzare questa riga con cautela e di assicurarsi che lo script PowerShell sia effettivamente terminato
os.remove(ps_script_path)

