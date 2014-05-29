#!/usr/bin/env python3
# web_app.py
# David Prager Branner
# 20140529, works

"""Flask application to run URL-shortening project."""

from flask import Flask, render_template, redirect, session, Markup, make_response
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import shorten
import lookup
import utils as U

class InputForm(Form):
    url = TextAreaField('URL to be shortened', validators=[DataRequired()])
    submit = SubmitField('submit')

app = Flask(__name__) # __name__ because this file is self-contained.
app.config['SECRET_KEY'] = 'secretsecret'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'message' not in session:
        session['message'] = ''
    session['url'] = None
    session['path'] = None
    the_form = InputForm()
    if the_form.validate_on_submit():
        session['url'] = the_form.url.data
        # Validate this url before proceeding.
        if U.validate_by_opening(session['url']):
            # Remove any previous messages.
            session['message'] = ''
            return redirect('/shortened')
        else:
            session['message'] = (
                '''URL {} could not be validated; try again.'''.
                format(session['url']))
    return render_template('index.html', form=the_form, session=session)

@app.route('/shortened')
def results(path=None):
    path = shorten.shorten(session)
    session['path'] = path
    session['message'] = ''
    return render_template('results.html', path=path)

@app.route('/<path>')
def send_away(path):
#    if path == None:
#        print('here')
#        session['message'] = ''
#        return redirect('/')
    # Send to function to look up original URL.
    # Serve new page bearing the path assigned.
    retrieved_url = lookup.get_url(path)
    if retrieved_url == None:
        session['message'] = 'Path {} was not found'.format(path)
        return redirect('/')
    return render_template('refresh.html', url=retrieved_url[0])

if __name__ == '__main__':
    app.run(debug=True)
