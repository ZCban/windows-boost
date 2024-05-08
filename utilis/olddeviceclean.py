import subprocess
import time

# Definisce il contenuto dello script PowerShell come una singola stringa
ps_script_content = """
Import-Module PnpDevice;
$allDevices = Get-PnpDevice;
"Elenco completo dei dispositivi con stato di connessione:";
foreach ($device in $allDevices) {
    $status = if ($device.Present) { "Collegato" } else { "Non collegato" };
    "$($device.FriendlyName) - $status";
};
"`nElenco dei dispositivi Non collegati:";
$nonConnectedDevices = $allDevices | Where-Object { -not $_.Present };
foreach ($device in $nonConnectedDevices) {
    "$($device.FriendlyName) - Non collegato";
};
$confirmRemoval = 'S';
if ($confirmRemoval -eq 'S') {
    "Inizio rimozione dei dispositivi non collegati...";
    foreach ($device in $nonConnectedDevices) {
        "Rimozione del dispositivo: $($device.FriendlyName)";
        & pnputil /remove-device $device.InstanceId;
    };
    "Rimozione completata.";
} else {
    "Rimozione annullata.";
};
$desktopPath = [Environment]::GetFolderPath("Desktop");
$logFile = Join-Path -Path $desktopPath -ChildPath "OldDeviceLog.txt";
Remove-Item -Path $logFile -ErrorAction Ignore;
"""

# Comando per eseguire lo script PowerShell direttamente
run_command = ["powershell", "-Command", ps_script_content]

# Esegue lo script PowerShell
subprocess.run(run_command, shell=True)



