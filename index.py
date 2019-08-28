import csv

DataFile=open('.\\Pdata\\out.csv','r',encoding="utf-8")
Datareader=csv.reader(DataFile)
Lines=[]
#往返 0
#环线 1
#上行 2
#下行 3



#需要跳过第一行
for row in Datareader:
	try:
		if str(row[2][0])=='上':
			Lines.append(['2',row[2][3:-1],'3',row[4][3:-1]])
		elif str(row[2][0])=='环':
			Lines.append(['1',row[2][3:-1]])
		elif str(row[2][0])=='S':
			Lines.append(['0',row[2][0:-1]])
	except Exception as e:	
		#print(e)
		print('error')
#参数检验		
'''
@param start 
@param end
@param Lines i 为公交号码 值为 公交路线
'''
def checkParam(start,end,Lines):
	if not isinstance(start,int):
		print('start 参数错误')
		return False
	elif not isinstance(end,int):
		print('end 参数错误')
		return False
	elif not isinstance(Lines,list):
		print('Lines 参数错误')
		return False
	else: 
		return True
#根据节点搜索路线
'''
@param start
@param end
@param Lines
'''
def searchLine(start,end,Lines):
	if checkParam(start,end,Lines):
		startLine=[]
		endLine=[]
		for i in range(len(Lines)):
			try:
				if len(Lines[i])>2:
					Line_tmp1=''.join(Lines[i][1]).split('-')
					Line_tmp2=''.join(Lines[i][3]).split('-')
					for j in range(len(Line_tmp1)):
						if str(start)==Line_tmp1[j][1:]:
							#print('success search ' + str(start) +' from up')
							#print('Line'+str(i+1))
							startLine.append(i+1)
						elif str(end)==Line_tmp1[j][1:]:
							#print('success search '+str(end)+' from up')
							#print('Line'+str(i+1))
							endLine.append(i+1)
					for j in range(len(Line_tmp2)):
						if str(start)==Line_tmp2[j][1:]:
							#print('success search '+ str(start) +' from down')
							#print('Line'+str(i+1))
							startLine.append(i+1)
						elif str(end)==Line_tmp2[j][1:]:
							#print('success search '+str(end)+' from down')
							#print('Line'+str(i+1))
							endLine.append(i+1)
				else:
					Line_tmp=''.join(Lines[i][1]).split('-')
					for k in range(len(Line_tmp)):
						if str(start)==Line_tmp[k][1:]:
							#print('success serach '+str(start))
							#print('Line'+str(i+1))
							startLine.append(i+1)
						elif str(end)==Line_tmp[k][1:]:
							#print('success search ' +str(end))
							#print('Line'+str(i+1))
							endLine.append(i+1)
			except Exception as e:
				#print(e)
				print('error')
		print(list(set(startLine)),list(set(endLine)))
		resline=[]
		resline.append(list(set(startLine)))
		resline.append(list(set(endLine)))
		return resline

#在两个路线中查找受否有相同的
'''
@param startLine[]
@param endLine[]
'''
def serachFromTwoLines(startLine,endLine):
	for i in startLine:
		for j in endLine:
			if i==j:
				return True
				return i
			else:
				return False


# 用来把路线转换为节点列表的函数
def convertNode(Line):
	if len(Line)>2:
		nodeUp=''.join(Line[1]).split('-')
		nodeDown=''.join(Line[3]).split('-')
		return nodeUp,nodeDown
	if len(Line)==2:
		node=''.join(Line[1]).split('-')
		return node

# 通过寻找线路上的站点 看是否有相同站点 即为换乘站点
def serachEqualNode(startLine,endLine):
	print(len(Lines[351]))
	for i in range(len(startLine)):
		startLineNode=convertNode(Lines[startLine[i]-1])
	for j in range(len(endLine)):
		endLineNode=convertNode(Lines[endLine[j]-1])
	print(startLineNode,endLineNode)
# main function
resline=searchLine(3359,1828,Lines)
if serachFromTwoLines(resline[0],resline[1]):
	i=serachFromTwoLines(resline[0],resline[1])
	print(i)
	print('找到直达路径')
else:
	print('未找到直达路径')
	serachEqualNode(resline[0],resline[1])
