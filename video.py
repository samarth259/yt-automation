import os

def create_video():
    os.system("""
    ffmpeg -loop 1 -i assets/bg.jpg -i voice.mp3 \
    -c:v libx264 -t 30 -pix_fmt yuv420p \
    -vf scale=1080:1920 output.mp4
    """)
