import ctypes
import os
import subprocess

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

def disable_readyboost_and_memory_compression():
    commands = [
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Class\\{71a27cdd-812a-11d0-bec7-08002be2092f}" /v "LowerFilters" /t REG_MULTI_SZ /d "fvevol\\0iorate" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\rdyboost" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SysMain" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "EnablePrefetcher" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "EnableSuperfetch" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\EMDMgmt" /v "GroupPolicyDisallowCaches" /t REG_DWORD /d "1" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\EMDMgmt" /v "AllowNewCachesByDefault" /t REG_DWORD /d "0" /f',
        'PowerShell -NonInteractive -NoLogo -NoProfile -Command "Disable-MMAgent -mc"',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "isMemoryCompressionEnabled" /t REG_DWORD /d "0" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("ReadyBoost and Memory Compression have been disabled successfully! Please restart your PC.")

def enable_superfetch():
    commands = [
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Class\\{71a27cdd-812a-11d0-bec7-08002be2092f}" /v "LowerFilters" /t REG_MULTI_SZ /d "fvevol\\0iorate\\0rdyboost" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\rdyboost" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SysMain" /v "Start" /t REG_DWORD /d "2" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "EnablePrefetcher" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "EnableSuperfetch" /t REG_DWORD /d "3" /f',
        'reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\EMDMgmt" /v "GroupPolicyDisallowCaches" /f',
        'reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\EMDMgmt" /v "AllowNewCachesByDefault" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Superfetch has been enabled successfully! Please restart your PC.")

# Example usage:
disable_readyboost_and_memory_compression()
# enable_superfetch()
