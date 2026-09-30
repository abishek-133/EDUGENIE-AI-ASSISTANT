import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# Free Groq key
GROQ_KEY = os.environ.get("GROQ_API_KEY", "gsk_PASTE_YOUR_GROQ_KEY_HERE")
client = Groq(api_key=GROQ_KEY)

SYSTEM_INSTRUCTION = (
    "You are EduGenie, an intelligent, empathetic, and clear AI tutor. "
    "Break down complex academic concepts step-by-step, use real-world analogies, "
    "and provide structured, accurate educational responses."
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_query = data.get("message", "").strip()

    if not user_query:
        return jsonify({"response": "Please enter a question!"})

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_INSTRUCTION},
                {"role": "user", "content": user_query}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
