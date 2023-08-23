from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def generate():
    """Generates and returns input form from prompts"""
    return render_template('questions.html', prompts = silly_story.prompts)