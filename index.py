import csv

DataFile=open('.\\Pdata\\out.csv','r',encoding="utf-8")
Datareader=csv.reader(DataFile)
Lines=[]
#需要跳过第一行
for row in Datareader:
	try:
		if str(row[2][0])=='上':
			Lines.append(row[2][3:-1])
			Lines.append(row[4][3:-1])
		if str(row[2][0]=='环'):
			Lines.append(row[2][3:-1])
		else:
			Lines.append(row[2])
	except Exception as e:	
		print(Lines)

#建立Line与路线之间的关系
# line[i] i 为公交号码 值为 公交路线

