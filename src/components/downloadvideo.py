from pytube import YouTube

def download_youtube_video(url, output_path="."):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path)
        print("Download complete!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter the YouTube video URL: ")
    output_folder_path = r"C:\Users\HP\Desktop\Babs_1v9_Journey\VideoCuttingAutomatisation\output_Videos"

    download_youtube_video(video_url, output_folder_path)
