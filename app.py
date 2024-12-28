from flask import Flask, request, jsonify, render_template
from pydub import AudioSegment
import os

app = Flask(__name__)
SOURCE_DIR = "source"
OUTPUT_FILE = "output.wav"
OUTPUT_DIR = "static"

os.makedirs(OUTPUT_DIR, exist_ok=True)  # 出力ディレクトリを確実に作成

@app.route('/')
def index():
    return render_template('index.html')  # HTMLファイルを読み込む

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "テキストが入力されていません"}), 400

    audio_segments = []
    for char in text:
        char_file = os.path.join(SOURCE_DIR, f"{char}.wav")
        if os.path.exists(char_file):
            audio_segments.append(AudioSegment.from_file(char_file))
        else:
            return jsonify({"error": f"音声ファイルが見つかりません: {char}"}), 404

    if audio_segments:
        combined = sum(audio_segments)
        output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        combined.export(output_path, format="wav")
        return jsonify({"audio_url": f"/static/{OUTPUT_FILE}"})

    return jsonify({"error": "音声の生成に失敗しました"}), 500

if __name__ == '__main__':
    app.run(debug=True)
