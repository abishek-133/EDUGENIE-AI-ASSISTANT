import os
import time
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# Use your working key directly (or from environment variable if set)
API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6I3DlxR7SB3JL8BeBexR61Pj0A8gCfUbH4UFQ5F7ic6vg")
client = genai.Client(api_key=API_KEY)

# Fallback models in priority order
CANDIDATE_MODELS = [
    "gemini-3.8-flash",
    "gemini-3.5-flash",
    "gemini-3-flash-preview"
]

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
        return jsonify({"response": "Gemini API key is not configured."}), 500

    data = request.get_json(silent=True) or {}
    user_query = data.get("message", "").strip()

    if not user_query:
        return jsonify({"response": "Please enter a question!"})

    last_error = None

    # Try models in priority order; gracefully retry if Google's servers report a 503 high demand spike
    for model_name in CANDIDATE_MODELS:
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=user_query,
                    config={"system_instruction": SYSTEM_INSTRUCTION}
                )
                if response and response.text:
                    return jsonify({"response": response.text})
            except Exception as e:
                last_error = e
                time.sleep(1)

    return jsonify({"response": f"Service temporarily busy. Details: {str(last_error)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
