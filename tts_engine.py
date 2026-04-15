from gtts import gTTS

def generate_voice(text, emotion, intensity):
    # Modify speech style based on emotion
    if emotion == "happy":
        text = "😊 " + text
        slow = False
    elif emotion == "frustrated":
        text = "😞 " + text
        slow = True
    else:
        slow = False
    
    # Intensity scaling (just simple emphasis)
    if intensity > 0.8:
        text = text.upper()
    
    tts = gTTS(text=text, lang='en', slow=slow)
    output_file = "static/output.mp3"
    tts.save(output_file)
    return output_file
