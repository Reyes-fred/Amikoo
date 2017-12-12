echo
echo "Welcome to Alexa Linux"
echo

sleep 4

cd ~/Desktop/Amikoo/

git clone https://github.com/devicehive/AlexaDevice.git

sudo apt install python3-pip git ffmpeg swig libportaudio2 portaudio19-dev libpulse-dev
sudo pip3 install requests 'git+https://github.com/moaxey/python-zeroconf' pocketsphinx pyaudio

