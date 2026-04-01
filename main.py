from trending import get_trending
from script import generate_script
from voice import create_voice
from video import create_video
from upload import upload_video

topic = get_trending()
print("Topic:", topic)

script = generate_script(topic)
print("Script generated")

create_voice(script)
print("Voice created")

create_video()
print("Video created")

upload_video(topic, script)
print("Uploaded successfully")
