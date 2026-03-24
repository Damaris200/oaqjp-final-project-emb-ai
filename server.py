
"""Flask web application for Emotion Detection using Watson NLP.

This module provides a simple web interface to detect emotions
in text using the Watson NLP library via the EmotionDetection package.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze emotion from text received via the web form.

    This is the main endpoint called by the frontend when the user submits text.
    It handles valid input as well as empty/invalid text cases.

    Returns:
        str: Formatted emotion response or error message.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse or text_to_analyse.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyse)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_output


if __name__ == "__main__":
    """Run the Flask development server on port 5000."""
    app.run(host='0.0.0.0', port=5000)
