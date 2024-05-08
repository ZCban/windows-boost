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

def enable_notifications():
    commands = [
        'reg delete "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_ALLOW_TOASTS_ABOVE_LOCK" /f',
        'reg delete "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_ALLOW_CRITICAL_TOASTS_ABOVE_LOCK" /f',
        'reg delete "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_TOASTS_ENABLED" /f',
        'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "DisableNotificationCenter" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /f',
        'reg delete "HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "DisableNotificationCenter" /f',
        'reg add "HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /f',
        'reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "ToastEnabled" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /f',
        'reg delete "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "ToastEnabled" /f',
        'reg add "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /f',
        'reg delete "HKCU\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "NoToastApplicationNotification" /f',
        'reg add "HKCU\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /f',
        'reg delete "HKCU\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "NoTileApplicationNotification" /f',
        'reg add "HKCU\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "IsNotificationsEnabled" /t REG_DWORD /d "1" /f',
        #'taskkill /im explorer.exe /f',
        #'start explorer.exe'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Notifications have been enabled successfully.")

def disable_notifications():
    commands = [
        'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_ALLOW_TOASTS_ABOVE_LOCK" /t REG_DWORD /d "0" /f',
        'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_ALLOW_CRITICAL_TOASTS_ABOVE_LOCK" /t REG_DWORD /d "0" /f',
        'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_TOASTS_ENABLED" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "DisableNotificationCenter" /t REG_DWORD /d "1" /f',
        'reg add "HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "DisableNotificationCenter" /t REG_DWORD /d "1" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "ToastEnabled" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "ToastEnabled" /t REG_DWORD /d "0" /f',
        'reg add "HKCU\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "NoToastApplicationNotification" /t REG_DWORD /d "1" /f',
        'reg add "HKCU\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "NoTileApplicationNotification" /t REG_DWORD /d "1" /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "IsNotificationsEnabled" /t REG_DWORD /d "0" /f',
        #'taskkill /im explorer.exe /f',
        #'start explorer.exe'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Notifications have been disabled successfully.")


# Note: Implement the commands for disable_notifications similar to enable_notifications,
# but adjust the registry values to disable notifications as needed.

disable_notifications()
