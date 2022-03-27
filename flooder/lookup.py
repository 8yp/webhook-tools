from colorama import init, Fore; init()
import requests
import os
import time

os.system("title WEBHOOK LOOKUP made by Swev#9999 and payed#0001")
print ( Fore.BLUE + """
               _     _                 _      _             _                
 __      _____| |__ | |__   ___   ___ | | __ | | ___   ___ | | ___   _ _ __  
 \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | |/ _ \ / _ \| |/ / | | | '_ \ 
  \ V  V /  __/ |_) | | | | (_) | (_) |   <  | | (_) | (_) |   <| |_| | |_) |
   \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_|\___/ \___/|_|\_\\__,_| .__/ 
                                                                      |_| 
""" + Fore.WHITE)
webhook = input ("Enter the webhook you want to lookup: ")
r=requests.get(webhook)
if "Uknown Webhook" in r.text:
    print("Invalid Webhook")
    exit()
r=r.json()
webhooktype = r["type"]
webhookid = r["id"]
webhookname = r["name"]
webhookavatar = r["avatar"]
channelid = r["channel_id"]
guildid = r["guild_id"]
appid = r["application_id"]
webhooktoken = r["token"]
print ("saved in webhook.txt")
time.sleep(3)
with open("webhook.txt", "w") as f:
    f.write(f"""
Webhook Type: {webhooktype}
Webhook ID: {webhookid}
Webhook Name: {webhookname}
Webhook Avatar: {webhookavatar}
Channel ID: {channelid}
Guild ID: {guildid}
Webhook Token: {webhooktoken}
Webhook: {webhook}""")