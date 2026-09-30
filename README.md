# EDUGENIE - GOOGLE GEMINI POWERED LEARNING ASSISTANT

#  EduGenie AI Assistant

EduGenie is a lightweight, responsive, and modern AI-powered learning assistant designed to help students master complex concepts across computer science, mathematics, and engineering. Built on a clean Flask backend and powered by the Google Gemini API, EduGenie delivers structured, step-by-step explanations, analogies, and practice problems in real time.

---

##  Features

- **Gemini-Powered Intelligence:** Powered by high-efficiency models (`gemini-3.8-flash` / `gemini-3.5-flash`) for low-latency tutoring.
- **Auto-Failover & Retry:** Automatic fallback to backup models if a server experiences temporary demand spikes (503 handling).
- **Modern Responsive UI:** Polished, centered dark-mode chat interface with glassmorphism, responsive message cards, and avatar tags.
- **Markdown & Code Rendering:** Built-in support for formatted lists, bold definitions, and formatted code blocks via `marked.js`.
- **Zero Heavy Bloat:** Clean architecture without bulky PyTorch weights or outdated avatar dependencies—runs instantly on modern Python environments (including Python 3.11+).

---
## Running on Google Colab
Open a new or existing notebook in Google Colab.

Clone the repository and navigate into the project directory:

Python
!git clone https://github.com/abishek-133/EDUGENIE-AI-ASSISTANT.git
%cd EDUGENIE-AI-ASSISTANT
Install the required lightweight dependencies:

Python
!pip install -r requirements.txt --quiet
!npm install -g localtunnel --silent > /dev/null 2>&1
Set your Google Gemini API key as an environment variable:

Python
import os
os.environ["GEMINI_API_KEY"] = "YOUR_GEMINI_API_KEY"
Launch the Flask server and start localtunnel:

Python
print("Your tunnel password (IP):")
!curl -s ipv4.icanhazip.com
print("\nClick the loca.lt link below and enter the IP address above:\n")
!npx localtunnel --port 5000 & python app.py
Click the generated .loca.lt link, enter your public IP address into the endpoint verification page, and begin using EduGenie.

## Project Structure

```text
EDUGENIE-AI-ASSISTANT/
├── app.py              # Flask server, route handling & Gemini integration
├── requirements.txt    # Project dependencies
├── templates/
│   └── index.html      # Modern chat interface
└── README.md           # Project documentation
```
---

eduGenie Chatbot is more than just a language learning tool; it's a responsive, engaging, and empathetic virtual assistant designed to make learning English interactive and enjoyable!

## License
This project is open-source and available under the MIT License.
