from gtts import gTTS

def create_voice(script):
    tts = gTTS(script)
    tts.save("voice.mp3")
