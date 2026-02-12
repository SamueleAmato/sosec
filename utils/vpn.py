import os
import distro
from rich.console import Console
from .colors import Color
from config import SELECTED_COUNTRY

console = Console()


def change_ip():
    try:
        if "Arch" in distro.linux_distribution()[0]:
            os.system("sudo systemctl start windscribe")
        os.system(f"\nwindscribe connect {SELECTED_COUNTRY}")
    except Exception as e:
        print(f"\n{Color.RED}VPN Error: {e}{Color.END}\n")


def vpn_error():
    print(f"\n\nERROR 0x03: {Color.RED}Unable to enable VPN on Windows\n\n{Color.END}")
    exit()


def get_vpn_choice():
    from .ui import ascii_art
    
    os.system("clear")
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
    console.print(":: 0 vpn off | 1 vpn on ::", justify="center", style="#B0DAFF")
    
    try:
        choice = int(input(f"\n\n{Color.GREEN} [choice]{Color.END} 〉"))
    except ValueError:
        print(f"\n\nERROR 0x02:{Color.RED} please enter a number between 0-1\n\n{Color.END}")
        exit()
    
    if choice > 1 or choice < 0:
        print(f"\n\nERROR 0x02:{Color.RED} please enter a number between 0-1\n\n{Color.END}")
        exit()
    
    return choice
