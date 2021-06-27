from wtforms import Form, BooleanField, StringField, PasswordField, validators, DateTimeField
from wtforms import FileField, TextAreaField, FieldList
from flask import request, redirect, flash
import re
from regex import Regex
from wtforms.validators import Optional, Regexp, UUID
import datetime
import os
from datetime import datetime
from uuid import UUID
import uuid
from flask_wtf import FlaskForm


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the terms of service', [validators.DataRequired()])

class UserPostForm(Form):
    content = TextAreaField('Create a post', [validators.Length(min=4, max=2000)])
    created = DateTimeField("Until", format="%Y-%m-%dT%H:%M:%S",
    	default=datetime.today, validators=[validators.DataRequired()])
    image   = FileField('image', [validators.Length(max=2000)])
    description  = TextAreaField(u'Image Description')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class upload(Form):
	excel = FileField('excel')
	data1 = StringField('Enter name of x column')
	data2 = StringField('Enter name of y column')
	project = StringField('Enter title of project')


# def upload(request):
#     form = UserPostForm(request.POST)
#     if form.image.data:
#         image_data = request.FILES[form.image.name].read()
#         open(os.path.join('images', form.image.data), 'w').write(image_data)


# def random_filename(filename):
#     ext = os.path.splitext(filename)[1]
#     new_filename = uuid.uuid4().hex + ext
#     return new_filename