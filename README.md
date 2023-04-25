# es50_final_proj

Blake Bernhardt, April Chen, and Eugene Ye

## Project summary

Live-scraping and detecting food trucks and people in the science center plaza.

## Setup

As of this writing, the Science Center Plaza livestream (formerly here: https://www.youtube.com/watch?v=JIb4EGf5uFA) has gone private. In order to get access, we (the members of this group) got private access for our individual Gmail accounts from the commonspaces team at the Smith Center. Hence, `youtube_private.py` includes code for scraping screenshots from the livestream assuming one has access to a Gmail account with access to the stream.

If you have access, you need to follow the following steps:

- In your terminal and virtual environment, run `pip install -r requirements.txt`
- Install the ca.cert certificate into your browser in order to allow Selenium to log into your Gmail account
- Duplicate the file `passwords_template.py` and rename the duplicate to `passwords.py`. Type in your Gmail username and password where indicated. `passwords.py` should be in the .gitignore and therefore should not be committed to Github, but DOUBLE CHECK THAT YOU ARE NOT COMMITTING YOUR GMAIL PASSWORD BEFORE YOU PUSH!!!!
- Run `python youtube_private.py`. You will need to manually fullscreen the video once it pops up, after that it will automatically take screenshots that will then be processed.
