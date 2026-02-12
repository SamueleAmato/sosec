#!/usr/bin/env bash
set -e

GITHUB_USER="samueleamato"
REPO="sosec"
RELEASE_TAG="v1.0"

if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Unable to detect Linux distribution."
    exit 1
fi

if [[ "$DISTRO" == "ubuntu" || "$DISTRO" == "debian" || "$DISTRO" == "kali" ]]; then
    sudo apt update -y
    sudo apt install -y curl wget python3-pip
    wget "https://github.com/SamueleAmato/sosec/releases/download/v1.0/windscribe-cli.deb"
    sudo dpkg -i windscribe-cli.deb || sudo apt install -f -y
elif [[ "$DISTRO" == "arch" ]]; then
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm base-devel git python-pip
    yay -S windscribe-v2-bin
elif [[ "$DISTRO" == "void" ]]; then
    sudo xbps-install -Sy python3-pip curl -y
    wget "https://github.com/SamueleAmato/sosec/releases/download/v1.0/windscribe-cli.xbps"
    sudo xbps-install -y ./windscribe-cli.xbps
else
    echo "Distribution not supported."
    exit 1
fi

windscribe-cli login

pip3 install -r cmd/requirements.txt

chmod +x linux.sh
./linux.sh
