from flask import Flask, request, render_template
from chatbot_model import get_chatbot_response

app = Flask(__name__)


def home():
    chatbot_response = None
    if request.method == "POST":
        user_input = request.form["user_input"]
       

if __name__ == "__main__":
    app.run(debug=True)


