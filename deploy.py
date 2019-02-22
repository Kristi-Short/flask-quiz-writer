from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Deployed to Heroku!</h1>'


@app.route('/api')
def api():
    quiz = [{"type": "fillin", "question": "______ was the 44th president of the United States.",
             "answer": "Barak Obama"},
             {"type": "multichoice", "question": "The 44th President of the United States", 
             "options":["Bill Clinton", "Jimmy Carter", "George Bush", "Barak Obama"],
             "answer": "Barak Obama"}]
    return jsonify(quiz)
