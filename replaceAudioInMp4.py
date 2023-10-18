from moviepy.editor import VideoFileClip, AudioFileClip

# Load the video file and the new audio file
video = VideoFileClip("input_video.mp4")
new_audio = AudioFileClip("new_audio.mp3")

# Replace the audio in the video file with the new audio
video = video.set_audio(new_audio)

# Write the video file with the replaced audio
video.write_videofile("output_video.mp4", codec='libx264', audio_codec='aac')

# Close the video and audio clips
video.close()
new_audio.close()
