"""
This module provides a Flask web server
to handle emotion detection requests.

Endpoints:
- POST /emotion_detector: Analyzes the provided text
  and returns the emotion scores and dominant emotion.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotion_detector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint to receive a POST request containing text
    and return the emotion analysis.

    Request format:
    {
        "text": "string"
    }

    Response format:
    {
        "anger": float,
        "disgust": float,
        "fear": float,
        "joy": float,
        "sadness": float,
        "dominant_emotion": "string"
    }
    or
    {
        "message": "Invalid text! Please try again!"
    }
    """
    data = request.json
    text = data.get('text', '')

    result = emotion_detector(text)

    if result.get('dominant_emotion') is None:
        return jsonify({
            "message": "Invalid text! Please try again!"
        }), 400

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)  # Ensure ports are correctly set
