import os
import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import colorama
import json
from colorama import Fore

colorama.init()
os.system("title WEBHOOK SPAMMER made by Swev#9999 and payed#0001")
print ( Fore.BLUE + """                                 
  ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
 |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
     |_|                                      
""" + Fore.WHITE)
def webhkspammer():
    webhook = input(Fore.WHITE + "[>] Enter The Webhook Link: ")
    message = input(Fore.WHITE + "[>] Enter The Message: ")
    delay = float(input(Fore.WHITE + "[>] Enter The Delay (Example : 0.5)"))

    while True:
        print(Fore.CYAN + "Sending --> " + message)
        print(Fore.RESET + " ")
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.CYAN + "Sent --> " + message)
        except:
            print("Something Happend! / Probably Broken Webhook -> " + webhook)
            time.sleep(5)
            exit()

x = 5
while x == 5:
    webhkspammer()