echo 
echo "Welcome Google Linux"
echo

sleep 4

sudo python3 -m pip install google-assistant-sdk[samples]

sudo pip install --upgrade google-assistant-library

sudo pip install --upgrade google-auth-oauthlib[tool]

google-oauthlib-tool --client-secrets /home/norman/Documents/keyassistant.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless


