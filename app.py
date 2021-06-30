from flask import Flask, g, session
from flask import render_template
from db import Post, User
from couchdb import Server
from flask import request, redirect, flash, url_for
from flask import session
from forms import RegistrationForm, UserPostForm, upload, excels
from dbsession import DatabaseObject
from couchdb.client import Database
# from uuid import UUID
from couchdb.http import PreconditionFailed
from flaskext.couchdb import ViewDefinition
# import simplejson
from charts.line import linePlot
# from bson import json_util
# import json
from encoder import DateTimeEncoder
from flask_session import Session
# from redis import Redis

# from wtforms import FileField
import os

from flask_uploads import IMAGES, configure_uploads, UploadSet 
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__, static_url_path='/static')
app.debug=True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# UPLOAD_FOLDER = 'uploads/images'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# Session(app)
app.config['UPLOADED_IMAGES_DEST'] = 'static/images'
uset = UploadSet('images', extensions=('xls', 'xlsx', 'csv'))
configure_uploads(app, uset)
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
server = Server()

@app.route("/", methods=["GET", "POST"])
def home():
	# form = UserPostForm(request.form)
	return render_template('dashboard.html')

	# if request.method == 'POST' and form.validate():
	# 	file = request.files['image']
	# 	print(file)
	# 	file = uset.save(file)
	# 	post = {"content":form.content.data,
	# 	"created":json.dumps(form.created.data, indent=4, cls=DateTimeEncoder),
	# 	"image":file, "description":form.description.data}
	# 	# post = json.dumps(post, indent=4, cls=DateTimeEncoder)
	# 	db = server['flaskdb']
		
	# 	doc_id, doc_rev=db.save(post)
	# 	flash('Posted successfully!')
	# 	return redirect('/')


# The chart builder:
@app.route('/plotchart', methods=['GET', 'POST'])	
def bring():
	return linePlot()


@app.route('/register', methods=['GET', 'POST'])

def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = {"username":form.username.data, "email":form.email.data,
		"password":form.password.data}
		server = Server()
		db = server['flaskuse']
		doc_id, doc_rev=db.save(user)
		return "<h2>Registered successfully</h2>"

	return render_template('register.html', form=form)

@app.route("/feed", methods=["GET", "POST"])
def feeds():
	db = server['flaskdb']
	map_func = '''function(doc) 
	{ emit(doc.doc_rev, doc); }'''
	feed = User.query(db, map_func, reduce_fun=None, reverse=True)

	
	return render_template('feeds.html', feed=feed)

