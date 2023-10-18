from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_mp3("input.mp3")

# Set the start and end times in milliseconds
start_time = 27000  # 27 seconds * 1000
end_time = 37000  # 37 seconds * 1000

# Extract the desired segment
extracted_segment = audio[start_time:end_time]

# Export the extracted segment to a new file
extracted_segment.export("output_file.mp3", format="mp3")
