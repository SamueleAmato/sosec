import os
import time
from rich.console import Console
from .colors import Color
from asciiart import ascii_art

console = Console()


def start():
    console.print(ascii_art, justify="center", style="#B0DAFF bold")

def get_main_choice():
    console.print(":: 1 instagram | 2 facebook | 3 gmail | 4 twitter ::", 
                  justify="center", style="#B0DAFF")
    
    try:
        choice = int(input(f"\n\n{Color.GREEN} [choice]{Color.END} 〉"))
    except ValueError:
        print(f"\n\nERROR 0x01:{Color.RED} please enter a number\n\n{Color.END}")
        exit()
    
    if choice > 4 or choice < 1:
        print(f"\n\nERROR 0x02:{Color.RED} please enter a number between 1-4\n\n{Color.END}")
        exit()
    
    return choice


def get_username():
    os.system("clear")
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
    console.print(":: username ::", justify="center", style="#B0DAFF")
    uname = input(f"\n\n{Color.GREEN} [choice]{Color.END} 〉@")
    return uname


def get_email():
    os.system("clear")
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
    console.print(":: email ::", justify="center", style="#B0DAFF")
    email = input(f"\n\n{Color.GREEN} [choice]{Color.END} 〉")
    return email


def get_facebook_username():
    os.system("clear")
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
    console.print(":: username ::", justify="center", style="#B0DAFF")
    uname = input(f"\n\n{Color.GREEN} [choice]{Color.END} 〉")
    return uname


def get_wordlist():
    os.system("clear")
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
    console.print(":: wordlist ::", justify="center", style="#B0DAFF")
    wordlist = input(f"\n\n{Color.GREEN} [wordlist absolute path]{Color.END} 〉")
    return wordlist


def get_amount():
    os.system("clear")
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
    console.print(":: amount ::", justify="center", style="#B0DAFF")
    
    try:
        amount = int(input(f"\n\n{Color.GREEN} [choice]{Color.END} 〉"))
    except ValueError:
        print(f"\n\nERROR 2x00:{Color.RED} please enter a number\n\n{Color.END}")
        exit()
    
    return amount


def display_ascii():
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
