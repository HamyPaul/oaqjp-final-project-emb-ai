"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)

    if dominant_emotion is None:
        return 'Invalid text! Please try again.'
    return 'This text has been identified as {}.'.format(dominant_emotion)#pylint: disable=consider-using-f-string
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
