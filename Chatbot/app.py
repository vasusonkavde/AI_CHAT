from flask import Flask, render_template, request
from bardapi import Bard
import os

os.environ['_BARD_API_KEY'] = "dAif_u6-oYIAOJrU8pJfczUOTwrYkJkMC-Ukyo7xdYUJj6KsBAOyGv-9rNwKS79YGMNUSg."

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html', answer="How can I help you today?")

@app.route('/get_answer', methods=['POST'])
def get_answer():
    user_input = request.form['inpt']
    answer_content = Bard().get_answer(user_input)['content']
    return render_template('index.html', answer=answer_content, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)