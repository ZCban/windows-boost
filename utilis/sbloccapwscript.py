import subprocess
import os
import time

# Definisce il contenuto dello script PowerShell
ps_script_content = """
Write-Host "#######UNLOCK POWESHELL#####"
##abilita script powershell
# Ottiene la politica di esecuzione corrente per la macchina locale
$currentPolicy = Get-ExecutionPolicy -Scope LocalMachine

# Controlla se la politica corrente non è 'Unrestricted'
if ($currentPolicy -ne 'Unrestricted') {
    # Imposta la politica di esecuzione su 'Unrestricted'
    Set-ExecutionPolicy Unrestricted -Scope LocalMachine -Force
    Write-Host "PS ExecutionPolicy cambiata in Unrestricted."
} else {
    Write-Host "PS ExecutionPolicy è già Unrestricted."
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
time.sleep(3)

# Elimina il file dello script PowerShell dopo l'esecuzione
# Si consiglia di utilizzare questa riga con cautela e di assicurarsi che lo script PowerShell sia effettivamente terminato
os.remove(ps_script_path)

