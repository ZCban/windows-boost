import subprocess
import os
import time

# Definisce il contenuto dello script PowerShell
ps_script_content = """
# Aumenta la dimensione della coda di ricezione TCP
netsh int tcp set global autotuninglevel=normal

# Abilita il Direct Cache Access per migliorare le prestazioni della rete
netsh int tcp set global dca=enabled

# Disabilita l'agendamento del pacchetto QoS per prevenire la riserva di larghezza di banda
gpupdate /force

# Disabilita l'indice di scaling della finestra TCP per migliorare le prestazioni di trasferimento dati su larghe distanze
netsh int tcp set global rss=enabled ecncapability=enabled

netsh int tcp set global autotuninglevel=disabled

#elimina cache dns
ipconfig /flushdns

# Reset client DNS
netsh interface ip delete arpcache
netsh winsock reset

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

import winreg as reg

def set_irp_stack_size(key_path, value_name, value):
    try:
        # Apri la chiave del registro di sistema in modalità scrittura
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
    except FileNotFoundError:
        # Se la chiave non esiste, creala
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)

    # Imposta il valore della chiave
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value)
    reg.CloseKey(key)
    print(f"Value '{value_name}' set to {value} in '{key_path}'.")

key_path = r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters"
value_name = "IRPStackSize"
value = 32

set_irp_stack_size(key_path, value_name, value)

def set_sizreqbuf(key_path, value_name, value):
    try:
        # Apri la chiave del registro di sistema in modalità scrittura
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
    except FileNotFoundError:
        # Se la chiave non esiste, creala
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)

    # Imposta il valore della chiave
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value)
    reg.CloseKey(key)
    print(f"Value '{value_name}' set to {value} in '{key_path}'.")

key_path = r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters"
value_name = "SizReqBuf"

# Qui puoi scegliere il valore che preferisci tra 17424 e 4356
value = 4356  # o 4356

set_sizreqbuf(key_path, value_name, value)

import winreg as reg

def set_default_ttl(key_path, value_name, value):
    try:
        # Apri la chiave del registro di sistema in modalità scrittura
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
    except FileNotFoundError:
        # Se la chiave non esiste, creala
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)

    # Imposta il valore della chiave
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value)
    reg.CloseKey(key)
    print(f"Value '{value_name}' set to {value} in '{key_path}'.")

key_path = r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters"
value_name = "DefaultTTL"
value = 62  # Imposta il TTL a 62

set_default_ttl(key_path, value_name, value)

import winreg as reg

def set_tcp1323opts(key_path, value_name, value):
    try:
        # Apri la chiave del registro di sistema in modalità scrittura
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
    except FileNotFoundError:
        # Se la chiave non esiste, creala
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)

    # Imposta il valore della chiave
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value)
    reg.CloseKey(key)
    print(f"Value '{value_name}' set to {value} in '{key_path}'.")

key_path = r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters"
value_name = "TCP1323Opts"
value = 1  # Imposta TCP1323Opts a 1

set_tcp1323opts(key_path, value_name, value)

import winreg as reg

def set_max_free_tcbs(key_path, value_name, value):
    try:
        # Apri la chiave del registro di sistema in modalità scrittura
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
    except FileNotFoundError:
        # Se la chiave non esiste, creala
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)

    # Imposta il valore della chiave
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value)
    reg.CloseKey(key)
    print(f"Value '{value_name}' set to {value} in '{key_path}'.")

key_path = r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters"
value_name = "MaxFreeTcbs"
value = 65536  # Imposta MaxFreeTcbs a 65536

set_max_free_tcbs(key_path, value_name, value)

import winreg as reg

def set_max_user_port(key_path, value_name, value):
    try:
        # Apri la chiave del registro di sistema in modalità scrittura
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
    except FileNotFoundError:
        # Se la chiave non esiste, creala
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)

    # Imposta il valore della chiave
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value)
    reg.CloseKey(key)
    print(f"Value '{value_name}' set to {value} in '{key_path}'.")

key_path = r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters"
value_name = "MaxUserPort"
value = 65534  # Imposta MaxUserPort a 65534

set_max_user_port(key_path, value_name, value)

import winreg as reg

def set_global_max_tcp_window_size(key_path, value_name, value):
    try:
        # Apri la chiave del registro di sistema in modalità scrittura
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
    except FileNotFoundError:
        # Se la chiave non esiste, creala
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)

    # Imposta il valore della chiave
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value)
    reg.CloseKey(key)
    print(f"Value '{value_name}' set to {value} in '{key_path}'.")

key_path = r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters"
value_name = "GlobalMaxTcpWindowSize"
value = 65535  # Imposta GlobalMaxTcpWindowSize a 65535

set_global_max_tcp_window_size(key_path, value_name, value)


