# Know About Sakthivelan

Know About Sakthivelan is a simple Flask chatbot project built to answer questions about Sakthivelan from a local knowledge base. It is meant to act like a personal portfolio assistant, where visitors can ask about education, skills, projects, achievements, and contact details in a quick and easy way.

The bot does not depend on any external API. Instead, it reads predefined question and answer pairs from `knowledge.json` and returns the closest matching response based on the words in your message. That makes the project lightweight, fast, and easy to customize.

## What this repo is for

This repository is useful if you want a small chatbot-style portfolio assistant, a beginner-friendly Flask project, or a simple example of keyword-based chat handling. It is also easy to extend by adding more intents and responses inside the knowledge file.

## How it works

- The browser UI sends your message to the Flask server
- `chatbot.py` checks the message against keywords stored in `knowledge.json`
- The best matching response is returned to the front end
- The chat interface shows the answer inside the page without reloading

## Main files

- `app.py` starts the Flask app and exposes the `/chat` endpoint
- `chatbot.py` handles message matching and response selection
- `knowledge.json` contains the bot's knowledge base
- `templates/index.html` contains the user interface

## How to open and run this repo

1. Open the folder in VS Code or any code editor.
2. Make sure Python is installed on your system.
3. Open the terminal inside the project folder.
4. Install Flask if it is not already installed:

   ```bash
   pip install flask
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open the local address shown in the terminal, usually `http://127.0.0.1:5000/`.

If you are using VS Code, you can also right-click the folder and choose Open in Integrated Terminal before running the command above.

## Example questions

- Who is Sakthivelan?
- What are his skills?
- Tell me about his projects.
- What certificates does he have?
- How can I contact him?

## Customization

If you want to add more answers, just open `knowledge.json` and add new keywords and responses. You can also update the UI text in `templates/index.html` to match your own portfolio style.

## Notes

This chatbot works best with simple, direct questions. Since it uses keyword matching, the clearer your question is, the easier it is for the bot to return the right response.