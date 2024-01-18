## Made by reproachdevs on github
import os
import ctypes
try:
    from discord_webhook import DiscordWebhook
except:
    os.system('pip install discord_webhook')
    os.system('pip install DiscordWebhook')
    from discord_webhook import DiscordWebhook
try:
    import requests
except:
    os.system('pip install requests')
    import requests
try:
    from colorama import Fore, Back, Style
except:
    os.system('pip install colorama')
    from colorama import Fore, Back, Style
try:
    import fade
except:
    os.system('pip install fade')
    import fade
ctypes.windll.kernel32.SetConsoleTitleW("Rephook - Made By Reproach")
os.system('cls')

os.system('mode 50,22')
banner = r'''
                               _.._
    ┳┓    ┓┏    ┓             .'    '.
    ┣┫┏┓┏┓┣┫┏┓┏┓┃┏           (____/`\ \
    ┛┗┗ ┣┛┛┗┗┛┗┛┛┗         (  |' ' )  )
        ┛                  )  _\= _/  (
                 __..---.(`_.'  ` \    )
                `;-""-._(_( .      `; (
                /       `-`'--'     ; )
               /    /  .    ( .  ,| |(
_.-`'---...__,'    /-,..___.-'--'_| |_)
'-'``'-.._       ,'  |   / .........'
         ``;--"`;   |   `-`
             `'..__.'        
       
   [1] Spam 
   [2] Delete
   [3] Spam + Delete

'''
fadedbanner = fade.water(banner)
print(fadedbanner)

def spam():
    
    url = input("\n   Webhook > ")
    msg = input("\n   Message > ")
    amt = int(input("\n   Amount > "))
    os.system('cls')
    print("\n")

    os.system("mode 50,20")

    run = 1
    for _ in range(amt):
        
        webhook = DiscordWebhook(url=url, content=msg)
        response = webhook.execute()
        print(Fore.LIGHTCYAN_EX + "\n   [!] Message sent -", run)
        run = run + 1

def deletewebhook():
    os.system('mode 50,22')
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print(Fore.LIGHTCYAN_EX + "   [!] Sucessfull Webhook deletion")
    elif check.status_code == 200:
        print(Fore.LIGHTCYAN_EX + "    [!] Deletion Failed")

def spamdel():
    url = input("\n   Webhook > ")
    msg = input("\n   Message > ")
    amt = int(input("\n   Amount > "))
    os.system('cls')
    print("\n")
    os.system('mode 50,22')

    run = 1
    for _ in range(amt):
        
        webhook = DiscordWebhook(url=url, content=msg)
        response = webhook.execute()
        print(Fore.LIGHTCYAN_EX + "\n   [!] Message sent -", run)
        run = run + 1

    print(" ")

    requests.delete(url)
    status = requests.get(url)
    if status.status_code == 404:
        print(Fore.LIGHTCYAN_EX + "\n    [!] Sucessfull Webhook deletion")
    elif status.status_code == 200:
        print(Fore.LIGHTCYAN_EX + "\n   [!] Deletion Failed")

def status():
    check = requests.get(webhook)
    if check.status_code == 404:
       print("\n    [!] Webhook is not Active")
       os.system("pause >nul")
    elif check.status_code == 200:
       print("\n   [!] Webhook is Active")  

option = int(input(Fore.LIGHTCYAN_EX + "   >  "))

if option == 1:    
    os.system("mode 139,7")
    spam()
elif option == 2:
    status()
    os.system("mode 139,7")
    webhook = input("\n   Webhook > ")
    deletewebhook()
elif option == 3:
   
   os.system("mode 139,7")
   spamdel()
else:
    print("   Invalid Option")

os.system('pause >nul')