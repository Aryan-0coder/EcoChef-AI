from flask import Flask, render_template, request
from rag import get_answer

app = Flask(__name__)

# Store chat history
chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():

    global chat_history

    if request.method == "POST":

        if "clear" in request.form:
            chat_history = []

        else:
            question = request.form["question"]

            answer, sources = get_answer(question)

            chat_history.append({
                "question": question,
                "answer": answer
            })

    return render_template(
        "index.html",
        chat_history=chat_history
    )

if __name__ == "__main__":
    app.run(debug=True)