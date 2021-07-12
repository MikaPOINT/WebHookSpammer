import os
import requests
from discord_webhook import DiscordWebhook
class colors:
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    blank = '\033[0m'

os.system('color c')
os.system("cls")
os.system("title WebHookRaid")
print('\n')
print('██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗██████╗  █████╗ ██╗██████╗ ███████╗██████╗ ')
print('██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗')
print('██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ ██████╔╝███████║██║██║  ██║█████╗  ██████╔╝')
print('██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ ██╔══██╗██╔══██║██║██║  ██║██╔══╝  ██╔══██╗')
print('╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗██║  ██║██║  ██║██║██████╔╝███████╗██║  ██║')
print(' ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝')
print('\n')                                                                                                       

print('Ce webhook destroyer est à utilisé avec sécurité, il est conseillé de utiliser ce tool sur un webhook qui ne vous appartient pas (comme un token grab).')
input("\n Appuyer Entrer pour continuer...")

url = str(input(" [*] Quelle est l'url du Webhook :"))
os.system('color f')
os.system("cls")
msg = str(input("[*] Quel est le message que vous voulez envoyez :"))
os.system('color d')
while True:
    webhook = DiscordWebhook(url=url, content=msg)
    response = webhook.execute()
    print('Le message à été envoyer!')
    os.system('color b')
