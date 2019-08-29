import csv

start='S3359'
end='S1828'


DataFile=open('.\\Pdata\\out.csv','r',encoding="utf-8")
Datareader=csv.reader(DataFile)
Balance=[]
Lines=[]
#往返 0
#环线 1
#上行 2
#下行 3



#需要跳过第一行
for row in Datareader:
	try:
		Balance.append(row[1])
		if str(row[2][0])=='上':
			Lines.append(['2',row[2][3:-1],'3',row[4][3:-1]])
		elif str(row[2][0])=='环':
			Lines.append(['1',row[2][3:-1]])
		elif str(row[2][0])=='S':
			Lines.append(['0',row[2][0:-1]])
	except Exception as e:	
		#print(e)
		print(e)
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
							startLine.append(i+1)
						elif str(end)==Line_tmp1[j][1:]:
							endLine.append(i+1)
					for j in range(len(Line_tmp2)):
						if str(start)==Line_tmp2[j][1:]:
							startLine.append(i+1)
						elif str(end)==Line_tmp2[j][1:]:
							endLine.append(i+1)
				else:
					Line_tmp=''.join(Lines[i][1]).split('-')
					for k in range(len(Line_tmp)):
						if str(start)==Line_tmp[k][1:]:
							startLine.append(i+1)
						elif str(end)==Line_tmp[k][1:]:
							endLine.append(i+1)
			except Exception as e:
				print(e)
		print('--------通过起点终点找寻到的路线有---------')
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
	if len(Line)!=2:
		nodeUp=''.join(Line[1]).split('-')
		nodeDown=''.join(Line[3]).split('-')
		return nodeUp,nodeDown
	elif len(Line)==2:
		node=''.join(Line[1]).split('-')
		return node

# 寻找线路上的站点 看是否有相同站点 即为换乘站点
def serachEqualNode(startLine,endLine):
	resList=[]
	for i in range(len(startLine)):
		startLineNode=convertNode(Lines[startLine[i]-1])
		for j in range(len(endLine)):
			endLineNode=convertNode(Lines[endLine[j]-1])
			if EqualNode(startLineNode,endLineNode):
				print('------------尝试寻找一次换乘路线-----------')
				print('L0'+str(startLine[i]),'L0'+str(endLine[j]))
				resnode=EqualNode(startLineNode,endLineNode)
				print(list(set(resnode)))
				resList.append([startLine[i],endLine[j],list(set(resnode))])
	return resList

# 通过寻找线路上的站点 看是否有相同站点 即为换乘站点
def EqualNode(startLineNode,endLineNode):
	resnode=[]
	if isinstance(startLineNode,list) & isinstance(endLineNode,list):
		for i in startLineNode:
			for j in endLineNode:
				if i==j:
					resnode.append(i)
				else:
					pass
	elif isinstance(startLineNode,tuple) &isinstance(endLineNode,list):
		for i in endLineNode:
			for j in startLineNode[0]:
				if i==j:
					resnode.append(i)
				else:
					pass
		for i in endLineNode:
			for j in startLineNode[1]:
				if i==j:
					resnode.append(i)
				else:
					pass
	elif isinstance(startLineNode,list) &isinstance(endLineNode,tuple):
		for i in startLineNode:
			for j in endLineNode[0]:
				if i==j:
					resnode.append(i)
				else:
					pass
		for i in startLineNode:
			for j in endLineNode[1]:
				if i==j:
					resnode.append(i)
				else:
					pass
	elif isinstance(startLineNode,tuple) &isinstance(endLineNode,tuple):
		for i in startLineNode[0]:
			for j in endLineNode[0]:
				if i==j:
					resnode.append(i)
				else:
					pass
		for i in startLineNode[0]:
			for j in endLineNode[1]:
				if i==j:
					resnode.append(i)
				else:
					pass
		for i in startLineNode[1]:
			for j in endLineNode[0]:
				if i==j:
					resnode.append(i)
				else:
					pass
		for i in startLineNode[1]:
			for j in endLineNode[1]:
				if i==j:
					resnode.append(i)
				else:
					pass
	if len(resnode)!=0:
		return resnode
		return True

