#!/usr/bin/env bash

set -e

if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Unable to detect Linux distribution."
    exit 1
fi

if [[ "$DISTRO" == "ubuntu" || "$DISTRO" == "debian" || "$DISTRO" == "kali" ]]; then
    sudo dpkg -i windscribe-cli.deb || sudo apt install -f -y
elif [[ "$DISTRO" == "arch" ]]; then
    yay -S --noconfirm windscribe-v2-bin
elif [[ "$DISTRO" == "void" ]]; then
    sudo dpkg -i windscribe-cli || xbps-install -y windscribe-cli
else
    echo "Distribution not supported."
    exit 1
fi

windscribe login

pip3 install -r cmd/requirements.txt

chmod +x linux.sh
./linux.sh

