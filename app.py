"""Madlibs Stories."""
from flask import Flask, render_template
from flask import request
from flask_debugtoolbar import DebugToolbarExtension
from random import randint
from random import choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickens'
debug = DebugToolbarExtension(app)


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# storyv2 = Story(
#     []
# )

s = Story(["noun", "verb"], "I love to {verb} a good {noun}.")
ans = {"verb": "eat", "noun": "mango"}
print(s.generate(ans))


@app.route('/form')
def form_page():
    prompts = story.prompts
    print(prompts)
    return render_template('form.html', prompts=prompts)


# @app.route('/greet-2')
# def get_greeting_2():
#     username = request.args['username']
#     wants = request.args.get('wants_compliments')
#     nice_things = sample(COMPLIMENTS, 3)
#     return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)


@app.route('/questions')
def show_quesions():
    user_questions = request.args['questions']
    print(request.args)
    return render_template('questions.html', user_questions=user_questions)


@app.route('/story')
def show_story():

    text = story.generate(request.args)

    return render_template('story.html', text=text)


# @app.route("/")
# def ask_questions():
#     """Generate and show form to ask words."""

#     prompts = story.prompts

#     return render_template("questions.html", prompts=prompts)


# @app.route("/story")
# def show_story():
#     """Show story result."""

#     text = story.generate(request.args)

#     return render_template("story.html", text=text)
