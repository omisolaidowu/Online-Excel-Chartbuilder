from forms import RegistrationForm, UserPostForm, upload, excels
from flask import Flask, g, session, jsonify
from flask import render_template
# from db import Post, User
from couchdb import Server
from flask import request, redirect, flash, url_for
from flask import session
from forms import RegistrationForm, UserPostForm, upload, excels

from uuid import UUID
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
from pymongo import MongoClient

matplotlib.use('Agg')

app = Flask(__name__)

app.config['UPLOADED_IMAGES_DEST'] = 'static/uploads'
uset = UploadSet('images', extensions=('xls', 'xlsx', 'csv'))
configure_uploads(app, uset)
connection = MongoClient()
db = connection.mydb #database name.
collection = db.Newcus
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def linePlot():

	# This block is getting the excel sheet name from the database and populating it to -->
	# SelectField in forms.py 
	form = upload(request.form)
	form2 = excels(request.form)
	feed = collection.find({})
	feed = [i for i in feed]
	form.exsheets.choices = [i['excel'] for i in feed]
	print(feed)
	# exfile = form.exsheets.data
	# if form.validate():
	# 	exfile = form.exsheets.data
	# 	df = pd.read_csv('static/images/'+exfile)
	# 	df = df.to_html()
	# 	return render_template("lineplot.html", df=df)
	# df = df.to_html()
	# # print(form.exsheets.choices)

	
	if request.method == 'POST':	
		try:
			file = request.files['excel']

			if file and form2.validate():
				try:
					file = uset.save(file)
					
			
					post = {"excel":file}
				
					if '.xlsx' or '.csv' in file:
						collection.insert_one(post)
						flash("Upload success! Please select your excel sheet from the dropdown", "success")
						return redirect('/plotchart')
						# return flask_excel.ExcelRequest.get_sheet(field_name="Forestry", sheet_name="Barnabase.xlsx", "success")
						
					else:
						flash("Please upload an excel (.xlsx) file", 'fail')
				except UploadNotAllowed:
					flash('Please uplaod an excel (.xlsx or a .csv) file', 'fail')


			if "view" in request.form and form.validate():
				myfile = form.exsheets.data
				if '.xlsx' in myfile:
					df = pd.read_excel('static/uploads/'+myfile)
				elif '.csv' in myfile:
					df = pd.read_csv('static/uploads/'+myfile)
				df2 = [raw.replace(' ', '_') for raw in df.columns]
				df.columns = df2
				df = df.to_html()
				# df = df.to_json()
				flash(df, "neutral")

			if "plot" in request.form and form.validate():		
				x_axis = form.data1.data
				y_axis = form.data2.data
				exfile = form.exsheets.data



				y_axis2 = form.data2.data
				y_axis2 = y_axis2.split(", ") #this is a list object (converting y_axis data to list)
				if '.xlsx' in exfile:
					
					df = pd.read_excel('static/uploads/'+exfile)
				elif '.csv' in exfile:
					
					df = pd.read_csv('static/uploads/'+exfile)
				df2 = [raw.replace(' ', '_') for raw in df.columns]
				df.columns = df2
				df1 = df.to_dict()
				
				df4 = df.to_html()
				for i in df.columns:
					i = i

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
						f = mpatches.Patch(color=b, label=y_axis2[counter].replace('_', ' '))
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
					return render_template('line.html', image=pngImageB64String, df4=df4)

				except KeyError:
					# return df1
					flash("Field error: Invalid column name(s)", "fail")

		except ValueError:
			flash("That file type is not supported, upload a .xlsx file", "fail")
		except FileNotFoundError:
			flash("Oops! Looks like we can't find that file, please upload another one and select it", "fail")

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
	return render_template('lineplot.html', form=form, form2=form2)
	
