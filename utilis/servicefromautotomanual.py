import subprocess
import os
import time

# Definisce il contenuto dello script PowerShell
ps_script_content = """
# Lista dei servizi che non si desidera cambiare in manuale
$serviziDaMantenereAutomatici = @(
    "Windows Event Log",
    "Security Center",
    "Themes",
    "User Profile Service",
    "RPC Endpoint Mapper",
    "Remote Procedure Call (RPC)",
    "Group Policy Client",
    "Print Spooler",
    "Background Tasks Infrastructure Service",
    "CoreMessaging",
    "Display Policy Service",
    "DNS Client",
    "Task Scheduler")

# Ottieni tutti i servizi in avvio automatico
$autoStartServices = Get-Service | Where-Object { $_.StartType -eq 'Automatic' }

# Filtra i servizi di Windows
$windowsServices = $autoStartServices | Where-Object { $_.DisplayName -match 'Windows' }

# Filtra i servizi di terze parti
$thirdPartyServices = $autoStartServices | Where-Object { $_.DisplayName -notmatch 'Windows' }

# Visualizza i servizi di Windows in avvio automatico
Write-Host "Servizi di Windows in avvio automatico:"
$windowsServices | Format-Table -Property DisplayName, StartType

# Visualizza i servizi di terze parti in avvio automatico
Write-Host "Servizi di terze parti in avvio automatico:"
$thirdPartyServices | Format-Table -Property DisplayName, StartType

# Imposta tutti i servizi di terze parti in avvio automatico a manuale
foreach ($service in $thirdPartyServices) {
    # Verifica se il servizio non è nella lista dei servizi da mantenere automatici
    if ($service.DisplayName -notin $serviziDaMantenereAutomatici) {
        try {
            $service | Set-Service -StartupType Manual -ErrorAction Stop
            Write-Host "Servizio $($service.DisplayName) impostato a manuale."
        } catch {
            Write-Host "Errore durante l'impostazione del servizio $($service.DisplayName): $_"
        }
    } else {
        Write-Host "Il servizio $($service.DisplayName) è nella lista dei servizi da mantenere automatici, quindi non verrà cambiato in manuale."
    }
}

# Visualizza un messaggio di conferma
Write-Host "I servizi di terze parti in avvio automatico sono stati impostati a manuale."

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
time.sleep(8)

# Elimina il file dello script PowerShell dopo l'esecuzione
# Si consiglia di utilizzare questa riga con cautela e di assicurarsi che lo script PowerShell sia effettivamente terminato
os.remove(ps_script_path)

