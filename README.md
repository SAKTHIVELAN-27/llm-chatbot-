# Know About Sakthivelan

This is a small Flask-based chatbot that answers questions about Sakthivelan using a local knowledge base. It runs on your machine and responds from the data stored in `knowledge.json`.

## What it can do

- Answer questions about Sakthivelan's background
- Share details about skills, education, and projects
- Tell you about certificates, achievements, and roles
- Provide contact information

## Project files

- `app.py` starts the Flask web app and exposes the chat endpoint
- `chatbot.py` matches user messages against the knowledge base
- `knowledge.json` stores the questions and answers the bot knows
- `templates/index.html` contains the chat interface

## How to run it

1. Install Flask if you do not already have it:

   ```bash
   pip install flask
   ```

2. Start the app:

   ```bash
   python app.py
   ```

3. Open the local address shown in the terminal, usually `http://127.0.0.1:5000/`.

## Example questions

- Who is Sakthivelan?
- What are his skills?
- Tell me about his projects.
- What certificates does he have?
- How can I contact him?

## Notes

The bot is keyword based, so it works best when you ask using simple phrases related to the topics listed above.