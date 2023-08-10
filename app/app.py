try:
    from colorama import Fore, Style
    import random
    from discord import Embed
    import requests
    import os
    import inspect
    import tkinter as tk
    from tkinter import messagebox
    from pystyle import Add, Colors, Colorate, Center, Write
    import sys

except ImportError:
    os.system('pip install colorama requests discord os inspect tkinter sys pystyle')

os.system("pip install discord.py==2.2.3")

        # Make sure that the user is running Python 3.8 or higher
if sys.version_info < (3, 8):
    exit("Python 3.8 or higher is required to run this bot!")

        # Now make sure that the discord.py library is installed or/and is up to date
try:
    from discord import app_commands, Intents, Client, Interaction
except ImportError:
            # Afficher une boîte de dialogue demandant à l'utilisateur de redémarrer
    print("Le logiciel n'est pas compatible (problème avec le import discord).")



        # inspect.cleandoc() is used to remove the indentation from the message
        # when using triple quotes (makes the code much cleaner)
        # Typicly developers woudln't use cleandoc rather they move the text
        # all the way to the left

banner1 = (f"""


██████╗░░█████╗░██████╗░░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔════╝
██████╦╝███████║██║░░██║██║░░██╗░█████╗░░
██╔══██╗██╔══██║██║░░██║██║░░╚██╗██╔══╝░░
██████╦╝██║░░██║██████╔╝╚██████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚══════╝ʙʏ Nᴏᴄᴛᴜʀɴᴀʟ""")
print(Colorate.Horizontal(Colors.red_to_white, str(banner1), 1))

print(inspect.cleandoc(f"""
    \nSalut, bienvenue sur NoBadge.
    Veuillez entrer ci-dessous le jeton de votre bot pour continuer.
                                    
    {Style.DIM}Ne fermez pas cette application après avoir entré le jeton.
    Vous pouvez la fermer une fois que le bot a été invité et que la commande a été exécutée.{Style.RESET_ALL}
    """))




while True:

    # Take input from the user if no token is detected
    token = input("> ")

            # Validates if the token you provided was correct or not
            # There is also another one called aiohttp.ClientSession() which is asynchronous
            # However for such simplicity, it is not worth playing around with async
            # and await keywords outside of the event loop
    try:
        data = requests.get("https://discord.com/api/v10/users/@me", headers={
            "Authorization": f"Bot {token}"
        }).json()
    except requests.exceptions.RequestException as e:
        if e.__class__ == requests.exceptions.ConnectionError:
            exit(f"{Fore.RED}Erreur de Connection{Fore.RESET}: Discord est souvent bloqué sur les réseaux publics, veuillez vous assurer que discord.com est accessible !")

        elif e.__class__ == requests.exceptions.Timeout:
            exit(f"{Fore.RED}Timeout{Fore.RESET} : La connexion à l'API de Discord a expiré (peut-être en raison d'un taux d'utilisation trop élevé?)")

                # Tells python to quit, along with printing some info on the error that occured
        exit(f"Unknown error has occurred! Additional info:\n{e}")

            # If the token is correct, it will continue the code
    if data.get("id", None):
        break  # Breaks out of the while loop

            # If the token is incorrect, an error will be printed
            # You will then be asked to enter a token again (while Loop)
    print(f"\nIl semble que vous avez entré un {Fore.RED}token invalide{Fore.RESET}. Veuillez entrer un jeton valide.")


