from flask import Flask, g, session
from flask import render_template
from db import Post, User
from couchdb import Server
from flask import request, redirect, flash, url_for
from flask import session
from forms import RegistrationForm, UserPostForm, upload, excels
from dbsession import DatabaseObject
from couchdb.client import Database
from uuid import UUID
from couchdb.http import PreconditionFailed
from flaskext.couchdb import ViewDefinition
import simplejson
# from bson import json_util
import json
from encoder import DateTimeEncoder
# from flask_session import Session
# from redis import Redis

from wtforms import FileField
import os
from flask_uploads import IMAGES, configure_uploads, UploadSet 
from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage
from uuid import UUID
import uuid
from flask_uploads import UploadNotAllowed
import pandas as pd
import openpyxl
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import base64
import matplotlib.patches as mpatches
import matplotlib
matplotlib.use('Agg')

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
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
server = Server()

@app.route("/", methods=["GET", "POST"])
def home():
	form = UserPostForm(request.form)

	if request.method == 'POST' and form.validate():
		file = request.files['image']
		print(file)
		file = uset.save(file)
		post = {"content":form.content.data,
		"created":json.dumps(form.created.data, indent=4, cls=DateTimeEncoder),
		"image":file, "description":form.description.data}
		# post = json.dumps(post, indent=4, cls=DateTimeEncoder)
		db = server['flaskdb']
		
		doc_id, doc_rev=db.save(post)

		# print(form.image.data)
		
		# image_data = request.FILES[form.image.data].read()
		# open(os.path.join('uploads/images', form.image.data), 'w').write(form.image.data)
		
		# 

		# filename = images.save(form.image.name)
		# print(form.image.data)
		
		# ext = os.path.splitext(file)[1]
		# file = uuid.uuid4().hex + ext
		

		# with open(form.image.data, 'rb') as fp:
		# filename = file.filename
		


		# post.store(db)
		
		# filename = images.save(form.image.data)
		
		
		



		# if form.image.data:
		# 	image_data = request.files[form.image.data].read()
		# 	open(os.path.join('images', form.image.data), 'w').write(image_data)
		# f = form.image.data
		# filename = random_filename(f)
		# os.path.join(app.config['UPLOAD_PATH'], filename)
		
			# image_data = request.files[form.image.name].read() 	
		# (os.path.join('images'))


		
		
		# doc = db[doc_id]

		flash('Posted successfully!')
		return redirect('/')


		
	return render_template('home.html', form=form)


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




