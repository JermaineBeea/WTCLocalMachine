#!/bin/bash
# script by onrambu022 CPT
# hope this works
sudo apt update
sudo apt install -y build-essential git
git clone https://github.com/lwfinger/rtw89.git
cd rtw89
make
sudo make install
sudo mkdir /usr/lib/firmware/rtw89
sudo cp rtw8852a_fw.bin /usr/lib/firmware/rtw89
sudo modprobe rtw89pci
sudo reboot
