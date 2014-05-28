#!/usr/bin/env python3
# web_app.py
# David Prager Branner
# 20140527, works

"""Flask application to run URL-shortening project."""

from flask import Flask, render_template, redirect, session, Markup
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import shorten
import lookup

class InputForm(Form):
    url = TextAreaField('URL to be shortened', validators=[DataRequired()])
    submit = SubmitField('submit')

app = Flask(__name__) # __name__ because this file is self-contained.
app.config['SECRET_KEY'] = 'secretsecret'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    the_form = InputForm()
    if the_form.validate_on_submit():
        session['url'] = the_form.url.data
        # QQQ validate this url; is it well formed? Is it real?
        return redirect('/shortened')
    return render_template('index.html', form=the_form)

@app.route('/shortened')
def results():
    path = shorten.shorten(session['url'])
    return render_template('results.html', path=path)

@app.route('/<path>')
def send_away(path):
#    print('path found:', path) # debug
    # Send to function to look up original URL.
    # Serve new page bearing .
    retrieved_url = lookup.get_url(path)
#    print('in send_away:', retrieved_url) # debug
    return render_template('refresh.html', url=retrieved_url)

if __name__ == '__main__':
    app.run(debug=True)
