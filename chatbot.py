import json
import re
from pathlib import Path


def load_knowledge_base(file_path):
	"""Load the chatbot knowledge base from JSON."""
	try:
		with open(file_path, "r", encoding="utf-8") as file:
			return json.load(file)
	except FileNotFoundError:
		print("Error: knowledge.json was not found.")
		return {"intents": []}
	except json.JSONDecodeError:
		print("Error: knowledge.json contains invalid JSON.")
		return {"intents": []}


def get_response(user_input, knowledge_base):
	"""Find a matching response for the user's message."""
	message = re.sub(r"[^a-z0-9\s]", "", user_input.lower()).strip()
	best_response = None
	best_score = -1

	for intent in knowledge_base.get("intents", []):
		for keyword in intent.get("keywords", []):
			clean_keyword = re.sub(r"[^a-z0-9\s]", "", keyword.lower()).strip()
			if clean_keyword in message:
				score = len(clean_keyword)
				if score > best_score:
					best_score = score
					best_response = intent.get("response", "")

	if best_response:
		return best_response

	return "I am sorry, I do not know that yet. Try asking about you, your project, or the chatbot knowledge."


def main():
	knowledge_path = Path(__file__).with_name("knowledge.json")
	knowledge_base = load_knowledge_base(knowledge_path)

	print("KnowBot is ready. Type 'exit' to quit.\n")

	while True:
		user_input = input("You: ")

		if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
			print("KnowBot: Goodbye! Have a great day!\n")
			break

		response = get_response(user_input, knowledge_base)
		print(f"KnowBot: {response}\n")


if __name__ == "__main__":
	main()
