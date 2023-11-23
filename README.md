# Telegram Video Cutter Bot

This script creates a Telegram bot using the `python-telegram-bot` library and the `pytube` library to interact with YouTube. The bot allows users to send a YouTube video link, and it responds by downloading the video, cutting it into 3-minute segments, and sending each segment back to the user on Telegram.

## Components and Functionality

### 1. Imports
- `Update` and `CallbackContext` classes from the `python-telegram-bot` library handle updates and context in asynchronous functions.
- `Application` class from the `python-telegram-bot` library is used for building a bot application.
- `YouTube` class from the `pytube` library interacts with YouTube videos.
- `VideoFileClip` class from the `moviepy` library is used to work with video files.

### 2. Token and Bot Initialization
- The script starts by defining the Telegram bot token obtained from the BotFather.
- An `Application` instance is created with this token.

### 3. Command Handlers
- A command handler (`start`) is registered to respond to the "/start" command. When users send this command, the bot replies with a welcome message and prints a message indicating the reception of the command.

### 4. Message Handler
- A message handler is registered to respond to text messages that are not commands.
- The `download_and_send_video` function is called when the bot receives a YouTube video link. This function:
  - Downloads the video using `pytube`.
  - Cuts the video into 3-minute segments using `moviepy`.
  - Sends each segment back to the user on Telegram.

### 5. Segment Creation
- The `cut_video_into_segments` function takes the downloaded video path and its title as arguments.
- It uses `moviepy` to open the video, calculate its total duration, and cut it into 3-minute segments.
- Each segment is saved with a filename indicating its order.

### 6. Main Function
- The `main` function initializes the bot, registers command and message handlers, and starts polling for updates.
- A welcome message is printed, indicating that the bot has started and is listening for commands.

### 7. Execution
- The `main` function is called if the script is executed.

In summary, this script creates a Telegram bot that provides a simple service of downloading YouTube videos, cutting them into segments, and sending the segments back to users. The bot continuously polls for new messages and commands.