from pathlib import Path

from flask import Flask, jsonify, render_template, request

from chatbot import get_response, load_knowledge_base


app = Flask(__name__)
knowledge_path = Path(__file__).with_name("knowledge.json")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()
    knowledge_base = load_knowledge_base(knowledge_path)

    if not user_message:
        return jsonify({"response": "Please type a message."})

    if user_message.lower() in ["bye", "goodbye", "exit"]:
        return jsonify({"response": "Goodbye! Have a great day!", "exit": True})

    response = get_response(user_message, knowledge_base)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)