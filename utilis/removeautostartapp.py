import winreg

# Definizione dei percorsi nel Registro di sistema
registry_paths = [
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"),
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"),
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_CURRENT_USER, r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run"),
]

def remove_startup_entries(hive, path):
    try:
        key = winreg.OpenKey(hive, path, access=winreg.KEY_ALL_ACCESS)
        count = 0
        while True:
            # Tentativo di elencare tutte le voci
            try:
                value = winreg.EnumValue(key, 0)
                winreg.DeleteValue(key, value[0])
                print(f"Rimossa l'entrata di avvio automatico: {value[0]} da {path}")
                count += 1
            except OSError:
                break
        if count == 0:
            print(f"Nessuna chiave di avvio automatico trovata da eliminare in {path}.")
        winreg.CloseKey(key)
    except PermissionError:
        print(f"Permessi insufficienti per modificare il registro in {path}.")
    except FileNotFoundError:
        print(f"Il percorso specificato {path} non esiste nel registro.")

# Esegui la funzione per ogni percorso nel Registro di sistema
for hive, path in registry_paths:
    remove_startup_entries(hive, path)
