from flask import Flask, render_template, request

import requests

app = Flask(__name__)

# Stores chat history
messages = []

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "tinyllama"


@app.route("/", methods=["GET", "POST"])
def home():

    global messages

    if request.method == "POST":

        user_message = request.form.get("user")

        if user_message:

            # Save user message
            messages.append({
                "role": "user",
                "content": user_message
            })

            try:
                response = requests.post(
                    OLLAMA_URL,
                    json={
                        "model": MODEL,
                        "prompt": user_message,
                        "stream": False
                    },
                    timeout=60
                )

                response.raise_for_status()

                bot_reply = response.json().get(
                    "response",
                    "No response received."
                )

            except Exception as e:
                bot_reply = f"Error: {e}"

            # Save bot response
            messages.append({
                "role": "bot",
                "content": bot_reply
            })

    return render_template(
        "ui.html",
        messages=messages
    )


@app.route("/clear")
def clear():

    global messages
    messages = []

    return render_template(
        "ui.html",
        messages=messages
    )


if __name__ == "__main__":
    app.run(debug=True)