#!/usr/bin/env python3
""" Index Page Route"""

from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Sophie'}
    posts = [
            {
                'author': {'username':'Pauline'},
                'body':'The African Bible'
            },
            {
                'author': {'username': 'Vincentian'},
                'body':'Christ is All'
            },
            {
                'author': {'username': 'Vincentia'},
                'body':'All Glory To Jesus'
            }
        ]
    return render_template('index.html', title='Home', user=user, posts=posts)
