import subprocess
import os
import platform
import fade
try:
    from pypresence import Presence
except Exception as e:
    pass
import time
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
    try:
        start = time.time()
        client_id = "487918449335468033"
        RPC = Presence(client_id)
        RPC.connect()
        RPC.update(state="Made by Thiplol#0248", details="Using Dorky Dorker.", large_image="large", small_image="small", instance=True, start=start)
    except Exception as e:
        pass
print(fade.greenblue("""
▓█████▄  ▒█████   ██▀███   ██ ▄█▀     ▄████  ▓█████ ███▄    █ 
▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒      ██▒ ▀█ ▓█   ▀ ██ ▀█   █ 
░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░     ▒██░▄▄▄ ▒███  ▓██  ▀█ ██▒
░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄     ░▓█  ██ ▒▓█  ▄▓██▒  ▐▌██▒
░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄    ▒▓███▀▒▒░▒████▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒    ░▒   ▒ ░░░ ▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒ ░ ░▒ ▒░     ░   ░ ░ ░ ░  ░ ░░   ░ ▒░
 ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░      ░   ░     ░     ░   ░ ░ 
   ░        ░ ░     ░     ░  ░            ░ ░   ░           ░ 

                    made by kirk65                                 
""")) #no skid please
print("Options:")
print("1: Generate dorks.")
print("2: Generate numbers.")
print("3: Reverse keywords.")
print("4: Extractor.")
print("5: Randomize.")
print("6: Split.")
print("7: Keyword suggestion scraper.")
print("8: Dork checker.")
print("9: Antipublic.")
selecting = 1
while selecting == 1:
    try:
        option = int(input("Select what you want to use: "))
    except:
        option = 404

    if option == 1:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/pre-generate.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/pre-generate.py"])
    elif option == 2:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/numbergen.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/numbergen.py"])
    elif option == 3:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/reverse_keywords.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/reverse_keywords.py"])
    elif option == 4:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/extractor.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/extractor.py"])
    elif option == 5:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/randomize.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/randomize.py"])
    elif option == 6:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/split.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/split.py"])
    elif option == 7:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/keyword-suggestion-scraper.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/keyword-suggestion-scraper.py"])
    elif option == 8:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/dork-checker.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/dork-checker.py"])
    elif option == 9:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/antipublic.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/antipublic.py"])
    else:
        print("You didn't select a valid option, please try again.")