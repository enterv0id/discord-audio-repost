import discord
import os
from moviepy.editor import *
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})

# Initialize the Discord client
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    # Check if the message is from the specific guild you want to monitor
    if message.guild.id == YOUR_GUILD_ID:
        # Check if the message has attachments
        if message.attachments:
            for attachment in message.attachments:
                filename, ext = os.path.splitext(attachment.filename)
                if ext.lower() in ['.wav', '.mp3', '.m4a', '.flac']:
                    # Create a temporary folder next to the Python file
                    temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp')
                    os.makedirs(temp_folder, exist_ok=True)

                    # Download the audio file locally to the temporary folder
                    temp_audio_path = os.path.join(temp_folder, filename)
                    await attachment.save(temp_audio_path)

                    # Convert the audio file to a video file
                    video_filename = f'{filename}.mp4'
                    audio = AudioFileClip(temp_audio_path)
                    background = ImageClip('background.jpg').set_duration(audio.duration)
                    video = CompositeVideoClip([background.set_audio(audio)])

                    # Set the frame rate (fps) of the video clip
                    video.fps = 4

                    # Calculate the length of the file title
                    title_length = len(filename)
                    # Adjust the text size based on the length of the file title
                    if title_length <= 10:
                        fontsize = 40
                    elif title_length <= 20:
                        fontsize = 30
                    else:
                        fontsize = 20

                    # Add the filename as text overlay on the video with adjusted text size
                    text = TextClip(filename, fontsize=fontsize, color='white', font='Arial', method='caption')
                    text = text.set_position(('center', 'bottom')).set_duration(video.duration)
                    video = CompositeVideoClip([video, text])

                    video.write_videofile(video_filename, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)

                    # Reply with the converted video file
                    await message.reply(file=discord.File(video_filename))

                    # Delete the original and converted files locally
                    os.remove(temp_audio_path)
                    os.remove(video_filename)

                    # Remove the temporary folder
                    os.rmdir(temp_folder)

# Replace YOUR_GUILD_ID with the ID of the guild you want to monitor
YOUR_GUILD_ID = add-your-guild-id-here

# Replace YOUR_BOT_TOKEN with your Discord bot token
client.run('place-your-token-here')
