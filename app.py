from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]

    response = requests.post(
        "http://127.0.0.1:11434/api/chat",
        json={
            "model": "llama3.2",
            "messages": [
                {"role": "user", "content": message}
            ],
            "stream": False
        }
    )

    data = response.json()
    return jsonify({"reply": data["message"]["content"]})

app.run(host="0.0.0.0", port=5000)