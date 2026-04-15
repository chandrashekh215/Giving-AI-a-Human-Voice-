from flask import Flask, render_template, request
from emotion import detect_emotion
from tts_engine import generate_voice
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    emotion = None
    
    if request.method == "POST":
        text = request.form["text"]
        emotion, intensity = detect_emotion(text)
        audio_file = generate_voice(text, emotion, intensity)
    
    return render_template("index.html", audio_file=audio_file, emotion=emotion)

if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    app.run(debug=True)
