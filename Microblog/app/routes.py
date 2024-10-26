#!/usr/bin/env python3
""" Index Page Route"""

from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
