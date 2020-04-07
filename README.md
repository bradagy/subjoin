# Subjoin
![image](https://i.pinimg.com/originals/f9/09/35/f90935f6acfe8bb0170bc7b34020a465.png)

### Setup
Before using Subjoin you will need to authenticate via OAuth by registering a
script on Reddit.

- Head over to this link: https://www.reddit.com/prefs/apps/
- Click on the **"Create an application"** button.
- There will be 3 different options to choose from: **Web Application, Installed
  Application, or Script**. Click on **Script**.
- You can enter any name for the application or just enter **Subjoin** as the
  name.
- Add a description or leave it blank. 

- In the redirect url, copy and paste this: http://localhost:8080. 
    - From ![PRAW DOCUMENTATION](https://praw.readthedocs.io/en/latest/getting_started/authentication.html)
        "Password Flow is the simplest type of authentication flow to work with because no callback process is involved in obtaining an access_token.
        While password flow applications do not involve a redirect URI, Reddit still requires that you provide one when registering your script application – http://localhost:8080 is a simple one to use."

- Click on **Create application.**


### Authentication
- After completing the steps above, clone this repository. to your computer.
- Find the file **subjoin.py** in the cloned repository. Follow these steps and
  change the values in the script according to the four pieces of information
  that were given to you when you created the **Script** application.

- From ![PRAW DOCUMENTATION](https://praw.readthedocs.io/en/latest/getting_started/authentication.html)
    In order to use a password flow application with PRAW you need four pieces of information:

    client_id:	The client ID is the 14-character string listed just under “personal use script” for the desired developed application
    client_secret:	The client secret is the 27-character string listed adjacent to secret for the application.
    password:	The password for the Reddit account used to register the application.
    username:	The username of the Reddit account used to register the application.
    With this information authorizing as username using a password flow app is as simple as:

    reddit = praw.Reddit(client_id='<your-client-id>',
                         client_secret='<your-client_secret>',
                         password='your-reddit-password',
                         user_agent='testscript by /u/<your-reddit-username>',
                         username='<your-reddit-username')
    To verify that you are authenticated as the correct user run:

    print(reddit.user.me())
    The output should contain the same name as you entered for username.
