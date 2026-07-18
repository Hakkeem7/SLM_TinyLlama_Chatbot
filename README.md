# SLM chatbot using tinylama
# 🤖 SLM TinyLlama Chatbot

A lightweight AI chatbot built using the TinyLlama Small Language Model (SLM) and Flask. The chatbot runs locally through Ollama and provides fast, interactive conversations without relying on cloud-based APIs.

---

## 📖 Overview

This project demonstrates how to build a local AI chatbot using TinyLlama, one of the smallest open-source language models. The chatbot features a clean web interface developed with Flask and communicates with the model through the Ollama API.

---

## ✨ Features

- 💬 Interactive AI chatbot
- 🦙 TinyLlama SLM integration
- ⚡ Fast local inference using Ollama
- 🌐 Flask web application
- 📝 Maintains chat history during the session
- 🔒 Fully offline after model installation

---

## 🛠️ Tech Stack

- Python
- Flask
- TinyLlama
- Ollama
- HTML5
- CSS3
- Requests Library

---

## 📂 Project Structure

```
SLM_TinyLlama_Chatbot/
│
├── templates/
│   └── ui.html
│
├── model1.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SLM_TinyLlama_Chatbot.git
```

### 2. Navigate to the Project

```bash
cd SLM_TinyLlama_Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Install TinyLlama

Install Ollama if it is not already installed.

Pull the TinyLlama model:

```bash
ollama pull tinyllama
```

Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run the Application

```bash
python model1.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 💻 How It Works

1. User enters a message in the web interface.
2. Flask receives the message.
3. The message is sent to the Ollama API.
4. TinyLlama generates a response.
5. Flask displays the response and stores the conversation history.

---

## 📸 Screenshot

Add a screenshot of your chatbot here.

Example:

```
images/chatbot.png
```

---

## 🚀 Future Enhancements

- Chat history database
- Multiple language support
- Voice input and output
- Dark mode
- RAG (Retrieval-Augmented Generation)
- PDF document chatbot
- User authentication

---

## 📋 Requirements

```
Python 3.10+
Flask
Requests
Ollama
TinyLlama
```

---

## 👨‍💻 Author

**Abdul**

- GitHub: https://github.com/yourusername
- LinkedIn: https://linkedin.com/in/yourprofile

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

- TinyLlama
- Ollama
- Flask
- Python Community
