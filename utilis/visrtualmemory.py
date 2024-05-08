import subprocess
import ctypes
import os
import datetime

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_command_as_admin(command):
    if is_admin():
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            print(f"Output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", f'"{os.path.abspath(__file__)}" {command}', None, 1)

def enable_virtual_memory():
    try:
        # Set paging file size to automatic for all drives
        run_command_as_admin('wmic computersystem set AutomaticManagedPagefile=True')
        print("La gestione automatica del file di paging è stata abilitata con successo.")
    except subprocess.CalledProcessError as e:
        print("Si è verificato un errore durante l'abilitazione della gestione automatica del file di paging:", e)
        print("Fallito.")

def disable_virtual_memory():
    try:
        # Disable automatic paging file management for all drives
        run_command_as_admin('wmic computersystem set AutomaticManagedPagefile=False')
        print("La gestione automatica del file di paging è stata disabilitata con successo.")
    except subprocess.CalledProcessError as e:
        print("Si è verificato un errore durante la disabilitazione della gestione automatica del file di paging:", e)
        print("Fallito.")

disable_virtual_memory()
