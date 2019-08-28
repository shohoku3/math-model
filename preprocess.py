import csv
import re
f=open('.\\Bdata\\1.1.txt','r')
outputfile=open('.\\Pdata\\out.csv','w',newline='',encoding="utf-8")
outputWrite=csv.writer(outputfile)
count=0
Line=[]
stopReg=re.compile(r'[S0-9]{5}')
node=[]
for row in f:
	count+=1
	Line.append(row)
	result=stopReg.findall(str(row))
	if result!=[]:
		Line.insert(6,len(result))
		node+=result
		node=list(set(node))
	if count==4:
		outputWrite.writerow(Line)
		count=0
		Line=[]

print('统计的总站点数'+str(len(node)))
outputWrite.writerow(['统计的总站点数'+str(len(node))])