# The chart builder:
@app.route('/plotchart', methods=['GET', 'POST'])	
def upload_file():

	# This block is getting the excel sheet name from the database and populating it to -->
	# SelectField in forms.py 
	form = upload(request.form)
	form2 = excels(request.form)
	server = Server()
	e_file = server['flaskdb']
	map_func = '''function(doc) { emit(doc.doc_rev, doc); }'''
	feed = User.query(e_file, map_func, reduce_fun=None, reverse=True)
	form.exsheets.choices = [(i.excel) for i in feed]
	# print(form.exsheets.choices)

	
	if request.method == 'POST':	
		try:
			file = request.files['excel']

			if file and form2.validate():
				try:
					file = uset.save(file)
					db = server['flaskdb']
					post = {"excel":file}
				
					if '.xlsx' or '.csv' in file:
						doc_id, doc_rev=db.save(post)
						flash("Upload success! Please select your excel sheet from the dropdown", "success")
						return redirect('/plotchart')
					else:
						flash("Please upload an excel (.xlsx) file", 'fail')
				except UploadNotAllowed:
					flash('Please uplaod an excel (.xlsx or a .csv) file', 'fail')


			if "plot" in request.form and form.validate():		
				x_axis = form.data1.data
				y_axis = form.data2.data
				exfile = form.exsheets.data



				y_axis2 = form.data2.data
				y_axis2 = y_axis2.split(", ") #this is a list object (converting y_axis data to list)
				if '.xlsx' in exfile:
					df = pd.read_excel('static/images/'+exfile)
				elif '.csv' in exfile:
					df = pd.read_csv('static/images/'+exfile)
				df2 = [raw.replace(' ', '_') for raw in df.columns]
				df.columns = df2
				df1 = df.to_dict()

				try:
					ydata = []
					for i in y_axis2:
						ydata.append(df1[i])

					new_data = [x_axis, df1[x_axis], y_axis, ydata]
					new_data = {new_data[a]:new_data[a+1] for a in range(0, len(new_data), 2)}

					plotdata = []
					for a in y_axis2:
						# Cleaning CSV/Excel string/float issue irregularities
						plotdata.append(df[a].astype(str).str.replace(",","").astype(float)) # populating df with each data in y_axis2 declared earlier
					
					# print(type(plotdata))
					# return new_data
					fig, ax = plt.subplots()
					x = df[x_axis]
					plt.xlabel(x_axis)
					plt.ylabel('Frequency of: {}'.format(y_axis))
					plt.title(form.project.data)



					# cvar = form.color.data.split(", ") # in case i later decide to allow users enter colours

					cvar = ['blue', 'red', 'green', 'brown', 'indigo']
					con = 0 # Counter variable for colors:
					# Code to increment colors or decrement colors and legend
					if len(plotdata)>len(cvar):
						dif = len(plotdata)-len(cvar)
						for i in range(0, dif):
							cvar.append('black')
						for d in plotdata:
							n = ax.plot(x, d, color=cvar[con])
							con += 1
					elif len(cvar)>len(plotdata):
						dif2 = len(cvar)-len(plotdata)
						for i in range(0, dif2):
							cvar.pop()
						for d in plotdata:
							n = ax.plot(x, d, color=cvar[con])
							con += 1
					else:
						for d in plotdata:
							n = ax.plot(x, d, color=cvar[con])
							con += 1

					v = []
					counter = 0 #counter variable for legend

					for b in cvar:
						f = mpatches.Patch(color=b, label=y_axis2[counter])
						counter += 1
						v.append(f)
					plt.legend(handles=v)

					# Testing legend patches (don't uncomment):

					# ax.legend([n], ['One', 'Two', 'Three'], bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
					# plt.box(False)
					# f = mpatches.Patch(label='The red data')
					# e = mpatches.Patch(label='The red data')
					# g = mpatches.Patch(label='The red data')

					# Tpatches = [f, e, g]
					# return fig
					# plt.savefig('static/images/instant_plot.png')
					# return new_data

					# Converting generated figure into an HTML readable format
					pngImage = io.BytesIO()
					FigureCanvas(fig).print_png(pngImage)
					pngImageB64String = "data:image/png;base64,"
					pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

					# Rendering an instance of the generated plot
					return render_template('plot.html', image=pngImageB64String)

				except KeyError:
					# return df1
					flash("Field error: Invalid column name(s)", "fail")

		except ValueError:
			flash("That file type is not supported, upload a .xlsx file", "fail")

			# return pngImageB64String


			



			# except KeyError:
			# 	return df
					# flash("Please enter the correct keys keys, can't get required columns from your data")
			# except TypeError:
			# 	flash("Please make sure your data doesn't have any extra data")
				
			
			


				

			

			# return df
			# filename.FileStorage('uploads/images')
			# print(filename)
			# ext = os.path.splitext(filename)[1]
			# new_filename = uuid.uuid4().hex + ext
			# print(filename)

			# uset.save(filename)
		
	return render_template('dashboard.html', form=form, form2=form2)

    

@app.route("/userdb", methods=["GET", "POST"])
def createdbUser():
	if request.method == 'POST':
		server = Server()
		db = server.create('flaskuserdb')
		
		post = User()
		if post.store(db) == False:
			return '<h2>Unsuccessful</h2>'	
		else:
			return '<h2>User database created successfully!</h2>'
	return render_template('/Userdb.html', name="database")


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

	        # user.id = uuid.uuid4().hex
	        # user.store()
	        # g.couch.save(user)
	        # state = True
	        # flash('Thanks for registering')

        # return redirect(url_for('login'))


@app.route("/feed", methods=["GET", "POST"])
def feeds():
	db = server['flaskdb']
	map_func = '''function(doc) 
	{ emit(doc.doc_rev, doc); }'''
	# feed = User.query.order_by()
	feed = User.query(db, map_func, reduce_fun=None, reverse=True)

	# reduce_func = '''function (keys, created) {
 #        return created;
 #    }''',


	
	# docs = []
	
	# for row in feed(db)[id]:
	# 	docs.append(row.value)
	# d = simplejson.dumps(docs)


	# 
	# 
	# feed = Post.load(db, Post.id)
	# feed.content[0]
	# return c
	return render_template('feeds.html', feed=feed)

