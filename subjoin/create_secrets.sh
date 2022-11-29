#!/bin/bash

read -p "Enter your Client ID: " CLIENT_ID
echo "export CLIENT_ID='$CLIENT_ID'" >> .env

read -p "Enter your Client Secret: " CLIENT_SECRET
echo "export CLIENT_SECRET='$CLIENT_SECRET'" >> .env

read -p "Enter your reddit password: " PASSWORD
echo "export PASSWORD='$PASSWORD'" >> .env

read -p "Enter your reddit username: " USERNAME
echo "export USERNAME='$USERNAME'" >> .env

echo "export USERAGENT='script by /u/$USERNAME'" >> .env
