import os
import platform
import shutil
from time import sleep
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
    os._exit(0)

# for find os
if platform.system() == "Linux":
    print(Fore.RED, "this version is just for windows")
    sleep(3)
    os._exit(0)

if __name__ == '__main__':
    # set path
    source = "app"
    destination = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")

    # check installetion
    try:
        with open("app/data/data.txt", "r", encoding="utf-8") as data_file:
            installation = data_file.read()

        if "True" in str(installation):
            un_confirm = input("do you want to uninstall this app? (y/n): ").strip()
            if un_confirm.lower() == "y":
                try:
                    os.remove(os.path.join(destination, "main.py"))
                    shutil.rmtree(os.path.join(destination, "data"))
                    os.remove("app/data/data.txt")
                    print(Fore.GREEN, "Uninstalled successfully.")
                    sleep(3)
                    os._exit(0)

                except:
                    print(Fore.RED, "error during uninstallation")
                    sleep(3)
                    os._exit(0)
            else:
                sleep(3)
                os._exit(0)
    except:
        pass

    os.system("cls")
    
    # get data from user
    target_folder = input("Enter the full path of the folder you want to clean (e.g. C:\\Users\\YourName\\Downloads): ").strip()
    days = int(input("Enter the number of days to keep files (older files will be deleted): ").strip())
    protected_items = input("Enter files or folders to protect from deletion (separated by commas): ").strip()
    confirm = input("Save these settings and continue? (y/n): ").strip()
    
    if confirm.lower() == "y":
        # move file to startup folder
        try :
            shutil.copy("app/main.py", os.path.join(destination, "main.py"))
            # writing data file
            with open("app/data/data.txt","w+", encoding= "utf-8") as data_file:
                data_file.write(f"{days}\n{protected_items}\n{target_folder}\nTrue")
            # copy data folder to startup folder
            shutil.copytree("app/data", os.path.join(destination, "data"), dirs_exist_ok=True)
            
            print(Fore.GREEN, "installed successfully.")
            sleep(3)
            os._exit(0)
        except:
            print(Fore.RED, "error")
            sleep(3)
            os._exit(0)
    else:
        os._exit(0)