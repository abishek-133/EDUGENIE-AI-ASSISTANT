

eduGenie Chatbot is an interactive, emotionally intelligent learning assistant, fine-tuned specifically for English language learners. Designed to be engaging and empathetic, eduGenie adapts to the user's mood and provides text, audio, and even an animated avatar to enhance the language learning experience.

## Overview

eduGenie combines state-of-the-art language and speech models with real-time animation to create a comprehensive, interactive learning tool. It detects user emotions, generates spoken responses, and presents a dynamic, lifelike avatar, creating a more engaging and supportive environment for language practice.



## Quick Start

Here’s how you can set up EduGenie Chatbot on your local machine:

### Step 1: Clone the Repository

```bash
git clone https://github.com/mtgsoftworks/eduGenie.git
cd eduGenie
```

### Step 2: Install Dependencies

- Set up a virtual environment and install required packages:
  ```bash
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
  ```

 
- Install the Desktop development with C++ module and install the CMake software build automation program. (Don't forget to set the environmental variables path for CCmake)  
  

### Step 3: Configure the Models

- Download models for emotion detection, text-to-speech, and vocoder:
  - Emotion Detection: `t5-base-finetuned-emotion`
  - TTS: `speecht5_tts` and `speecht5_hifigan`


1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Access the Chat Interface**:
   - Open your browser and navigate to `http://localhost:5000`.

3. **Start Chatting with EduGenie**:
   - Enter questions or statements in the chat box, and EduGenie will respond with text and an animated video!

## Warning
- You need to install Python version 3.9.13 for the project. Using the wrong version may cause incompatibility problems between the libraries used!

eduGenie Chatbot is more than just a language learning tool; it's a responsive, engaging, and empathetic virtual assistant designed to make learning English interactive and enjoyable!
