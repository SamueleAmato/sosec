import random

VPN_COUNTRIES = ["TR", "US-C", "US", "US-W", "CA", "CA-W", "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
SELECTED_COUNTRY = random.choice(VPN_COUNTRIES)

FACEBOOK_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

FACEBOOK_POST_URL = 'https://www.facebook.com/login.php'
TWITTER_LOGIN_URL = 'https://twitter.com/login/'
TWITTER_DATA_URL = 'https://twitter.com/settings/your_twitter_data'
GMAIL_SMTP_SERVER = 'smtp.gmail.com'
GMAIL_SMTP_PORT = 587

RANDOM_NUMBERS = [1, 2, 3, 4]

WORDLIST_DIR = "wordlist/"
