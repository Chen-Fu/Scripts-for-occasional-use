import os
import time
import concurrent.futures
from pytube import YouTube

def download_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Downloading {stream.title}... {percentage:.2f}% complete", end='\r')

def download_youtube_video(url, output_directory="."):
    try:
        # Create a YouTube object
        yt = YouTube(url, on_progress_callback=download_progress)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading {stream.title}...")
        stream.download(output_path=output_directory)
        print(f"{stream.title} download completed!")

    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def download_videos(video_urls, output_directory=".", max_simultaneous_downloads=3):
    os.chdir(output_directory)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_simultaneous_downloads) as executor:
        # Submit download tasks to the thread pool
        futures = [executor.submit(download_youtube_video, url) for url in video_urls]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)


# Input the YouTube video URLs
video_urls = [
r'https://www.youtube.com/watch?v=T1RBqTTM0qM&ab_channel=HCKWrestling',

]

download_videos(video_urls, max_simultaneous_downloads=3)


# Pending, need to test
r"""

import os
import time
import concurrent.futures
from pytube import YouTube

def download_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    status_message = f"Downloading {stream.title}... {percentage:.2f}% complete"

    # Print the status message alternately every 3 seconds
    if download_progress.last_message_time is None or time.time() - download_progress.last_message_time >= 3:
        print(status_message, end='\r')
        download_progress.last_message_time = time.time()

download_progress.last_message_time = None

def download_youtube_video(url, output_directory="."):
    try:
        # Create a YouTube object
        yt = YouTube(url, on_progress_callback=download_progress)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading {stream.title}...")
        stream.download(output_path=output_directory)
        print(f"{stream.title} download completed!")

    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def download_videos(video_urls, output_directory=".", max_simultaneous_downloads=3):
    os.chdir(output_directory)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_simultaneous_downloads) as executor:
        # Submit download tasks to the thread pool
        futures = [executor.submit(download_youtube_video, url) for url in video_urls]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

# Input the YouTube video URLs
video_urls = [
    r'https://www.youtube.com/watch?v=fYo3LN9Vf_M&ab_channel=TechTrain',
]
download_videos(video_urls, max_simultaneous_downloads=3)

"""
