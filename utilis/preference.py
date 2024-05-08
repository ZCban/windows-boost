import subprocess

def enable_auto_date_time():
    try:
        # Imposta la sincronizzazione automatica della data e dell'ora tramite il Registro di sistema
        subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\W32Time\\TimeProviders\\NtpClient" /v "Enabled" /t REG_DWORD /d 1 /f', shell=True)
        subprocess.run('w32tm /config /update', shell=True)
        print("Impostazione della data e dell'ora automatiche abilitata con successo.")
    except Exception as e:
        print("Errore durante l'abilitazione della data e dell'ora automatiche:", str(e))

def disable_auto_date_time():
    try:
        # Disabilita la sincronizzazione automatica della data e dell'ora tramite il Registro di sistema
        subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\W32Time\\TimeProviders\\NtpClient" /v "Enabled" /t REG_DWORD /d 0 /f', shell=True)
        subprocess.run('w32tm /config /update', shell=True)
        print("Impostazione della data e dell'ora automatiche disabilitata con successo.")
    except Exception as e:
        print("Errore durante la disabilitazione della data e dell'ora automatiche:", str(e))

def enable_show_hidden_files():
    try:
        # Abilita la visualizzazione di file e cartelle nascosti
        subprocess.run('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 1 /f', shell=True, check=True)
        print("La visualizzazione di file e cartelle nascosti è stata abilitata con successo.")
    except subprocess.CalledProcessError as e:
        print("Si è verificato un errore durante l'abilitazione della visualizzazione di file e cartelle nascosti:", e)
        print("Fallito.")



enable_auto_date_time()
enable_show_hidden_files()


