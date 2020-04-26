#!/usr/bin/env python3


import os
import praw


# Accessing secret environment variables.
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
PASSWORD = os.environ.get('PASSWORD')
USERNAME = os.environ.get('USERNAME')
USERAGENT = os.environ.get('USERAGENT')

# Authorizing with Praw.
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent=USERAGENT,
                     username=USERNAME)

print(reddit.user.me())