# 计算需换乘时间 并返回各个方案的时间集
def calTransformTime(resList,transferTime):
	print('---------计算时间-----------\n')
	result={'info':'相关信息','node':0,'sumcount':0,'sumtime':0,'sumbalance':0}
	selectLine=[]
	for i in resList:
		selectLine.append(i)
		# 判断行驶种类
		if str(Lines[i[0]-1][0]) == '2':
			Line1up=''.join(Lines[i[0]-1][1]).split('-')
			Line1down=''.join(Lines[i[0]-1][3]).split('-')
			Line2up=''.join(Lines[i[1]-1][1]).split('-')
			Line2down=''.join(Lines[i[1]-1][3]).split('-')
			for j in i[2]:
				selectLine.append(j)
				if j in Line1up:
					if Line1up.index(start)<Line1up.index(j):
						if j  in Line2up:
							if Line2up.index(j)<Line2up.index(end):
								L1count=Line1up.index(j)-Line1up.index(start)
								L2count=Line2up.index(end)-Line2up.index(j)
								sumcount=Line1up.index(j)-Line1up.index(start)+Line2up.index(end)-Line2up.index(j)
								sumtime=sumcount*3+transferTime*5
								sumbalance=calBalance(i[0],L1count)+calBalance(i[1],L2count)
								selectLine.append(sumcount)
								selectLine.append(sumtime)
								selectLine.append(sumbalance)
						if j in Line2down:
							if Line2down.index(j)<Line2down.index(end):
								L1count=Line1up.index(j)-Line1up.index(start)
								L2count=Line2down.index(end)-Line2down.index(j)
								sumcount=Line1up.index(j)-Line1up.index(start)+Line2down.index(end)-Line2down.index(j)
								sumtime=sumcount*3+transferTime*5
								sumbalance=calBalance(i[0],L1count)+calBalance(i[1],L2count)
								selectLine.append(sumcount)
								selectLine.append(sumtime)
								selectLine.append(sumbalance)
				if j in Line1down:
					if Line1down.index(start)<Line1down.index(j):
						if j in Line2up:
							if Line2up.index(j)<Line2up.index(end):
								L1count=Line1down.index(j)-Line1down.index(start)
								L2count=Line2up.index(end)-Line2up.index(j)
								sumcount=Line1down.index(j)-Line1down.index(start)+Line2up.index(end)-Line2up.index(j)
								sumtime=sumcount*3+transferTime*5
								sumbalance=calBalance(i[0],L1count)+calBalance(i[1],L2count)
								selectLine.append(sumcount)
								selectLine.append(sumtime)
								selectLine.append(sumbalance)
						if j in Line2down:
							if Line2down.index(j)<Line2down.index(end):
								L1count=Line1down.index(j)-Line1down.index(start)
								L2count=Line2down.index(end)-Line2down.index(j)
								sumcount=Line1down.index(j)-Line1down.index(start)+Line2down.index(end)-Line2down.index(j)
								sumtime=sumcount*3+transferTime*5
								sumbalance=calBalance(i[0],L1count)+calBalance(i[1],L2count)
								selectLine.append(sumcount)
								selectLine.append(sumtime)
								selectLine.append(sumbalance)
		if str(Lines[i[0]-1][0]) == '1':
			print('环线')
			
		if str(Lines[i[0]-1][0]) == '0':
			print('往返')
			
	return selectLine
#根据路线查询计价规则
def calBalance(line,lcount):
	if len(Balance[line-1])==6:
		if lcount<=20:
			return 1
		if lcount>20&lcount<=40:
			return 3
		else:
			return 6
	else:
		return 1


def mintime(selectLines):
	print(selectLines)

# main function
resline=searchLine(3359,1828,Lines)
print('----------------尝试寻找直达路径-----------')
if serachFromTwoLines(resline[0],resline[1]):
	i=serachFromTwoLines(resline[0],resline[1])
	resnode.append(i)
	print('找到直达路径')
else:
	print('未找到直达路径')
	resList=serachEqualNode(resline[0],resline[1])
	selectLine=calTransformTime(resList,1)
	mintime(selectLine)

