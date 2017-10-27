echo
echo "Welcome to Amikoo"
echo

sleep 4

git clone https://github.com/TheIoTLearningInitiative/CodeLabs.git

cd CodeLabs/

opkg update

sleep 4

sh ChichenItza/setup/setup.sh

sleep 4

sh Chicanna/setup/setup.sh

sleep 4

opkg install espeak

npm install mqtt --save




