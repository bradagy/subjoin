# Subjoin
![image](https://i.pinimg.com/originals/f9/09/35/f90935f6acfe8bb0170bc7b34020a465.png)

### Setup
Before using Subjoin you will need to authenticate via OAuth by registering a
script on Reddit.

- Head over to this link: https://www.reddit.com/prefs/apps/
- Click on the **"Create an application"** button.
- There will be 3 different options to choose from: 
    - **Web Application**
    - **Installed Application**
    - **Script**

- Click on **Script**.

- You can enter any name for the application or just enter **Subjoin** as the name.
- Add a description or leave it blank. 

- In the redirect url, copy and paste this: http://localhost:8080. 
    - From [praw-documentation](https://praw.readthedocs.io/en/latest/getting_started/authentication.html):
        "Password Flow is the simplest type of authentication flow to work with because no callback process is involved in obtaining an access_token.
        While password flow applications do not involve a redirect URI, Reddit still requires that you provide one when registering your script application – http://localhost:8080 is a simple one to use."

- Click on **Create application.**

### Authentication
- After completing the steps above, clone this repository to your computer.
- Create a virtual environment with the command `python3 -m venv venv` in the
  subdirectory of the project.
- Change your directory back to the root directory of the project and run the
  command `pip3 install -r requirements.txt` to install the necessary Python
  modules.

- Change your directory into the subdirectory of the project which is also named **"subjoin**".

![Imgur](https://i.imgur.com/GMVUgGp.png)

- **Do not run the file yet.** There will be a file called `create_secrets.sh`
- Run this file and enter the information required. This script will create a
  file called `.env` which will allow the secrets that were generated in your script application to work correctly with the program.
- Run the command `source .env` which will make the variables inside the `.env`
  file active within your current shell.

- From [praw-documentation](https://praw.readthedocs.io/en/latest/getting_started/authentication.html):
    "In order to use a password flow application with PRAW you need four pieces of information:

    - client_id: The client ID is the 14-character string listed just under “personal use script” for the desired developed application
    - client_secret: The client secret is the 27-character string listed adjacent to secret for the application.
    - password: The password for the Reddit account used to register the application.
    - username:	The username of the Reddit account used to register the application."

- Once this file has been generated, find the file `test_run.sh` **(located in the subdirectory of the project)** and run it. The output of
  this program should display your Reddit username. If this works, everything should work correctly.

![Imgur](https://i.imgur.com/GMVUgGp.png)

### Joining Subreddits
- After completing the steps above, find the `subjoin.py` file and run it. The program will
  ask you for the name of the subreddit(s) you would like to join. You can enter as
  many as you wish. For every 3 subreddits that you join, your subscribed list
  of subreddits will be displayed to you. This will help you keep track of what
  subreddits you're subscribing to.

- Once the program finishes joining the subreddits, you
  will see a `subreddits.json` file. **DO NOT LOSE THIS FILE**. This file will make it easier to join the same subreddits on another account. 
- **You cannot use the same authentication information for different accounts.  You will need to follow the Authentication steps listed above for each account.**
