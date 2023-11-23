from moviepy.video.io.VideoFileClip import VideoFileClip

def cut_video(input_video, output_folder, segment_duration=3):
    clip = VideoFileClip(input_video)

    total_duration = clip.duration
    segment_start = 0
    segment_end = segment_duration * 60  # Convert minutes to seconds

    segment_number = 1

    while segment_start < total_duration:
        if segment_end > total_duration:
            segment_end = total_duration

        segment = clip.subclip(segment_start, segment_end)

        # Save the segment
        output_path = f"{output_folder}/segment_{segment_number}.mp4"
        segment.write_videofile(output_path, codec="libx264", audio_codec="aac")

        segment_start = segment_end
        segment_end += segment_duration * 60
        segment_number += 1

    clip.close()

if __name__ == "__main__":
    input_video_path = r"C:\Users\HP\Desktop\Babs_1v9_Journey\VideoCuttingAutomatisation\output_Videos\7 Steps To UnFuk Your Life.mp4"
    
    output_folder_path = r"C:\Users\HP\Desktop\Babs_1v9_Journey\VideoCuttingAutomatisation\output_Videos"

    cut_video(input_video_path, output_folder_path)
