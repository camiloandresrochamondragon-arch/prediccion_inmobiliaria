from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/objetivos')
def objetivos():
    return render_template('objetivos.html')

@app.route('/idea')
def idea():
    return render_template('idea.html')

@app.route('/uso')
def uso():
    return render_template('uso.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
