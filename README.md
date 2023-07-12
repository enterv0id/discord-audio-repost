# Discord Audio-to-Video Converter Bot

This Discord bot converts audio files sent in channels to video files with text overlay and replies with the converted videos so mobile users can listen to the files easily. It uses the MoviePy library and ImageMagick to handle the audio-to-video conversion.


# Setting up to run the bot!

## 1. Clone this Repo
Make sure git is installed on your computer. To check if you have git, in the console run
```
git
```
If an error shows up, you will need to install git on your computer. See here for instructions: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Otherwise, open up console/command prompt in the directory you wish to clone this project in.
run the command
```
 clone https://github.com/enterv0id/Audio_Reposter_Discord.git
```
Now you have all the code in this repo cloned to your computer!!


## 2. Install Dependencies
 This package relies on Discord.py and MoviePy packages
```
pip install -r requirements.txt
```

## 3. Installing ImageMagick
Download and install ImageMagick software from the official website:
https://imagemagick.org/script/download.php

Note: Make sure to select the correct version compatible with your operating system (Windows, Linux, or macOS).
Once it's installed, make sure you're using the correct path to the ImageMagick in bot.py

``change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})``

## 4. Configure the Bot
Open the bot.py file in a text editor.
- Replace `add-your-guild-id-here` with the ID of the Discord guild (server) you want to monitor for audio file conversions. You can obtain the guild ID by enabling Developer Mode in your Discord client and right-clicking on the guild to copy its ID.

You can create a bot and obtain its token by following the Discord bot creation guide: https://discordpy.readthedocs.io/en/stable/discord.html

Go to https://discordapp.com/developers/applications/me and login with your discord account. 

Click on `New Application`. Name your application anything you want, (but try to make it unique, if too many bots have the same name, discord won't let you use this username)! 

Next, click on the `Bot` text on the left hand side of the developer panel.

Then click on `Add Bot` and confirm to create your discord bot

Under `TOKEN`, click on the `Copy` button.

Now come back to your code and paste the token in the `bot.py` file replacing the `place-your-token-here` with your bot's token
```
client.run('place-your-token-here')
```

**KEEP YOUR BOT'S TOKEN SAFE!! It is the equivalent as the login information for your bot! Anyone with access to the token has full permission to run anything off of your bot!!!**

*If you make a github repo, **make sure it is set to private if it includes your token**

## 4. Adding the bot to a server

To add your bot to a discord server, head back to the discord developer panel. 

Click on `OAuth2` on the left-hand side. 

In the `Scopes` grid of checkboxes, check `bot` and select any permissions you wish to give to the bot. 

Then click on the `Copy` button next to long url in the scopes box and goto the given link to add the bot to your server


## 5. Running the bot

Run the bot script using the following command:
```
python bot.py
```

without any additional errors, then **CONGRATULATIONS!!**

To test if the bot is fully working, go to the server that you added the bot to and post an audio file.

If the bot replies with the mp4 version, you are all set!!

Tested on Window 10
