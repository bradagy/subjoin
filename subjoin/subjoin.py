#!/usr/bin/env python3


import json
import os
import sys
import praw

from prawcore import NotFound


CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
PASSWORD = os.environ.get('PASSWORD')
USERNAME = os.environ.get('USERNAME')
USERAGENT = os.environ.get('USERAGENT')


def login():
    return praw.Reddit(client_id=CLIENT_ID,
                       client_secret=CLIENT_SECRET,
                       password=PASSWORD,
                       user_agent=USERAGENT,
                       username=USERNAME)


reddit = login()


def joining_subreddit():
    """Check if subreddit(s) exists before joining it."""
    list_of_subreddits = []
    filename = 'subreddits.json'

    while True:
        exists = True
        try:
            enter_subreddits = input("\nEnter the name(s) of the subreddit(s) "
                                     "you would like to join: ")
            reddit.subreddits.search_by_name(enter_subreddits, exact=True)
        except NotFound:
            exists = False
            print("\nThis subreddit does not exist, please try again. \n")
        else:
            list_of_subreddits.append(enter_subreddits)
            # This will help keep track of what subreddits are being added.
            if len(list_of_subreddits) % 3 == 0:
                print("The current subreddit(s) in your list are:")
                for sub_reddit in list_of_subreddits:
                    print(f"-{sub_reddit}")

                continue_or_stop = input("\nWould you like to stop "
                                         "the program and join the preferred "
                                         "subreddits? [Y/n] ")
                if continue_or_stop in ('Y', 'y'):
                    with open(filename, 'w') as file:
                        json.dump(list_of_subreddits, file, indent=4)
                    for sub_reddit in list_of_subreddits:
                        reddit.subreddit(sub_reddit).subscribe()
                        print(f"-Joining the subreddit: {sub_reddit}.")
                    print("\nFinished joining the subreddits!")
                    break
                elif continue_or_stop in ('N', 'n'):
                    continue
                else:
                    print("That is not a valid answer. Please try again.")
            continue

            return exists


def load_subreddits_from_memory():
    """If subreddits.json file exists, ask the user if they would like to join
    it (join subreddits if the answer is "yes".). If the user
    refuses, exit the program."""
    try:
        with open('subreddits.json') as file:
            list_of_subreddits = json.load(file)
    except FileNotFoundError:
        print("Your subreddit(s) file could not be found. "
              "Try entering 'n' at the prompt to join subreddit(s).\n")
    else:
        print("\nYour current subreddits are:")
        for item in list_of_subreddits:
            print(f"-{item}")
        join_or_not = input("\nWould you like to join them? "
                            "[Y/n] ")
        if join_or_not in ('Y', 'y'):
            for item in list_of_subreddits:
                print(f"-Joining the subreddit: {item}.")
                reddit.subreddit(item).subscribe()
            print('\nFinished joining the subreddits!')
        elif join_or_not in ('N', 'n'):
            print("\nExiting the program.")
            sys.exit()


def main():
    while True:
        user_input = input("Would you like to join the previous subreddit(s) "
                           " you were subscribed to? [Y/n] ")
        if user_input in ('Y', 'y'):
            load_subreddits_from_memory()
        elif user_input in ('N', 'n'):
            joining_subreddit()
        else:
            print('That was not a valid answer please try again.')
            continue


if __name__ == '__main__':
    main()
