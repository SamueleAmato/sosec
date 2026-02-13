#!/usr/bin/env bash
set -e

# Detect Termux
if [ -d "/data/data/com.termux/files/usr" ]; then
    DISTRO="termux"
elif [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Unsupported system."
    exit 1
fi

if [[ "$DISTRO" == "ubuntu" || "$DISTRO" == "debian" || "$DISTRO" == "kali" ]]; then
    sudo apt update -y
    sudo apt install -y curl wget python3-pip
    wget "https://github.com/SamueleAmato/sosec/releases/download/v1.0/windscribe-cli.deb"
    sudo dpkg -i windscribe-cli.deb || sudo apt install -f -y
    windscribe-cli login

elif [[ "$DISTRO" == "arch" ]]; then
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm base-devel git python-pip
    yay -S --noconfirm windscribe-v2-bin
    windscribe-cli login

elif [[ "$DISTRO" == "void" ]]; then
    sudo xbps-install -Sy python3-pip curl -y
    wget "https://github.com/SamueleAmato/sosec/releases/download/v1.0/windscribe-cli.xbps"
    sudo xbps-install -y ./windscribe-cli.xbps
    windscribe-cli login

elif [[ "$DISTRO" == "termux" ]]; then
    pkg update -y
    pkg install -y python curl wget
fi

pip3 install -r requirements.txt

echo ""
echo "Setup complete."
echo "Run: python3 main.py"

