Behold, the Wikia fetcher is on steroids now! Or should I say on Seleniumoids? Since they've disabled File: directories when you aren't logged into Fandom, even Selenium was brought to on its knees. However, little do they know that you can actually attach a profile to Selenium and actually do the automation process while being logged in!

## How to run

- Clone/fetch this rep, I'm saying this because otherwise you'll need to go ahead and download Geckodriver anyway, so I'm cutting you a slack and already including it in here
- Install Python 3 (3.6.8 if you will, that's what I've used for this)
- `cd` to the folder where this repo is located and do `python -m pip install -r install.py`
- Install Firefox if you don't have it
- Run Firefox with `firefox.exe -p` from Command Shell, Run or w/e
- Create a new profile and launch Firefox with it (you might wanna untick "Use this profile on launch by default"), **note down the path of the profile you've just created**
- Go to Wikia/Fandom and log into your account or create one if you don't have one
- Go to `fetch.py`, you should see the comment I've written there
- Run the script with `python fetch.py` and watch the show as images of shipgirls are downloaded