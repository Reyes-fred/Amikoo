sudo apt-get update
sudo apt-get install linux-headers-$(uname -r) build-essential git
git clone https://github.com/lwfinger/rtl8188eu
cd rtl8188eu  
make all  
sudo make install  
sudo insmod 8188eu.ko
