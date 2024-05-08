import subprocess
import os
import time

# Definisce il contenuto dello script PowerShell
ps_script_content = """
# Impostazione del piano energetico su "Alte prestazioni"
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c

# Disattivazione del risparmio energetico del processore
powercfg /change standby-timeout-ac 0
powercfg /change standby-timeout-dc 0
powercfg /change hibernate-timeout-ac 0
powercfg /change hibernate-timeout-dc 0
powercfg /change monitor-timeout-ac 0
powercfg /change monitor-timeout-dc 0

# Disattivazione della sospensione ibrida
powercfg /h off

# Impostazione della CPU minima al 50% e massima al 100%
powercfg /setacvalueindex SCHEME_CURRENT SUB_PROCESSOR PROCTHROTTLEMIN 50
powercfg /setacvalueindex SCHEME_CURRENT SUB_PROCESSOR PROCTHROTTLEMAX 100

# Disattivazione delle opzioni di risparmio energetico della scheda di rete
powercfg /change standby-timeout-ac 0
powercfg /change standby-timeout-dc 0
powercfg /change hibernate-timeout-ac 0
powercfg /change hibernate-timeout-dc 0

# Impostazione della massima velocità di connessione per la scheda di rete (sostituisci "NomeConnessione" con il nome effettivo)
Get-NetAdapter | Where-Object Name -eq "NomeConnessione" | Set-NetAdapterAdvancedProperty -DisplayName "Speed & Duplex" -DisplayValue "1.0 Gbps Full Duplex"

# Aumento delle dimensioni del file di paging per migliorare la gestione della memoria virtuale
$PageFileSize = Get-WmiObject Win32_PageFileSetting
$PageFileSize.InitialSize = 4096
$PageFileSize.MaximumSize = 8192
$PageFileSize.Put()

# Disattivazione della deframmentazione automatica del disco rigido
Disable-ScheduledTask -TaskName 'ScheduledDefrag'


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
time.sleep(1)

# Elimina il file dello script PowerShell dopo l'esecuzione
# Si consiglia di utilizzare questa riga con cautela e di assicurarsi che lo script PowerShell sia effettivamente terminato
os.remove(ps_script_path)





