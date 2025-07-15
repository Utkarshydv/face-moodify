from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
import cv2
import numpy as np
import base64
from youtube import get_songs_by_emotion

app = Flask(__name__)
CORS(app)

@app.route("/detect", methods=["POST"])
def detect():
    data = request.json
    img_data = base64.b64decode(data["image"].split(",")[1])
    frame = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)

    try:
        res = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)
        emo = res[0]["dominant_emotion"]
    except:
        emo = "neutral"

    songs_list = get_songs_by_emotion(emo)
    return jsonify({"emotion": emo, "songs": songs_list})

if __name__ == "__main__":
    app.run(debug=True)
