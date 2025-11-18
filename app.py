from flask import Flask, request, jsonify, render_template
from chatbot.rag import SmartRAG
from chatbot.config import load_config

app = Flask(__name__)
config = load_config()
rag = SmartRAG(config)

@app.route('/')
def index():
    return render_template('index.html')   # ← cette ligne doit être indentée !

@app.route('/api/chat', methods=['POST'])
def chat():
    payload = request.json
    question = payload.get('question')
    session_id = payload.get('session_id')
    if not question:
        return jsonify({'error': 'question required'}), 400

    response = rag.answer(question, session_id=session_id)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
