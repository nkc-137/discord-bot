# OGWolf's discord bot guild
**Note:** The repo is still very rudimentary, there is going to be some figuring out before you can run them bots. Below is some guidance on how you can it working.  
## How to run
1. Install the dependencies using pip
2. `bots` folder contains the logic for the bots
3. Before you can run bots, you will need discord `token` for filthy frank bot and you would need an additional youtube API `token` to run the phasmo bot.
4. Copy those tokens to `.env`, that's where the code picks it from
4. `main.py` is the entry point. Just run `python3 main.py` to get them bots running.

## Things to keep in mind
1. The tokens you see lying around in the code are fakes. Please don't commit the tokens. If you do, Discord will revoke that token. We will have to generate a new one.
2. Let's follow scout rule: "Leave the campground cleaner than you found it."
3. Choose descriptive and unambiguous names for objects.
4. Github has changed it's AuthN strategy - This [documentation](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls) can guide you more.
4. Have fun!

## References
1. https://discordpy.readthedocs.io/en/stable/
2. https://developers.google.com/youtube/v3
3. https://docs.python.org/3/library/asyncio.html