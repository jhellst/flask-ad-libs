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


@app.get('/results')
def display_story():
    """Takes input from form and displays story"""

    # breakpoint() # Pauses code, like debugger

    # responses = {}
    # for prompt in silly_story.prompts:
    #     responses[prompt] = request.args[prompt]

    ad_lib_template = silly_story.get_result_text(request.args) # We can pass request.args because it already behaves like a dict

    return render_template('results.html', ad_lib_template=ad_lib_template)