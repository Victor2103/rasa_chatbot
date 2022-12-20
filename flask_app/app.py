from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("chatbot.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')