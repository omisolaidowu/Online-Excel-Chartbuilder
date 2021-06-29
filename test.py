import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('static/images/Barnabas.csv')
a = df["AGRICULTURE"].astype(str)

a=a.str.replace(",","").astype(float)


print(a)

# df.to_excel('static/images/nabas.xlsx')

# read_file = pd.read_csv (r'Path where the CSV file is stored/File name.csv')
# read_file.to_excel (r'Path to store the Excel file\File name.xlsx', index = None, header=True)

# for i in df['AGRICULTURE']:
# 	i = i.replace(',', '')
# 	print(i)

# cou = 0

# plot = [df['AGRICULTURE'], df['Forestry']]

# # if len(plot)>cou:
# # 	for i in plot:
# # 		df3 = i.replace(',', '')
# # 		cou+=1
# # 		print(df3)
# for i in plot:
# 	df3 =[str(a).replace(',', '') for a in i]
# 	# print(df3.astype(float))
# 	df4 = [float(i) for i in df3]
# 	print(df4)
# # for i in df4:
# # 	# df3 = float(i)
# # 	print(type(df4))








# x = [1, 2, 3, 4]

# y = [2, 3, 4, 5]

# z = [10, 11, 12, 5]

# plt.plot(x, y)
# plt.plot(x, z)
# plt.legend()
# plt.show()
# cvar = ['blue', 'red', 'green']
# print(len(cvar))