# Import libraries

from flask import Flask, redirect, request, render_template, url_for
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask f

app = Flask(__name__)

# Read operation: List all transactions
@app.route("/")
def get_main():
    return render_template("index.html", title="Emotion Detector")
    
@app.route("/emotionDetector/<string:text>")
def get_emotions(text):
    return emotion_detector(text)

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)