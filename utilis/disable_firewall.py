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


def enable_firewall():
    commands = [
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile" /v "EnableFirewall" /t REG_DWORD /d "1" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile" /v "EnableFirewall" /t REG_DWORD /d "1" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile" /v "EnableFirewall" /t REG_DWORD /d "1" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Windows Firewall has been enabled successfully!")

def disable_firewall():
    commands = [
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile" /v "EnableFirewall" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile" /v "EnableFirewall" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile" /v "EnableFirewall" /t REG_DWORD /d "0" /f'

    ]
    for command in commands:
        run_command_as_admin(command)
    print("Windows Firewall has been disabled successfully!")

disable_firewall()
