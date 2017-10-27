echo
echo "Welcome to Amikoo"
echo

sleep 4

git clone https://github.com/TheIoTLearningInitiative/CodeLabs.git

cd CodeLabs/

sudo apt-get update

sleep 4

sh ChichenItza/setup/setup.sh

sleep 4

sh Chicanna/setup/setup.sh

sleep 4

sudo apt-get install espeak
sudo apt-get install npm
sudo apt-get install fswebcam
sudo apt-get install mpg123
sudo apt-get install feh
sudo apt-get install vlc

npm install mqtt --save




