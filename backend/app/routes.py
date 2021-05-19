# -*- coding: utf-8 -*-
from flask import render_template, redirect
from app import app
from app.forms import Comment

messages = [
    {'name': 'Andrei',
     'email': 'andre@gmail.com',
     'text': 'Hello bildiiii'}
]


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Comment()
    print("HELLO")
    print(dir(form))
    if form.validate_on_submit():
        messages.append(
            {'name' : form.name.data,
             'email' : form.email.data,
             'text' : form.text.data})
        print(messages)
        #return redirect('/index')
    return render_template('index.html', title='Home', messages=messages, form=form)