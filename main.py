from flask import Flask, request, jsonify, send_file
from gtts import gTTS
from responses import get_response
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Voice Bot Server is Running!'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("text", "")

    response_text = get_response(user_input)

    # Generate audio file
    tts = gTTS(response_text, lang='id')
    audio_path = "response.mp3"
    tts.save(audio_path)

    return jsonify({
        "response": response_text,
        "audio_url": request.host_url + "audio"
    })

@app.route('/audio')
def audio():
    return send_file("response.mp3", mimetype="audio/mpeg")

# Hapus baris ini karena gunicorn yang akan menjalankan app:
# if __name__ == '__main__':
#     app.run()
