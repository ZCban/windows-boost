import subprocess
import ctypes

# Lista dei pacchetti Xbox da disabilitare/riabilitare
xbox_packages = [
    "Microsoft.XboxApp",
    "Microsoft.XboxGameOverlay",
    "Microsoft.XboxGamingOverlay",
    "Microsoft.XboxIdentityProvider",
    "Microsoft.XboxSpeechToTextOverlay",
    "Microsoft.Xbox.TCUI"
]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_command_as_admin(command):
    if is_admin():
        try:
            result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True, check=True)
            print(f"Output: {result.stdout}")
            if result.stderr:
                print(f"Error: {result.stderr}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")
    else:
        # In questo caso, non è possibile elevare direttamente i comandi PowerShell tramite ShellExecuteW
        # come si farebbe con un comando cmd.exe o con un eseguibile. Potrebbe essere necessario
        # avviare PowerShell con privilegi elevati e passare il comando.
        print("Questo script necessita di privilegi di amministratore per eseguire modifiche.")

def disable_xbox_packages():
    if not is_admin():
        print("Riavvia lo script come amministratore per disabilitare i pacchetti Xbox.")
        return
    try:
        for package in xbox_packages:
            command = f'Get-AppxPackage {package} | Remove-AppxPackage'
            run_command_as_admin(command)
    except Exception as e:
        print(f"Errore durante la disabilitazione dei pacchetti Xbox: {e}")

def enable_xbox_packages():
    if not is_admin():
        print("Riavvia lo script come amministratore per riabilitare i pacchetti Xbox.")
        return
    try:
        for package in xbox_packages:
            command = f'Get-AppxPackage -AllUsers {package} | Foreach {{Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\\AppXManifest.xml"}}'
            run_command_as_admin(command)
    except Exception as e:
        print(f"Errore durante la riabilitazione dei pacchetti Xbox: {e}")

# Esempio di utilizzo
disable_xbox_packages()
# enable_xbox_packages()

