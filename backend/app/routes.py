# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for
from app import app
from app.forms import CommentForm
from app import db
from app.models import Message


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CommentForm()
    messages = Message.query.all()
    if form.validate_on_submit():
        message = Message(name=form.name.data,
                          email=form.email.data,
                          body=form.body.data)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', messages=messages, form=form)
