#!/usr/bin/env python3


import json
import os
import sys
import praw

from prawcore import NotFound


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

user_input = input("Would you like to join the previous subreddit(s) that you were "
                   "subscribed to? (Enter 'y' or 'n') " )


def joining_subreddit():
    """Check if subreddit(s) exists before joining it."""
    list_of_subreddits = []
    filename = 'subreddits.json'

    while True:
        exists = True
        # Checking to see if entered subreddit exists.
        try:
            enter_subreddits = input("\nEnter the name(s) of the subreddit(s) "
                                     "you would like to join: ")
            reddit.subreddits.search_by_name(enter_subreddits, exact=True)
        except NotFound:
            exists = False
            print("\nThis subreddit does not exist, please try again. \n")
        else:
            # Add entered subreddit to the list of subreddits and create a JSON
            # file with the list of subreddits.
            list_of_subreddits.append(enter_subreddits)
            with open(filename, 'w') as file:
                json.dump(list_of_subreddits, file)

            if list_of_subreddits:
                print("The current subreddit(s) in your list are:")
                for sub_reddit in list_of_subreddits:
                    print('-' + sub_reddit)

            continue_or_stop = input("\nWould you like to stop "
                                     "the program and join the preferred "
                                     "subreddits? (Enter 'y' or 'n') ")
            if continue_or_stop == 'y':
                # Join each subreddit in the list of subreddits.
                for sub_reddit in list_of_subreddits:
                    reddit.subreddit(sub_reddit).subscribe()
                    print(f"-Joining the subreddit: {sub_reddit}.")
                print("\nFinished joining the subreddits!")
                break
            elif continue_or_stop == 'n':
                continue
            else:
                print("That is not a valid answer. Please try again.")
                continue

            return exists


def load_subreddits_from_memory():
    """
    If the "subreddits.json" file exists, ask the user if they
    would like to join the subreddits within the JSON file.
    """
    filename = 'subreddits.json'
    try:
        with open(filename) as file:
            list_of_subreddits = json.load(file)
    except FileNotFoundError:
        print("Your subreddit(s) file could not be found. "
              "Try entering 'n' at the prompt to join subreddit(s).")
    else:
        print("\nYour current subreddits are:")
        for item in list_of_subreddits:
            print("-" + item)
        join_or_not = input("\nWould you like to join them? "
                            "(Enter 'y' or 'n')")
        if join_or_not == 'y':
            for item in list_of_subreddits:
                reddit.subreddit(item).subscribe()
        elif join_or_not == 'n':
            print("Exiting program.")
            sys.exit()


if user_input == 'y':
    load_subreddits_from_memory()
elif user_input == 'n':
    joining_subreddit()
