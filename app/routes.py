from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'droopy'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in San Diego!'
        },
        {
            'author': {'username': 'Jill'},
            'body': 'The Star Wars movie was awesome.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
