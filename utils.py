import os
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

# Function to sanitize the file name
def sanitize_filename(filename):
	invalid_chars = '\\/:*?"<>|'
	valid_filename = ''.join(char if char not in invalid_chars else '_' for char in filename)
	return valid_filename.strip()  # Strip leading and trailing spaces

# Function to download audio from YouTube
async def dl_audio(ctx, url):
	if not url:import os
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

# Function to sanitize the file name
def sanitize_filename(filename):
	invalid_chars = '\\/:*?"<>|'
	valid_filename = ''.join(char if char not in invalid_chars else '_' for char in filename)
	return valid_filename.strip()  # Strip leading and trailing spaces

# Function to download audio from YouTube
async def dl_audio(ctx, url):
	if not url:
		await ctx.send("Please enter a YouTube URL")
		return False, None

	try:
		# Create options for audio download
		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}

		# Create the YoutubeDL object with the specified options
		ydl = YoutubeDL(ydl_opts)

		# Extract video information to get the title
		info = ydl.extract_info(url, download=False)
		video_title = info.get('title', 'video')  # Get the title or set a default name

		# Sanitize the title to remove invalid characters
		sanitized_title = sanitize_filename(video_title)

		# Construct the output file name with the sanitized title
		output_file_name = f"{sanitized_title}.mp3"

		# Set the output file name template
		ydl_opts['outtmpl'] = output_file_name

		# Download the file with the constructed output file name
		ydl = YoutubeDL(ydl_opts)
		ydl.download([url])

		# Check if the file was downloaded successfully
		if os.path.exists(output_file_name):
			return True, output_file_name
		else:
			return False, None

	except Exception as e:
		print(f"An error occurred: {e}")
		return False, None
		

# Function to play audio in the voice channel
async def play_audio(ctx, voice_channel, file_name, next_url=None):
	# Construct the full file path
	file_path = os.path.join(os.getcwd(), file_name)

	try:
		# Check if the bot is already in a voice channel
		voice_state = ctx.voice_client
		if voice_state and voice_state.is_connected():
			# Create a PCMVolumeTransformer to play the audio
			audio_source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file_path))

			# Play the audio
			file_name_without_extension = os.path.splitext(file_name)[0]
			await ctx.send(f"Playing : {file_name_without_extension}")
			voice_state.play(audio_source, after=lambda e: print(f"Finished playing: {file_name_without_extension}"))

			# Remove the file after playing
			os.remove(file_path)

			# Fetch and play the next video if available
			if next_url:
				success, next_file_name = await dl_audio(ctx, next_url)
				if success:
					await play_audio(ctx, voice_channel, next_file_name)
				else:
					await ctx.send("Failed to download the next video :(")
		else:
			print("Bot is not in a voice channel.")
	except Exception as e:
		print(f"Error playing audio: {e}")
