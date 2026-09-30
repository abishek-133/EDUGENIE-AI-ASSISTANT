import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# Load Gemini API Key from environment or hardcode as a fallback
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_KEY")
client = genai.Client(api_key=GEMINI_KEY) if GEMINI_KEY else None

SYSTEM_INSTRUCTION = (
    "You are EduGenie, an intelligent, empathetic, and clear AI tutor. "
    "Break down complex academic concepts step-by-step, use real-world analogies, "
    "and provide helpful, structured answers to students."
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    if not client:
        return jsonify({"error": "Gemini API key is not configured."}), 500

    data = request.get_json(silent=True) or {}
    user_query = data.get("message", "").strip()

    if not user_query:
        return jsonify({"response": "Please enter a question!"})

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_query,
            config={"system_instruction": SYSTEM_INSTRUCTION}
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"API Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
