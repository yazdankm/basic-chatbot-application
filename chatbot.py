import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(question):
    response = openai.Completion.create(
        engine="davinci-codex",  # Or use another suitable engine
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    while True:
        question = input("You: ")
        if question.lower() == "quit":
            break
        answer = get_response(question)
        print(f"Chatbot: {answer}")
