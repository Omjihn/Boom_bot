<h1 align="center">
	Boom_bot
</h1>

# A Discord Youtube music bot

> [!NOTE]
> This project has been tested on Ubuntu and Raspberry Pi OS.
> It should works on MacOS and Windows but untested

This project require Python 3 :

    > sudo apt install python3

You also need git installed to download youtube_dl library :

    > sudo apt install git

### Python dependencies :

I recommend installing them in a virtual environment (you can choose any name you want for the 4th argument):

    > python -m venv myenv

Each time you need to start using the bot, you must activate your environment with this command:
    
    > source myenv/bin/activate

After this, you may see your environment name in your terminal.

### Now you can install all the Python libraries you need (They will be installed in your environment):

### Discord.py :
Needed to use Discord API

    > pip install discord.py discord    

### Youtube_dl :
Used to download Youtube musics

    > pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"

### Dot-env :
Needed to add the discord bot token in the .env file

    > pip install python-dotenv

# Create your bot :

Now you need to create your bot

- Go to this link and log in : https://discord.com/developers/applications

- Click on "New Application", give it a name, and click create.

- Go to the OAuth2 tab and select at least these permissions:

    ![Screen_github](https://github.com/Omjihn/Boom_bot/assets/110061001/66d78cad-827d-4e29-9951-b87a3414df98)

- Then get the URL at the bottom of the page, it will allows you to invite the bot to a server. (Make sure you have the right to add a bot to the server you want to add it to)

- Now go to the Bot tab, click reset your token, and put it in the .env file.

- Still in the Bot tab, activate all "Privileged Gateway Intents" be sure to save all the modifications.

- Your bot is now ready !

Now with your python env selected, you can run the main.py with the following command :

    > python main.py

After this your bot must be connected, you just need to connect a voice chanel an type in a discord text chanel : !play [Youtube URL]

If you encounter an unexpected error please report a detailed issue.
Enjoy your music !
