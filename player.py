import os
import random
import time
from subprocess import PIPE, Popen, STDOUT

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []

def getVideos():
    global videos
    videos = []
    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            videos.append(os.path.join(directory, file))

def playVideos():
    global videos
    if len(videos) == 0:
        getVideos()
        time.sleep(5)
        return
    
    # This is exactly the same shuffling logic as the original
    random.shuffle(videos)
    # Then we play each video in the shuffled order
    for video in videos:
        # VLC command line arguments:
        # --fullscreen: Play video in fullscreen
        # --no-osd: No on-screen display
        # --aspect-ratio=fill: Full screen
        # --no-repeat: Don't repeat the video
        playProcess = Popen([
            'cvlc',  # Use cvlc instead of vlc to run without GUI
            '--fullscreen',
            '--no-osd',
            '--aspect-ratio=fill',
            '--no-repeat',
            video
        ])
        playProcess.wait()
        # Wait for the current video to finish before playing the next one
        # This ensures videos play in the shuffled order we specified

def main():
    while True:
        playVideos()

if __name__ == "__main__":
    main()