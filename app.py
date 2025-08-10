from flask import Flask, render_template, request

app = Flask(__name__)

# Bot logic
responses = {
    "hi": "Hello! How can I assist you?",
    "hello": "Hi there! Ask me anything.",
    "what is codealpha": "CodeAlpha is a cloud internship program.",
    "how to submit project": "Submit using the WhatsApp form shared by CodeAlpha.",
    "bye": "Goodbye! Best of luck with your tasks.",
    "hi": "Hello!",
    "how to submit": "Use the WhatsApp form shared by CodeAlpha.",
    "project deadline": "Check your WhatsApp group for the deadline."
    
}



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_msg = request.args.get("msg").lower()
    return responses.get(user_msg, "Sorry, I didn't understand that.")

if __name__ == "__main__":
    app.run(debug=True)
