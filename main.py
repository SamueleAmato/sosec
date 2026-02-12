#!/usr/bin/env python3

import os
import sys
from utils.ui import start, get_main_choice, get_username, get_email, get_wordlist, get_facebook_username
from utils.vpn import get_vpn_choice, vpn_error
from modules import instagram, facebook, gmail, twitter


def handle_instagram(vpn_enabled):
    username = get_username()
    wordlist = get_wordlist()
    instagram.bruteforce(username, wordlist, vpn_enabled)


def handle_facebook(vpn_enabled):
    username = get_facebook_username()
    wordlist = get_wordlist()
    facebook.bruteforce(username, wordlist, vpn_enabled)


def handle_gmail(vpn_enabled):
    email = get_email()
    wordlist = get_wordlist()
    gmail.bruteforce(email, wordlist, vpn_enabled)


def handle_twitter(vpn_enabled):
    username = get_username()
    wordlist = get_wordlist()
    twitter.bruteforce(username, wordlist, vpn_enabled)


def main():
    start()
    
    vpn_choice = get_vpn_choice()
    vpn_enabled = vpn_choice == 1
    
    if vpn_enabled and sys.platform == "win32":
        vpn_error()

    os.system("clear")
    start()
    choice = get_main_choice()
    
    if choice == 1:
        handle_instagram(vpn_enabled)
    elif choice == 2:
        handle_facebook(vpn_enabled)
    elif choice == 3:
        handle_gmail(vpn_enabled)
    elif choice == 4:
        handle_twitter(vpn_enabled)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
