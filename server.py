"""Serve an emotion detection web interface with Flask."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector


app = Flask(__name__)
INVALID_TEXT_MESSAGE = "Invalid Respuesta de texto! Please try again!"


@app.route("/")
def render_index_page():
    """Display the web interface for emotion detection."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Return emotion scores and the dominant emotion for submitted text."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return INVALID_TEXT_MESSAGE

    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return INVALID_TEXT_MESSAGE

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
