from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class Comment(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    text = StringField('Text', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Submit')