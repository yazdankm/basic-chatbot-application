from flask import Flask, request, render_template
import openai

app = Flask(__name__)
openai.api_key = "OPENAI_API_KEY"

def get_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify your preferred model here
        messages=[{"role": "user", "content": question}],
    )
    return response['choices'][0]['message']['content']

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["question"]
        answer = get_response(question)
        return render_template("index.html", question=question, answer=answer)
    return render_template("index.html", question="", answer="")

if __name__ == "__main__":
    app.run(debug=True)