import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from utils import dl_audio, play_audio

# Load environment variables from .env file
load_dotenv()

# Initialize Discord client with command capabilities
intents = discord.Intents.all()
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load the bot token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

is_playing = False

# Event: Bot is ready
@bot.event
async def on_ready():
	print(f'Logged in as {bot.user}')

# Modify the 'play' function to check for queued URLs
@bot.command()
async def play(ctx, url: str):
	global is_playing

	voice_channel = ctx.author.voice.channel if ctx.author.voice else None

	if not voice_channel:
		await ctx.send("You're not in a voice channel. Please join a voice channel first.")
		return

	try:
		if ctx.voice_client is not None:
			ctx.voice_client.stop()

		is_playing = True
		success, file_name = await dl_audio(ctx, url)
		if success:
			if ctx.voice_client is None:
				voice_client = await voice_channel.connect()
			else:
				voice_client = ctx.voice_client

			await play_audio(ctx, voice_client, file_name)

		else:
			await ctx.send("Failed to download video :(")
	finally:
		is_playing = False

# Run the bot
bot.run(TOKEN)
