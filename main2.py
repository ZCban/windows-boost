import os
import subprocess
import requests
import shutil

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
zip_path = os.path.join(desktop_path, "windows-boost.zip")
extract_path = os.path.join(desktop_path, "windows-boost-main")

def run_command(command):
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except subprocess.CalledProcessError:
        print(f"Error executing command: {command}")

def download_and_extract(url, folder_name="utilis"):


    # Download the zip file
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.

        with open(zip_path, 'wb') as f:
            f.write(response.content)
        print("Downloaded zip file to Desktop.")
    except requests.RequestException as e:
        print(f"Failed to download the file: {e}")
        return
    
    # Extract the zip file
    try:
        subprocess.run(f"tar -xf {zip_path} -C {desktop_path}", check=True, shell=True)
        print(f"Extracted to {extract_path}.")
    except subprocess.CalledProcessError:
        print("Failed to extract the zip file.")
        return

    # Navigate to the 'utils' folder
    os.chdir(os.path.join(extract_path, folder_name))
    print(f"Changed directory to {os.path.join(extract_path, folder_name)}.")
    os.remove(zip_path)

def main():
    # Download and prepare environment
    download_and_extract("https://github.com/ZCban/windows-boost/archive/refs/heads/main.zip")

    commands = [
        "python disable_uac.py",
        "sbloccapwscript.py",
        "installwinget.py",
        "installallVC+DX+FRAMEWORL48.py",
        "disable_windows_defender.py",
        "windows-update-hide.py",
        "disable_notifications.py",
        "disable_xbox_service.py",
        "visrtualmemory.py",
        "disable_readyboost_and_memory_compression.py",
        "disable_onedrive.py",
        "disable_firewall.py",
        "removeautostartapp.py",
        "olddeviceclean.py",
        "servicefromautotomanual.py",
        "boostinternet.py",
        "Disable-AdminPasswordPrompts.py",
        "ResetCleanV2.py",
        "PowerPlan.py"
    ]


    
    for cmd in commands:
        print(f"Running: {cmd}")
        run_command(cmd)
        print(f"{cmd} completed.")

    print("Results have been saved")


if __name__ == "__main__":
    main()
    os.remove(extract_path)
    print("Riavvio del computer in corso...")
    os.system("shutdown /r /t 0 /f /d p:4:1")
