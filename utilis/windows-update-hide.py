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

def unhide_windows_updates():
    run_command_as_admin('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v "SettingsPageVisibility" /t REG_SZ /d "hide:cortana;privacy-automaticfiledownloads;privacy-feedback" /f')
    run_command_as_admin('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v "IsWUHidden" /t REG_DWORD /d "0" /f')
    #run_command_as_admin('taskkill /im explorer.exe /f')
    #run_command_as_admin('start explorer.exe')
    print("Windows Updates is now available in Settings.")

def hide_windows_updates():
    run_command_as_admin('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v "SettingsPageVisibility" /t REG_SZ /d "hide:cortana;privacy-automaticfiledownloads;privacy-feedback;windowsinsider;windowsupdate" /f')
    run_command_as_admin('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v "IsWUHidden" /t REG_DWORD /d "1" /f')
    #run_command_as_admin('taskkill /im explorer.exe /f')
    #run_command_as_admin('start explorer.exe')
    print("Windows Updates is now hidden!")

# Example usage:
# unhide_windows_updates()
hide_windows_updates()
