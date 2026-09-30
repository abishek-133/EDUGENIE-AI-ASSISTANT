import os
import glob

# 1. Enter the project folder
app_file = glob.glob("/content/EDUGENIE-AI-ASSISTANT/**/app.py", recursive=True)[0]
project_dir = os.path.dirname(app_file)
os.chdir(project_dir)
print(f"Working in: {project_dir}")

# 2. Put your fresh Google Gemini API key here:
GEMINI_KEY = "AQ.Ab8RN6LpzDqN6OVekFDMKNown70bXmsshdU01c4MNTC3veQavA".strip()

# 3. Update requirements.txt to pure Google GenAI
with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write("flask\nflask-cors\ngoogle-genai\n")

!pip install -r requirements.txt --quiet
!npm install -g localtunnel --silent > /dev/null 2>&1

# 4. Write app.py with robust multi-model Gemini fallback
app_code = f'''import os
import time
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key="{GEMINI_KEY}")

# Fallback sequence across active Gemini 3 endpoints:
# Lite models have massive capacity and almost never 503.
GEMINI_MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.7-flash",
    "gemini-3.8-flash"
]

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
    data = request.get_json(silent=True) or {{}}
    user_query = data.get("message", "").strip()

    if not user_query:
        return jsonify({{"response": "Please enter a question!"}})

    last_error = None

    # Try each active Gemini model in order with short retry
    for model_name in GEMINI_MODELS:
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=user_query,
                    config={{"system_instruction": SYSTEM_INSTRUCTION}}
                )
                if response and response.text:
                    return jsonify({{"response": response.text}})
            except Exception as e:
                last_error = e
                # Pause half a second before retrying / hopping to the next endpoint
                time.sleep(0.5)

    return jsonify({{"response": f"Gemini servers are momentarily busy. Please try again. (Details: {{str(last_error)}})"}}), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
'''

with open("app.py", "w", encoding="utf-8") as f:
    f.write(app_code)

print("app.py successfully configured with resilient Gemini failover!")

# 5. Show Tunnel Password & Launch Server
print("\n" + "=" * 60)
print("YOUR LOCALTUNNEL PASSWORD (IP ADDRESS):")
!curl -s ipv4.icanhazip.com
print("=" * 60)
print("Click the link below and submit the IP address above:\n")

!npx localtunnel --port 5000 & python app.py
