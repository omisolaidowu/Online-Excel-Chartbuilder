# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np 
# import matplotlib.patches as mpatches

# # df = pd.read_excel('static/images/Coliform1.xlsx')
  
# # x_axis = df['Months']

# # y1 = df['ST1']
# # y2 = df['ST2']
# # # Ygirls = [10,20,20,40,69]
# # # Zboys = [20,30,25,30,56]
# # # nboys = [20,40,35,40,76]
# # # mboys = [30,60,75,80,45]
# # # tboys = [150,60,18,48,87]


# # y_axis = [y1, y2]


  
# # x = np.arange(len(x_axis))

# # bar_width = 0.18
# # v = 0
# # g = 0

# # cvar = ['blue', 'red', 'green', 'brown', 'indigo']
# # fig, ax = plt.subplots()

# # # con = 0 # Counter variable for colors:
# # 					# Code to increment colors or decrement colors and legend
# # if len(y_axis)>1:
# # 	if len(y_axis)>len(cvar):
# # 		dif = len(y_axis)-len(cvar)
# # 		for i in range(0, dif):
# # 			cvar.append('black')
		
# # 		for d in y_axis:
# # 			n = ax.bar(x_axis+bar_width*v, d, 0.18, zorder=1, color=cvar[g])
# # 			v +=1.1
# # 			g +=1
		
			
# # 	elif len(cvar)>len(y_axis):
# # 		dif2 = len(cvar)-len(y_axis)
# # 		for i in range(0, dif2):
# # 			cvar.pop()
# # 		for d in y_axis:
# # 			n = ax.bar(x_axis+bar_width*v, d, 0.18, zorder=1, color=cvar[g])
# # 			v += 1.1
# # 			g +=1
			
# # 	else:
# # 		for d in y_axis:
# # 			n = ax.bar(x_axis+bar_width*v, d, 0.18, zorder=1, color=cvar[g])
# # 			v += 1.1
# # 			g +=1
# # 	v = []
# # 	counter = 0 #counter variable for legend

# # 	for b in cvar:
# # 		f = mpatches.Patch(color=b, label=y_axis[counter])
# # 		counter += 1
# # 		v.append(f)
# # 	plt.legend(handles=v)
# # 	plt.show()
	  
# # 	# plt.xticks(x, x_axis)
# # 	# pngImage = io.BytesIO()
# # 	# FigureCanvas(fig).print_png(pngImage)
# # 	# pngImageB64String = "data:image/png;base64,"
# # 	# pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

# # 	# Rendering an instance of the generated plot
# # 	# return render_template('barchart.html', image=pngImageB64String, df4=df4)
# # elif len(y_axis)==1:
# # 	for b in y_axis:
# # 		ax.bar(x, b, 0.5, color="brown")
# # 	plt.xticks(x, x_axis)
# # 	f = [mpatches.Patch(color="brown", label=y_axis)]
# # 	plt.legend(handles=f)
# # 	plt.show()

# b = [1, 23, 4, 5]


# x = np.arange(len(b))
# print(x)
# 	# pngImage = io.BytesIO()
# 	# FigureCanvas(fig).print_png(pngImage)
# 	# pngImageB64String = "data:image/png;base64,"
# 	# pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

# 	# Rendering an instance of the generated plot
# 	# return render_template('barchart.html', image=pngImageB64String, df4=df4)
# # else:
# # 	print("There is a problem")

		


# # v = 0
# # a = [1, 2, 3, 5]
# # for i in a:
# # 	i=i*v
# # 	v +=1
# # 	print(i)
















# # # df = pd.read_csv('static/images/Barnabas.csv')
# # # a = df["AGRICULTURE"].astype(str)

# # # a=a.str.replace(",","").astype(float)


# # # print(a)








# # # df.to_excel('static/images/nabas.xlsx')

# # # read_file = pd.read_csv (r'Path where the CSV file is stored/File name.csv')
# # # read_file.to_excel (r'Path to store the Excel file\File name.xlsx', index = None, header=True)

# # # for i in df['AGRICULTURE']:
# # # 	i = i.replace(',', '')
# # # 	print(i)

# # # cou = 0

# # # plot = [df['AGRICULTURE'], df['Forestry']]

# # # # if len(plot)>cou:
# # # # 	for i in plot:
# # # # 		df3 = i.replace(',', '')
# # # # 		cou+=1
# # # # 		print(df3)
# # # for i in plot:
# # # 	df3 =[str(a).replace(',', '') for a in i]
# # # 	# print(df3.astype(float))
# # # 	df4 = [float(i) for i in df3]
# # # 	print(df4)
# # # # for i in df4:
# # # # 	# df3 = float(i)
# # # # 	print(type(df4))








# # # x = [1, 2, 3, 4]

# # # y = [2, 3, 4, 5]

# # # z = [10, 11, 12, 5]

# # # plt.plot(x, y)
# # # plt.plot(x, z)
# # # plt.legend()
# # # plt.show()
# # # cvar = ['blue', 'red', 'green']
# # # print(len(cvar))

# myArray = [
#     {'x': {1:50, 2:60, 3:70}, 'y': {1: 7, 2: 8, 3: 9}}
    
#   ]

# for i in myArray[0].values():
# 	for i in i.values():
# 		print(i)

# myArray = {
#     'x': {1:50, 2:60, 3:70}, 'y': {1: 7, 2: 8, 3: 9}
# }

# # print(len(myArray))
# # for i in myArray:
# # 	for k in myArray[i]:
# # 		print(k)

# for i in myArray.values():
# 	for i in i.values():
# 		print(i)

# # print(myArray)
# arr = ["Welcome", "to"]

# print("-".join(arr))


# j = "Idowu"
# print(len(j))

# a = [3j, 2, 4, 7, 8]
# b =[9, 9]

# a.append(3, 7)
# print(a)




# a.pop(2)
# print(a)
# b.copy()



# y = open("file.txt", "rb")
# print(y.read())

# print("IDOWU".capitalize())
from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib.parse
load_dotenv()


a = os.getenv("NAME")
b = os.getenv("PASSWORD")

print(a)
print(b)

# Database_URL = f'mongodb+srv://idowupaul:{b}'\
#               '@cluster0.jzhee.mongodb.net/mydb?'\
#               'retryWrites=true&w=majority'

Database_URL= "mongodb+srv://idowupaul:" + urllib.parse.quote(b) +\
     "@cluster0.jzhee.mongodb.net/mydb?retryWrites=true&w=majority"

connection=MongoClient(Database_URL)


db = connection.mydb 

user = {"username":"Idowu", "email":"omisolaidowu",
		"password":"secret"}
data = {"excel":"Idowu", "ema":"omisolaidowu",
		"pass":"secret"}

# print(db.Newcus)
db.Newcus.insert_one(data)

# connection = MongoClient()
# connection = MongoClient("mongodb+srv://idowupaul:"+b+"@cluster0.jzhee.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = Database_URL.test

# idowupaul
# omisolaidowu