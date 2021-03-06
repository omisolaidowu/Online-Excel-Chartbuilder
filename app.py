from typing import Collection
from flask import Flask, g, session, jsonify
from flask import render_template
from flask import request, redirect, flash, url_for
from flask import session
from forms import RegistrationForm, UserPostForm, upload, excels
from dbsession import DatabaseObject
from charts.line import linePlot
from charts.bars import barPlot

from encoder import DateTimeEncoder
from flask_session import Session

import os

from flask_uploads import IMAGES, configure_uploads, UploadSet 
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import flask_excel as excel
from flask_pymongo import PyMongo
from pymongo import MongoClient

from dotenv import load_dotenv
import os
import urllib.parse
import pymongo
from dotenv import load_dotenv

app = Flask(__name__, static_url_path='/static')
app.debug=True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
load_dotenv('.env')


Database_URL = os.environ.get("mongo_URL")






# manager.sync(app)

# UPLOAD_FOLDER = 'uploads/images'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# Session(app)
app.config['UPLOADED_IMAGES_DEST'] = 'static/uploads'
uset = UploadSet('images', extensions=('xls', 'xlsx', 'csv'))
configure_uploads(app, uset)

 

app.config["MONGO_URI"] = Database_URL

mongo = PyMongo(app)

connection=MongoClient(Database_URL)

# connection = MongoClient()
db = connection.mydb #database name.


# connection = MongoClient("mongodb+srv://idowupaul:<password>@cluster0.jzhee.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

collection = {
	"files": db.Newcus,
	"users": db.users
	}
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#


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
	
		

@app.route('/barchart', methods=['GET', 'POST'])	
def myBar():
	return barPlot()



@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = {"username":form.username.data, "email":form.email.data,
		"password":form.password.data}
		collection["users"].insert_one(user)
		# server = Server()
		# db = server['flaskuse']
		# doc_id, doc_rev=db.save(user)
		return "<h2>Registered successfully</h2>"

	return render_template('register.html', form=form)
	
if __name__ == '__main__':
	app.run()

# @app.route("/feed", methods=["GET", "POST"])
# def feeds():
# 	db = server['flaskdb']
# 	map_func = '''function(doc) 
# 	{ emit(doc.doc_rev, doc); }'''
# 	feed = User.query(db, map_func, reduce_fun=None, reverse=True)

	
# 	return render_template('feeds.html', feed=feed)


# if __name__ =="__main__":
# 	app.config().update(
# 		DEBUG = True,
# 		COUCHDB_SERVER = 'http://localhost:5984',
# 		COUCHDB_DATABASE = 'flaskdb'

# 	)
# 	manager = CouchDBManager()
# 	manager.setup(app)
# 	manager.sync(app)
# 	app.run(host='0.0.0.0', port=5000)
	# manager.add_viewdef(docs_by_author)

