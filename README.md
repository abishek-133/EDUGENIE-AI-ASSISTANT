# EDUGENIE - GOOGLE GEMINI POWERED LEARNING ASSISTANT

eduGenie Chatbot is an interactive, emotionally intelligent learning assistant, fine-tuned specifically for English language learners. Designed to be engaging and empathetic, eduGenie adapts to the user's mood and provides text, audio, and even an animated avatar to enhance the language learning experience.

## Overview

eduGenie combines state-of-the-art language and speech models with real-time animation to create a comprehensive, interactive learning tool. It detects user emotions, generates spoken responses, and presents a dynamic, lifelike avatar, creating a more engaging and supportive environment for language practice.

## Quick Start

Here’s how you can set up EduGenie Chatbot on your local machine:

## run this code on google colab 
import os
import glob

# 1. Clear previous clone and get the latest code from your repo
%cd /content
!rm -rf EDUGENIE-AI-ASSISTANT
!git clone https://github.com/abishek-133/EDUGENIE-AI-ASSISTANT.git

# 2. Automatically enter the folder where app.py is located
app_files = glob.glob("/content/EDUGENIE-AI-ASSISTANT/**/app.py", recursive=True)
if not app_files:
    raise FileNotFoundError("app.py could not be found!")

run_dir = os.path.dirname(app_files[0])
%cd {run_dir}
print(f"Running from: {run_dir}")

# 3. Install dependencies
!pip install --upgrade google-genai flask flask-cors --quiet
!npm install -g localtunnel --silent > /dev/null 2>&1

# 4. Display Localtunnel IP & Launch Server
print("\n" + "=" * 60)
print("YOUR LOCALTUNNEL PASSWORD (IP ADDRESS):")
!curl -s ipv4.icanhazip.com
print("=" * 60)
print("Click the URL below and submit the IP address above:\n")

!npx localtunnel --port 5000 & python app.py


---------------------------------------------------------------
## Steps to open and test:
step 1:Look at the output of the cell and copy the IP address (e.g., 34.120.x.x).

## Click the [https://...loca.lt](https://...loca.lt) link.

step 2:Paste the IP into the Endpoint IP field and click Submit.
---------------------------------------------------------------
## Dependencies

eduGenie Chatbot relies on several key libraries and models:
- **Transformers** for language and emotion models
- **MoviePy** for video processing
- **Flask** for creating a local web server
- **Google Gemini API** for text generation and response adaptation

eduGenie Chatbot is more than just a language learning tool; it's a responsive, engaging, and empathetic virtual assistant designed to make learning English interactive and enjoyable!
