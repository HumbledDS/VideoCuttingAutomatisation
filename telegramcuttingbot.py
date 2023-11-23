from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

from logger import logging

# Replace 'YOUR_BOT_TOKEN' with the actual API token you obtained from the BotFather
TOKEN = '6647424882:AAH0lBo8-vbd0-NzWY7Qwy3-SzDAFRgudBg'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Send me a YouTube video link, and I'll download and send it back to you.")
    print("Received /start command")

async def download_and_send_video(update: Update, context: CallbackContext) -> None:
    # Get the message text
    video_url = update.message.text

    try:
        print(f"Received video URL: {video_url}")

        # Create a YouTube object
        yt = YouTube(video_url)

        print(f"Download started for video: {yt.title}")

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        video_path = f"{yt.title}.mp4"
        video_stream.download()

        print(f"Video downloaded successfully: {video_path}")

        # Cut the video into 3-minute segments
        cut_video_into_segments(video_path, yt.title)

        # Send the segments back to the chat
        for i in range(1, 100):  # Assuming a maximum of 100 segments
            segment_path = f"{yt.title}_segment_{i}.mp4"
            try:
                with open(segment_path, 'rb') as video_file:
                    update.message.reply_video(video_file.read())
                    logging.info(f"Segment {i} sent successfully")
            except FileNotFoundError:
                break

    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")
        print(f"Error: {str(e)}")

def cut_video_into_segments(video_path, video_title):
    clip = VideoFileClip(video_path)

    total_duration = clip.duration
    segment_duration = 3 * 60  # 3 minutes in seconds

    segment_start = 0
    segment_end = segment_duration
    segment_number = 1

    while segment_start < total_duration:
        if segment_end > total_duration:
            segment_end = total_duration

        segment = clip.subclip(segment_start, segment_end)

        # Save the segment
        segment_path = f"{video_title}_segment_{segment_number}.mp4"
        segment.write_videofile(segment_path, codec="libx264", audio_codec="aac")

        print(f"Segment {segment_number} created: {segment_path}")

        segment_start = segment_end
        segment_end += segment_duration
        segment_number += 1

    clip.close()

def main():
    # Create the Updater and pass it your bot's token
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))

    # Register a message handler (download, cut, and send video segments)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_and_send_video))

    print("Bot started. Listening for commands...")

    # Start the Bot
    app.run_polling(poll_interval=3)

    # Run the bot until you send a signal to stop
    # app.idle()

if __name__ == '__main__':
    main()
