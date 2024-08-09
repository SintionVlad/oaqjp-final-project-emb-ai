from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.json
    text = data.get('text', '')

    result = emotion_detector(text)
    
    if result.get('dominant_emotion') is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
