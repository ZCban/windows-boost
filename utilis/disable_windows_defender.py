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

def enable_windows_defender():
    commands = [
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\MsSecFlt" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SecurityHealthService" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\Sense" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdBoot" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdFilter" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdNisDrv" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdNisSvc" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WinDefend" /v "Start" /t REG_DWORD /d "2" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "SecurityHealth" /t REG_EXPAND_SZ /d "%systemroot%\\system32\\SecurityHealthSystray.exe" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SgrmAgent" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SgrmBroker" /v "Start" /t REG_DWORD /d "2" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\webthreatdefsvc" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\webthreatdefusersvc" /v "Start" /t REG_DWORD /d "2" /f',
        'reg delete "HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\smartscreen.exe" /f',
        'reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations" /f',
        'reg delete "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\SmartScreen" /f',
        'reg delete "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\Signature Updates" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Windows Defender has been enabled successfully! Please restart your PC.")

def disable_windows_defender():
    commands = [
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\MsSecFlt" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SecurityHealthService" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\Sense" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdBoot" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdFilter" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdNisDrv" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdNisSvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WinDefend" /v "Start" /t REG_DWORD /d "4" /f',
        'reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "SecurityHealth" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SgrmAgent" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SgrmBroker" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\webthreatdefsvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\webthreatdefusersvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\smartscreen.exe" /v "Debugger" /t REG_SZ /d "%%windir%%\\System32\\taskkill.exe" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations" /v "DefaultFileTypeRisk" /t REG_DWORD /d "1808" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Attachments" /v "SaveZoneInformation" /t REG_DWORD /d "1" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations" /v "LowRiskFileTypes" /t REG_SZ /d ".avi;.bat;.com;.cmd;.exe;.htm;.html;.lnk;.mpg;.mpeg;.mov;.mp3;.msi;.m3u;.rar;.reg;.txt;.vbs;.wav;.zip;" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations" /v "ModRiskFileTypes" /t REG_SZ /d ".bat;.exe;.reg;.vbs;.chm;.msi;.js;.cmd" /f',
        'reg add "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\SmartScreen" /v "ConfigureAppInstallControlEnabled" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\SmartScreen" /v "ConfigureAppInstallControl" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\SmartScreen" /v "EnableSmartScreen" /t REG_DWORD /d "0" /f',
        'reg add "HKCU\\Software\\Policies\\Microsoft\\MicrosoftEdge\\PhishingFilter" /v "EnabledV9" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\Software\\Policies\\Microsoft\\MicrosoftEdge\\PhishingFilter" /v "EnabledV9" /t REG_DWORD /d "0" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Windows Defender has been disabled successfully! Please restart your PC.")

# Note: Implement the disable_windows_defender function similar to enable_windows_defender,
# but with the registry changes required to disable Windows Defender components.

# Example usage:
# enable_windows_defender()
disable_windows_defender()
