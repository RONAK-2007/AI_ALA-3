from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # ✅ Correct file name

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # Simple chatbot logic
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        response = "Hello! How are you?"
    elif "how are you" in user_input.lower():
        response = "I'm doing great, thanks for asking! How about you?"
    elif "your name" in user_input.lower():
        response = "I'm a simple chatbot made with Python."
    elif user_input.lower() == "2+2":
        response = f"The answer is {2+2}"
    elif "bye" in user_input.lower():
        response = "Goodbye! Have a nice day 😊"
    else:
        response = f"Sorry, I don't understand '{user_input}' yet."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
