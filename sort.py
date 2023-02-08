import random
import pygame

import config as co
import render as r

listLen=co.listLen

arAux=list(range(listLen))
arAux2=list(range(listLen))
	
def swap(a,b):
	global ar
	temp=ar[a]
	ar[a]=ar[b]
	ar[b]=temp
	r.drawWrites(a,b)
	
def sort3(i1,i2,i3):
	global ar
	r.drawComps(i1,i2)
	if ar[i1] < ar[i2]:
		r.drawComps(i2,i3)
		if ar[i2] > ar[i3]:
			r.drawComps(i1,i3)
			if ar[i1] < ar[i3]:
				swap(i2,i3)
			else:
				temp=ar[i3]
				ar[i3]=ar[i2]
				ar[i2]=ar[i1]
				ar[i1]=temp
				r.drawWrites(i1,i2,i3)
		#else: in order
	else:
		r.drawComps(i2,i3)
		if ar[i2] > ar[i3]:
			swap(i1,i3)
		else:
			r.drawComps(i1,i3)
			if ar[i1] < ar[i3]:
				swap(i1,i2)
			else:
				temp=ar[i1]
				ar[i1]=ar[i2]
				ar[i2]=ar[i3]
				ar[i3]=temp
				r.drawWrites(i1,i2,i3)

def randInd():
	global listLen
	return random.randint(0,listLen-1)

def shuffle():
	global ar
	global listLen
	for c in range(listLen):
		i=randInd()
		if i!=c:
			swap(i,c)
		
def minishuffle(swaps):
	global ar
	global listLen
	for c in range(swaps):
		i=randInd()
		i2=randInd()
		if i!=i2:
			swap(i,i2)

def randSortSwaps(swaps):
	global ar
	global listLen
	for c in range(swaps):
		i=randInd()
		i2=randInd()
		if i<i2:
			r.drawComps(i,i2)
			if ar[i] > ar[i2]:
				swap(i,i2)
		elif i>i2:
			r.drawComps(i,i2)
			if ar[i] < ar[i2]:
				swap(i,i2)

def reverse():
	global ar
	global listLen
	for c in range(int(listLen/2)):
		swap(c,listLen-1-c)
		
def bubbleSort():
	global ar
	global listLen
	topInd=listLen-1
	while topInd > 0:
		lastSwap=0
		
		for c in range(topInd):
			r.drawComps(c,c+1)
			if ar[c] > ar[c+1]:
				swap(c,c+1)
				lastSwap=c
				
		for c in range(lastSwap+1,topInd+1):
			r.drawDone(c)
		pygame.display.update()
		topInd=lastSwap
		
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	
def tribubbleSort():
	global ar
	global listLen
	topInd=listLen-1
	while topInd > 0:
		lastSwap=0
		
		for c in range(topInd-1):
			r.drawComps(c,c+1)
			if ar[c+1] > ar[c+2]:
				lastSwap=c
			sort3(c,c+1,c+2)
				
		for c in range(lastSwap+1,topInd+1):
			r.drawDone(c)
		pygame.display.update()
		topInd=lastSwap
		
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	
def bigbubblesort():
	global ar
	global arAux
	global listLen
	topInd=listLen
	passes=0
	while topInd > 0:
		passes +=1
		auxIndTop=0
		auxIndLow=0
		arAux[0]=ar[0]
		arInd=0
		
		for c in range(1,topInd):
			cVal=ar[c]
			r.drawComps(c)
			if cVal >= arAux[auxIndTop]:#grow bubble
				auxIndTop+=1
				arAux[auxIndTop]=cVal
			elif cVal <= arAux[auxIndLow]:#swap over bubble
				ar[arInd]=cVal
				r.drawWrites(arInd)
				arInd+=1
			else:#insert into bubble
				for i in range(auxIndLow,auxIndTop+1):
					if cVal <= arAux[i]:
						auxIndLow-=1
						arAux[auxIndLow]=cVal
						break
					ar[arInd]=arAux[i]
					r.drawWrites(arInd)
					arInd+=1
					auxIndLow+=1
		
		topInd2=arInd
		for c in range(auxIndLow,auxIndTop+1):
			ar[arInd]=arAux[c]
			r.drawWrites(arInd)
			arInd+=1
		
		for c in range(topInd2,topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=topInd2
		#print(topInd)
		
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	print(passes)

#not done
def megabubblesort():
	global ar
	global arAux
	global listLen
	topInd=listLen
	passes=0
	while topInd > 0:
		passes +=1
		auxIndTop=0
		auxIndLow=0
		arAux[0]=ar[0]
		arInd=0
		tailInd=listLen
		
		for c in range(1,topInd):
			cVal=ar[c]
			r.drawComps(c)
			if cVal >= arAux[auxIndTop]:#grow bubble
				auxIndTop+=1
				arAux[auxIndTop]=cVal
			elif cVal <= arAux[auxIndLow]:#grow tail
				if tailInd == listLen:#no tail
					tailInd -= 1
					arAux[tailInd] = cVal
				elif cVal <= arAux[tailInd]:#append tail
					tailInd -= 1
					arAux[tailInd] = cVal
				elif cVal > arAux[listLen-1]:#front of tail
					#drop tail
					for i in range(tailInd,listLen):
						ar[arInd]=arAux[i]
						r.drawWrites(arInd)
						arInd+=1
					#print(listLen-tailInd)
					tailInd=listLen-1
					arAux[tailInd] = cVal
				else :#insert tail
					#print(listLen-tailInd)
					for i in range(tailInd,listLen):
						if cVal <= arAux[tailInd]:
							tailInd-=1
							arAux[tailInd]=cVal
							break
						ar[arInd]=arAux[tailInd]
						r.drawWrites(arInd)
						arInd+=1
						tailInd+=1
			else:#insert into bubble
				#drop tail
				for i in range(tailInd,listLen):
					ar[arInd]=arAux[i]
					r.drawWrites(arInd)
					arInd+=1
				#print(listLen-tailInd)
				tailInd=listLen
				
				#insert bubble
				for i in range(auxIndLow,auxIndTop+1):
					if cVal <= arAux[i]:
						auxIndLow-=1
						arAux[auxIndLow]=cVal
						break
					ar[arInd]=arAux[i]
					r.drawWrites(arInd)
					arInd+=1
					auxIndLow+=1
		
		#drop tail
		#print(listLen-tailInd)
		for i in range(tailInd,listLen):
			ar[arInd]=arAux[i]
			r.drawWrites(arInd)
			arInd+=1
		
		topInd2=arInd
		for c in range(auxIndLow,auxIndTop+1):
			ar[arInd]=arAux[c]
			r.drawWrites(arInd)
			arInd+=1
		
		for c in range(topInd2,topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=topInd2
		#print(topInd)
		
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	print(passes)
	
def megabubblemergeSort():
	travelLimitCoeff = 1
	travalLimitMin = 1
	
	global ar
	global listLen
	topInd=listLen
	passes=0
	while topInd > 1:
		passes +=1
		arInd=0
		top=Node(ar[0])
		r.drawComps(0)
		topEnd=top
		runLow=1
		for c in range(2,topInd):
			r.drawComps(c,c-1)
			if ar[c] < ar[c-1]:
				#merge
				runTop = c - 1
				r.drawComps(runLow,runTop)
				topVal = ar[runTop]
				lowVal = ar[runLow]
				travelLimit = c - runLow
				travelLimit *= travelLimitCoeff
				travelLimit += travalLimitMin
				toptopNode = top
				toplowNode = topEnd
				travel=0
				#cutNode = None
				inserted = False
				
				while runLow <= runTop and lowVal < topEnd.val:
					ar[arInd] = lowVal
					r.drawWrites(arInd)
					runLow += 1
					arInd +=1
					lowVal = ar[runLow]
					r.drawComps(runLow)
					
				if runLow <= runTop and topVal >= top.val:
					top.insertValAfter(topVal)
					runTop -= 1
					topVal = ar[runTop]
					r.drawComps(runTop)
					top = top.next
					
					
				while runLow <= runTop:
					
					while runLow <= runTop and topVal >= toptopNode.val:
						toptopNode.insertValAfter(topVal)
						runTop -= 1
						topVal = ar[runTop]
						r.drawComps(runTop)
					toptopNode = toptopNode.prev
					
					while runLow <= runTop and lowVal <= toplowNode.val:
						toplowNode.insertValBefore(lowVal)
						runLow +=1
						lowVal = ar[runLow]
						r.drawComps(runLow)
						inserted = True
					toplowNode = toplowNode.next
					
					travel += 1
				
				if travel > travelLimit:
					if inserted and toplowNode != None:
						cutNode = toplowNode
					else:
						cutNode = toptopNode
					node = topEnd
					while node != cutNode:
						ar[arInd] = node.val
						r.drawWrites(arInd)
						node = node.next
						arInd += 1
					topEnd = cutNode
					topEnd.prev=None
				runLow = c
				#print(topEnd.str())
				
		
		runTop = topInd - 1
		topVal = ar[runTop]
		lowVal = ar[runLow]
		r.drawComps(runLow,runTop)
		toptopNode = top
		toplowNode = topEnd
		
		while runLow <= runTop and lowVal < topEnd.val:
			ar[arInd] = lowVal
			r.drawWrites(arInd)
			runLow += 1
			arInd += 1
			if runLow <= runTop:
				lowVal = ar[runLow]
				r.drawComps(runLow)
		
		topInd2 = arInd
		
		while runLow <= runTop:
			while runLow <= runTop and topVal >= toptopNode.val:
				toptopNode.insertValAfter(topVal)
				runTop -= 1
				topVal = ar[runTop]
				r.drawComps(runTop)
			toptopNode = toptopNode.prev
			
			while runLow <= runTop and lowVal <= toplowNode.val:
				toplowNode.insertValBefore(lowVal)
				runLow +=1
				if runLow <= runTop:
					lowVal = ar[runLow]
					r.drawComps(runLow)
			toplowNode = toplowNode.next
		
		node = topEnd
		while node != None:
			ar[arInd] = node.val
			r.drawWrites(arInd)
			node = node.next
			arInd += 1
				
		for c in range(topInd2,topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=topInd2
	
	if topInd == 1:
		r.drawComps(0,1)
		if ar[0] > ar[1]:
			swap(0,1)
	
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	
	print(passes)


class Node():
	next=None
	prev=None
	val=0
	def __init__(self,val=0):
		self.val=val
	
	def insertNodeAfter(self, node):
		node.prev = self
		if self.next!= None:
			node.next = self.next
			self.next.prev = node
		self.next = node
	
	def insertValAfter(self, val):
		self.insertNodeAfter( Node(val) )
		
	def insertNodeBefore(self, node):
		node.next = self
		if self.prev != None:
			node.prev = self.prev
			self.prev.next = node
		self.prev = node
	
	def insertValBefore(self, val):
		self.insertNodeBefore( Node(val) )
	
	def str(self):
		node=self
		s = '['
		while node != None:
			s += str(node.val)
			node = node.next
			if node != None:
				s += ','
		s += ']'
		return s
		
	def strAlt(self):
		node=self
		s = ']'
		while node != None:
			s = str(node.val) + s
			node = node.prev
			if node != None:
				s = ',' + s
		s = '[' + s
		return s
		
def bigbubblemergeSort():
	travelLimitCoeff = 1
	travalLimitMin = 1
	
	global ar
	global listLen
	topInd=listLen
	passes=0
	while topInd > 1:
		sortRunsInversions(topInd)
		passes +=1
		arInd=0
		top=Node(ar[0])
		r.drawComps(0)
		topEnd=top
		runLow=1
		for c in range(2,topInd):
			r.drawComps(c,c-1)
			if ar[c] < ar[c-1]:
				#merge
				runTop = c - 1
				r.drawComps(runLow,runTop)
				topVal = ar[runTop]
				lowVal = ar[runLow]
				travelLimit = c - runLow
				travelLimit *= travelLimitCoeff
				travelLimit += travalLimitMin
				toptopNode = top
				toplowNode = topEnd
				travel=0
				#cutNode = None
				inserted = False
				
				while runLow <= runTop and lowVal < topEnd.val:
					ar[arInd] = lowVal
					r.drawWrites(arInd)
					runLow += 1
					arInd +=1
					lowVal = ar[runLow]
					r.drawComps(runLow)
					
				if runLow <= runTop and topVal >= top.val:
					top.insertValAfter(topVal)
					runTop -= 1
					topVal = ar[runTop]
					r.drawComps(runTop)
					top = top.next
					
					
				while runLow <= runTop:
					
					while runLow <= runTop and topVal >= toptopNode.val:
						toptopNode.insertValAfter(topVal)
						runTop -= 1
						topVal = ar[runTop]
						r.drawComps(runTop)
					toptopNode = toptopNode.prev
					
					while runLow <= runTop and lowVal <= toplowNode.val:
						toplowNode.insertValBefore(lowVal)
						runLow +=1
						lowVal = ar[runLow]
						r.drawComps(runLow)
						inserted = True
					toplowNode = toplowNode.next
					
					travel += 1
				
				if travel > travelLimit:
					if inserted and toplowNode != None:
						cutNode = toplowNode
					else:
						cutNode = toptopNode
					node = topEnd
					while node != cutNode:
						ar[arInd] = node.val
						r.drawWrites(arInd)
						node = node.next
						arInd += 1
					topEnd = cutNode
					topEnd.prev=None
				runLow = c
				#print(topEnd.str())
				
		
		runTop = topInd - 1
		topVal = ar[runTop]
		lowVal = ar[runLow]
		r.drawComps(runLow,runTop)
		toptopNode = top
		toplowNode = topEnd
		
		while runLow <= runTop and lowVal < topEnd.val:
			ar[arInd] = lowVal
			r.drawWrites(arInd)
			runLow += 1
			arInd += 1
			if runLow <= runTop:
				lowVal = ar[runLow]
				r.drawComps(runLow)
		
		topInd2 = arInd
		
		while runLow <= runTop:
			while runLow <= runTop and topVal >= toptopNode.val:
				toptopNode.insertValAfter(topVal)
				runTop -= 1
				topVal = ar[runTop]
				r.drawComps(runTop)
			toptopNode = toptopNode.prev
			
			while runLow <= runTop and lowVal <= toplowNode.val:
				toplowNode.insertValBefore(lowVal)
				runLow +=1
				if runLow <= runTop:
					lowVal = ar[runLow]
					r.drawComps(runLow)
			toplowNode = toplowNode.next
		
		node = topEnd
		while node != None:
			ar[arInd] = node.val
			r.drawWrites(arInd)
			node = node.next
			arInd += 1
				
		for c in range(topInd2,topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=topInd2
	
	if topInd == 1:
		r.drawComps(0,1)
		if ar[0] > ar[1]:
			swap(0,1)
	
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	
	print(passes)

def sortRuns(topInd=-1):
	if topInd == -1:
		topInd = listLen

	runs=[]
	runStart=0
	minRun=listLen
	maxRun=0
	
	for c in range(1,topInd):
		r.drawComps(c,c-1)
		if ar[c] < ar[c-1]:
			run=[]
			for x in range(runStart,c):
				run.append(ar[x])
			runs.append(run)
			size=c-runStart
			if size < minRun:
				minRun = size
			if size > maxRun:
				maxRun = size
			runStart=c
				
	run=[]
	for x in range(runStart,topInd):
		run.append(ar[x])
	runs.append(run)
	size=topInd-runStart
	if size < minRun:
		minRun = size
	if size > maxRun:
		maxRun = size
		
	runRange = maxRun - minRun + 1
	print(str(minRun)+'-'+str(maxRun))
	runs2=list(range(runRange))
	for c in range(len(runs2)):
		runs2[c]=[]

	for c in runs:
		runs2[ len(c) - minRun ].append(c)
	
	for c in range(len(runs2)):
		if len(runs2[c]) > 0:
			print(" "+str(c+minRun) + ':' + str(len(runs2[c])))
			
	i=0
	for x in runs2:
		for y in x:
			for z in y:
				ar[i]=z
				r.drawWrites(i)
				i+=1

def sortRunsInversions(topInd=-1):
	if topInd == -1:
		topInd = listLen

	runs=[]
	runStart=0
	minRun=listLen
	maxRun=0
	norm=True
	
	for c in range(1,topInd):
		r.drawComps(c,c-1)
		if ar[c] < ar[c-1] and norm:
			size=c-runStart
			if size > 1:
				run=[]
				for x in range(runStart,c):
					run.append(ar[x])
				runs.append(run)
				if size < minRun:
					minRun = size
				if size > maxRun:
					maxRun = size
				runStart=c
			else:
				norm=False
		elif ar[c] > ar[c-1] and not norm:
			size=c-runStart
			run=[]
			for x in range(runStart,c):
				run.append(ar[x])
			run.reverse()
			runs.append(run)
			if size < minRun:
				minRun = size
			if size > maxRun:
				maxRun = size
			runStart=c
			norm=True
			
				
	run=[]
	for x in range(runStart,topInd):
		run.append(ar[x])
	if not norm:
		run.reverse()
	runs.append(run)
	size=topInd-runStart
	if size < minRun:
		minRun = size
	if size > maxRun:
		maxRun = size
		
	runRange = maxRun - minRun + 1
	print(str(minRun)+'-'+str(maxRun))
	runs2=list(range(runRange))
	for c in range(len(runs2)):
		runs2[c]=[]

	for c in runs:
		runs2[ len(c) - minRun ].append(c)
		
	for c in range(len(runs2)):
		if len(runs2[c]) > 0:
			print(" "+str(c+minRun) + ':' + str(len(runs2[c])))
	
	i=0
	for x in runs2:
		for y in x:
			for z in y:
				ar[i]=z
				r.drawWrites(i)
				i+=1

#not done
def gigabubbleSort():
	global ar
	global listLen
	topInd=listLen
	while topInd > 0:
		arInd=0
		top=node(ar[0])
		topEnd=top
		tail=None
		tailTop=None
		runLow=1
		for c in range(2,topInd):
			if ar[c] < ar[c-1]:
				#merge
				runTop = c - 1
				topVal = ar[runTop]
				lowVal = ar[runLow]
				travelLimit = c - runLow
				if topVal > topEnd.val:
					if lowVal > topEnd.val:#top only
						toptopNode = top
						toplowNode = topEnd
						travel=0
						cutNode=None
						while runLow <= runTop:
							while runLow <= runTop and topVal >= toptopNode.val:
								toptopNode.insertValAfter(topVal)
								runTop -= 1
								topVal = ar[runTop]
							toptopNode = toptopNode.prev
							
							while runLow <= runTop and lowVal <= toplowNode.val:
								toplowNode.insertValBefore(lowVal)
								runLow +=1
								lowVal = ar[runLow]
							toplowNode = toplowNode.next
							
							travel += 1
							
							if cutNode == None and travel > travelLimit:
								cutNode = toptopNode
								
					else:#top and tail
						pass
				else:#tail only
					pass
				
				
		
		#merge
		#drop
		#complete
		
		topInd-=1


def megacocktailshakersort():
	global ar
	global arAux
	global listLen
	topInd=listLen
	lowInd=0
	while topInd - lowInd > 0:
		auxIndTop=0
		auxIndLow=0
		arAux[0]=ar[lowInd]
		arInd=lowInd
		tailInd=listLen
		
		for c in range(lowInd+1,topInd):
			cVal=ar[c]
			r.drawComps(c)
			if cVal >= arAux[auxIndTop]:#grow bubble
				auxIndTop+=1
				arAux[auxIndTop]=cVal
			elif cVal <= arAux[auxIndLow]:#swap over bubble
				if tailInd == listLen:#no tail
					tailInd -= 1
					arAux[tailInd] = cVal
				elif cVal <= arAux[tailInd]:#append tail
					tailInd -= 1
					arAux[tailInd] = cVal
				elif cVal > arAux[listLen-1]:#front of tail
					#drop tail
					for i in range(tailInd,listLen):
						ar[arInd]=arAux[i]
						r.drawWrites(arInd)
						arInd+=1
					tailInd=listLen-1
					arAux[tailInd] = cVal
				else :#insert tail
					for i in range(tailInd,listLen):
						if cVal <= arAux[tailInd]:
							tailInd-=1
							arAux[tailInd]=cVal
							break
						ar[arInd]=arAux[tailInd]
						r.drawWrites(arInd)
						arInd+=1
						tailInd+=1
			else:#insert into bubble
				#drop tail
				for i in range(tailInd,listLen):
					ar[arInd]=arAux[i]
					r.drawWrites(arInd)
					arInd+=1
				tailInd=listLen
				
				#insert bubble
				for i in range(auxIndLow,auxIndTop+1):
					if cVal <= arAux[i]:
						auxIndLow-=1
						arAux[auxIndLow]=cVal
						break
					ar[arInd]=arAux[i]
					r.drawWrites(arInd)
					arInd+=1
					auxIndLow+=1
		
		#drop tail
		for i in range(tailInd,listLen):
			ar[arInd]=arAux[i]
			r.drawWrites(arInd)
			arInd+=1
		
		topInd2=arInd
		for c in range(auxIndLow,auxIndTop+1):
			ar[arInd]=arAux[c]
			r.drawWrites(arInd)
			arInd+=1
		
		for c in range(topInd2,topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=topInd2
			#print(topInd)
			
		if topInd - lowInd > 0:
			auxIndTop=0
			auxIndLow=0
			arAux[0]=ar[topInd-1]
			arInd=topInd-1
			tailInd=listLen
			
			for c in range(2,topInd-lowInd+1):
				cVal=ar[topInd-c]
				r.drawComps(topInd-c)
				if cVal <= arAux[auxIndTop]:#grow bubble
					auxIndTop+=1
					arAux[auxIndTop]=cVal
				elif cVal >= arAux[auxIndLow]:#swap over bubble
					if tailInd == listLen:#no tail
						tailInd -= 1
						arAux[tailInd] = cVal
					elif cVal >= arAux[tailInd]:#append tail
						tailInd -= 1
						arAux[tailInd] = cVal
					elif cVal < arAux[listLen-1]:#front of tail
						#drop tail
						for i in range(tailInd,listLen):
							ar[arInd]=arAux[i]
							r.drawWrites(arInd)
							arInd-=1
						tailInd=listLen-1
						arAux[tailInd] = cVal
					else :#insert tail
						for i in range(tailInd,listLen):
							if cVal >= arAux[tailInd]:
								tailInd-=1
								arAux[tailInd]=cVal
								break
							ar[arInd]=arAux[tailInd]
							r.drawWrites(arInd)
							arInd-=1
							tailInd+=1
				else:#insert into bubble
					#drop tail
					for i in range(tailInd,listLen):
						ar[arInd]=arAux[i]
						r.drawWrites(arInd)
						arInd-=1
					tailInd=listLen
						
					for i in range(auxIndLow,auxIndTop+1):
						if cVal >= arAux[i]:
							auxIndLow-=1
							arAux[auxIndLow]=cVal
							break
						ar[arInd]=arAux[i]
						r.drawWrites(arInd)
						arInd-=1
						auxIndLow+=1
			
			#drop tail
			for i in range(tailInd,listLen):
				ar[arInd]=arAux[i]
				r.drawWrites(arInd)
				arInd-=1
			
			lowInd2=arInd+1
			for c in range(auxIndLow,auxIndTop+1):
				ar[arInd]=arAux[c]
				r.drawWrites(arInd)
				arInd-=1
			
			for c in range(lowInd,lowInd2):
				r.drawDone(c)
			pygame.display.update()
			lowInd=lowInd2
		
	for c in range(lowInd, topInd+1):
		r.drawDone(c)
	pygame.display.update()
	
def bigcocktailshakersort():
	global ar
	global arAux
	global listLen
	topInd=listLen
	lowInd=0
	while topInd - lowInd > 0:
		auxIndTop=0
		auxIndLow=0
		arAux[0]=ar[lowInd]
		arInd=lowInd
		
		for c in range(lowInd+1,topInd):
			cVal=ar[c]
			r.drawComps(c)
			if cVal >= arAux[auxIndTop]:#grow bubble
				auxIndTop+=1
				arAux[auxIndTop]=cVal
			elif cVal <= arAux[auxIndLow]:#swap over bubble
				ar[arInd]=cVal
				r.drawWrites(arInd)
				arInd+=1
			else:#insert into bubble
				for i in range(auxIndLow,auxIndTop+1):
					if cVal <= arAux[i]:
						auxIndLow-=1
						arAux[auxIndLow]=cVal
						break
					ar[arInd]=arAux[i]
					r.drawWrites(arInd)
					arInd+=1
					auxIndLow+=1
		
		topInd2=arInd
		for c in range(auxIndLow,auxIndTop+1):
			ar[arInd]=arAux[c]
			r.drawWrites(arInd)
			arInd+=1
		
		for c in range(topInd2,topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=topInd2
			#print(topInd)
			
		if topInd - lowInd > 0:
			auxIndTop=0
			auxIndLow=0
			arAux[0]=ar[topInd-1]
			arInd=topInd-1
			for c in range(2,topInd-lowInd+1):
				cVal=ar[topInd-c]
				r.drawComps(topInd-c)
				if cVal <= arAux[auxIndTop]:#grow bubble
					auxIndTop+=1
					arAux[auxIndTop]=cVal
				elif cVal >= arAux[auxIndLow]:#swap over bubble
					ar[arInd]=cVal
					r.drawWrites(arInd)
					arInd-=1
				else:#insert into bubble
					for i in range(auxIndLow,auxIndTop+1):
						if cVal >= arAux[i]:
							auxIndLow-=1
							arAux[auxIndLow]=cVal
							break
						ar[arInd]=arAux[i]
						r.drawWrites(arInd)
						arInd-=1
						auxIndLow+=1
			
			lowInd2=arInd+1
			for c in range(auxIndLow,auxIndTop+1):
				ar[arInd]=arAux[c]
				r.drawWrites(arInd)
				arInd-=1
			
			for c in range(lowInd,lowInd2):
				r.drawDone(c)
			pygame.display.update()
			lowInd=lowInd2
		
	for c in range(lowInd, topInd+1):
		r.drawDone(c)
	pygame.display.update()
	

	
def bubbleExchangeSort():
	global ar
	global listLen
	topInd=listLen-1
	while topInd > 0:
		lastSwap=0
		
		r.drawComps(0,topInd)
		if ar[0] > ar[topInd]:
			swap(0,topInd)
		
		for c in range(topInd-1):
			r.drawComps(c,c+1)
			if ar[c] > ar[c+1]:
				swap(c,c+1)
				lastSwap=c
			else:
				r.drawComps(c+1,topInd)
				if ar[c+1] > ar[topInd]:
					swap(c+1,topInd)
				
		for c in range(lastSwap+1,topInd+1):
			r.drawDone(c)
		pygame.display.update()
		topInd=lastSwap
		
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	
def bubbleExchangePullSort():#sometimes wrong at the end
	global ar
	global listLen
	global arAux
	pullInd=0
	topInd=listLen-1
	lowInd=0
	while topInd > lowInd:
		lastSwap=lowInd
		
		r.drawComps(lowInd,topInd)
		if ar[lowInd] > ar[topInd]:
			swap(lowInd,topInd)
		
		pullInd=0
		for c in range(lowInd,topInd-1):
			r.drawComps(c,c+1)
			if ar[c] > ar[c+1]:
				swap(c,c+1)
				lastSwap=c
			else:
				r.drawComps(c+1,topInd)
				arAux[pullInd]=c
				pullInd+=1
				if ar[c+1] > ar[topInd]:
					swap(c+1,topInd)
				
		for c in range(lastSwap+1,topInd+1):
			r.drawDone(c)
		pygame.display.update()
		skipPulls=topInd-lastSwap-1
		topInd=lastSwap
		
		pullInd-=skipPulls
		if pullInd >=0:
			p=arAux[pullInd]
			for c in range(topInd):
				tc=topInd-c-1
				if tc <= p:
					if p==pullInd+lowInd:
						for i in range(lowInd,p+1):
							r.drawDone(i)
						pygame.display.update()
						lowInd=p+1
						break
					pullInd-=1
					if pullInd < 0:
						break
					p=arAux[pullInd]
				r.drawComps(p,tc)
				if ar[p] > ar[tc]:
					swap(p,tc)
					if pullInd<0:
						break
					pullInd-=1
					p=arAux[pullInd]
		
	for c in range(lowInd, topInd+1):
		r.drawDone(c)
	pygame.display.update()

	
def cocktailShakerSort():
	global ar
	global listLen
	topInd=listLen-1
	lowInd=0
	while topInd - lowInd > 0:
		lastSwap=lowInd
		
		for c in range(lowInd,topInd):
			r.drawComps(c,c+1)
			if ar[c] > ar[c+1]:
				swap(c,c+1)
				lastSwap=c
				
		for c in range(lastSwap+1,topInd+1):
			r.drawDone(c)
		pygame.display.update()
		topInd=lastSwap
		
		if topInd - lowInd > 0:
			lastSwap=topInd
		
			for c in reversed(range(lowInd,topInd)):
				r.drawComps(c,c+1)
				if ar[c] > ar[c+1]:
					swap(c,c+1)
					lastSwap=c+1
					
			for c in range(lowInd,lastSwap+1):
				r.drawDone(c)
			pygame.display.update()
			lowInd=lastSwap
		
	for c in range(lowInd, topInd+1):
		r.drawDone(c)
	pygame.display.update()

def combSort():
	gapFactor=1.3
	
	global ar
	global listLen
	gap=listLen-1
	while gap > 1:
		for c in range(listLen-gap):
			r.drawComps(c,c+gap)
			if ar[c] > ar[c+gap]:
				swap(c,c+gap)
		gap=int(gap/gapFactor)
	bubbleSort()
	
def triswapCombSort():
	gapFactor=1.3
	
	global ar
	global listLen
	gap=listLen-1
	while gap > 1:
		for c in range(listLen-gap-1):
			sort3(c,c+gap,c+gap+1)
		gap=int(gap/gapFactor)
	bubbleSort()
	
def exchangeSort():
	global ar
	global listLen
	for c in range(listLen-1):
		topInd=listLen-c-1
		for i in range(topInd):
			r.drawComps(i,topInd)
			if ar[i] > ar[topInd]:
				swap(i,topInd)
		r.drawDone(topInd)
		pygame.display.update()
	r.drawDone(0)
	pygame.display.update()
				
def gnomeSort():
	global ar
	global listLen
	for c in range(1,listLen):
		for i in range(c):
			r.drawComps(c-i-1,c-i)
			if ar[c-i-1] > ar[c-i]:
				swap(c-i-1, c-i)
			else:
				break
	r.drawDoneAr()
	
def insertionSort(topInd=-1):
	global ar
	global listLen
	if topInd == -1:
		topInd=listLen
	for c in range(1,topInd):
		temp=ar[c]
		endInd=0
		for i in range(c):
			r.drawComps(c-i-1)
			if ar[c-i-1] > temp:
				ar[c-i] = ar[c-i-1]
				r.drawWrites(c-i)
			else:
				endInd=c-i
				break
		ar[endInd] = temp
		r.drawWrites(endInd)
				
	r.drawDoneAr()

def shellsort():
	gapFactor=2.25
	
	global ar
	global listLen
	gap=listLen-1
	while gap > 1:
		for c in range(gap,listLen):
			temp=ar[c]
			endInd=c%gap
			for i in range(int(c/gap)):
				cigap=c-i*gap
				cigapNext=c-(i+1)*gap
				r.drawComps(cigapNext)
				if ar[cigapNext] > temp:
					ar[cigap] = ar[cigapNext]
					r.drawWrites(cigap)
				else:
					endInd=cigap
					break
			ar[endInd] = temp
			r.drawWrites(endInd)
		gap=int(gap/gapFactor)
	insertionSort()

def shellsort2():
	gapFactor=3
	global ar
	global listLen
	gap = 1
	while gap < listLen:
		gap *= gapFactor
	gap = int( gap/gapFactor )
	
	while gap > 1:
		for c in range(gap,listLen):
			temp=ar[c]
			endInd=c%gap
			for i in range(int(c/gap)):
				cigap=c-i*gap
				cigapNext=c-(i+1)*gap
				r.drawComps(cigapNext)
				if ar[cigapNext] > temp:
					ar[cigap] = ar[cigapNext]
					r.drawWrites(cigap)
				else:
					endInd=cigap
					break
			ar[endInd] = temp
			r.drawWrites(endInd)
		gap = int( gap/gapFactor )
	insertionSort()

def shellsort23():
	global ar
	global listLen
	gap = 1
	while gap < listLen:
		gap *= 6
	gap = int( gap/6 )
	turn=False
	if gap*4 < listLen:
		gap *= 4
	elif gap*3 < listLen:
		gap *= 3
		turn=True
	elif gap*2 < listLen:
		gap *= 2
	
	while gap > 1:
		for c in range(gap,listLen):
			temp=ar[c]
			endInd=c%gap
			for i in range(int(c/gap)):
				cigap=c-i*gap
				cigapNext=c-(i+1)*gap
				r.drawComps(cigapNext)
				if ar[cigapNext] > temp:
					ar[cigap] = ar[cigapNext]
					r.drawWrites(cigap)
				else:
					endInd=cigap
					break
			ar[endInd] = temp
			r.drawWrites(endInd)
		if turn:
			gap = int( gap/3 )
		else:
			gap = int( gap/2 )
		turn = not turn
	insertionSort()
	
def bigbubbleShellsort():
	global ar
	global arAux
	global listLen
	topInd=listLen
	
	gapFactor=2.25
	gap=int(listLen/gapFactor)
	
	while topInd > 0:
		auxIndTop=0
		auxIndLow=0
		arAux[0]=ar[0]
		arInd=0
		
		for c in range(1,topInd):
			cVal=ar[c]
			r.drawComps(c)
			if cVal >= arAux[auxIndTop]:#grow bubble
				auxIndTop+=1
				arAux[auxIndTop]=cVal
			elif cVal <= arAux[auxIndLow]:#swap over bubble
				endInd=arInd%gap
				for i in range(int(arInd/gap)):
					cigap=arInd-i*gap
					cigapNext=arInd-(i+1)*gap
					r.drawComps(cigapNext)
					if ar[cigapNext] > cVal:
						ar[cigap] = ar[cigapNext]
						r.drawWrites(cigap)
					else:
						endInd=cigap
						break
				ar[endInd] = cVal
				r.drawWrites(endInd)
				arInd+=1
				
			else:#insert into bubble
				for i in range(auxIndLow,auxIndTop+1):
					if cVal <= arAux[i]:
						auxIndLow-=1
						arAux[auxIndLow]=cVal
						break
					ar[arInd]=arAux[i]
					r.drawWrites(arInd)
					arInd+=1
					auxIndLow+=1
		
		topInd2=arInd
		for c in range(auxIndLow,auxIndTop+1):
			ar[arInd]=arAux[c]
			r.drawWrites(arInd)
			arInd+=1
		
		for c in range(topInd2,topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=topInd2
		gap=int(gap/gapFactor)
		maxGap=int(topInd/gapFactor)
		if maxGap < gap:
			gap=maxGap
		
		if gap <= 1:
			insertionSort(topInd)
			return
		
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	
def megabubbleShellsort():
	global ar
	global arAux
	global listLen
	topInd=listLen
	gapFactor=2.25
	gap=int(listLen/gapFactor)
	while topInd > 0:
		auxIndTop=0
		auxIndLow=0
		arAux[0]=ar[0]
		arInd=0
		tailInd=listLen
		
		for c in range(1,topInd):
			cVal=ar[c]
			r.drawComps(c)
			if cVal >= arAux[auxIndTop]:#grow bubble
				auxIndTop+=1
				arAux[auxIndTop]=cVal
			elif cVal <= arAux[auxIndLow]:#grow tail
				if tailInd == listLen:#no tail
					tailInd -= 1
					arAux[tailInd] = cVal
				elif cVal <= arAux[tailInd]:#append tail
					tailInd -= 1
					arAux[tailInd] = cVal
				elif cVal > arAux[listLen-1]:#front of tail
					#drop tail
					for i in range(tailInd,listLen):
						endInd=arInd%gap
						tVal=arAux[i]
						for t in range(int(arInd/gap)):
							cigap=arInd-t*gap
							cigapNext=arInd-(t+1)*gap
							r.drawComps(cigapNext)
							if ar[cigapNext] > tVal:
								ar[cigap] = ar[cigapNext]
								r.drawWrites(cigap)
							else:
								endInd=cigap
								break
						ar[endInd] = tVal
						r.drawWrites(endInd)
						arInd+=1
						
					tailInd=listLen-1
					arAux[tailInd] = cVal
				else :#insert tail
					for i in range(tailInd,listLen):
						if cVal <= arAux[tailInd]:
							tailInd-=1
							arAux[tailInd]=cVal
							break
						endInd=arInd%gap
						tVal=arAux[i]
						for t in range(int(arInd/gap)):
							cigap=arInd-t*gap
							cigapNext=arInd-(t+1)*gap
							r.drawComps(cigapNext)
							if ar[cigapNext] > tVal:
								ar[cigap] = ar[cigapNext]
								r.drawWrites(cigap)
							else:
								endInd=cigap
								break
						ar[endInd] = tVal
						r.drawWrites(endInd)
						arInd+=1
						tailInd+=1
			else:#insert into bubble
				#drop tail
				for i in range(tailInd,listLen):
					endInd=arInd%gap
					tVal=arAux[i]
					for t in range(int(arInd/gap)):
						cigap=arInd-t*gap
						cigapNext=arInd-(t+1)*gap
						r.drawComps(cigapNext)
						if ar[cigapNext] > tVal:
							ar[cigap] = ar[cigapNext]
							r.drawWrites(cigap)
						else:
							endInd=cigap
							break
					ar[endInd] = tVal
					r.drawWrites(endInd)
					arInd+=1
					
				tailInd=listLen
				
				#insert bubble
				for i in range(auxIndLow,auxIndTop+1):
					if cVal <= arAux[i]:
						auxIndLow-=1
						arAux[auxIndLow]=cVal
						break
					ar[arInd]=arAux[i]
					r.drawWrites(arInd)
					arInd+=1
					auxIndLow+=1
		
		#drop tail
		for i in range(tailInd,listLen):
			endInd=arInd%gap
			tVal=arAux[i]
			for t in range(int(arInd/gap)):
				cigap=arInd-t*gap
				cigapNext=arInd-(t+1)*gap
				r.drawComps(cigapNext)
				if ar[cigapNext] > tVal:
					ar[cigap] = ar[cigapNext]
					r.drawWrites(cigap)
				else:
					endInd=cigap
					break
			ar[endInd] = tVal
			r.drawWrites(endInd)
			arInd+=1
		
		topInd2=arInd
		for c in range(auxIndLow,auxIndTop+1):
			ar[arInd]=arAux[c]
			r.drawWrites(arInd)
			arInd+=1
		
		for c in range(topInd2,topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=topInd2
		gap=int(gap/gapFactor)
		maxGap=int(topInd/gapFactor)
		if maxGap < gap:
			gap=maxGap
		
		if gap <= 1:
			insertionSort(topInd)
			return
		
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	
def bubbleShellsort():
	gapFactor=2.25
	
	global ar
	global listLen
	gap=int(listLen/gapFactor)
	topInd=listLen
	while gap > 1:
		lastSwap=0
		for c in range(0,topInd-1):
			temp=ar[c+1]
			r.drawComps(c,c+1)
			if temp < ar[c]:
				lastSwap=c+1
				ar[c+1]=ar[c]
				r.drawWrites(c+1)
				endInd=c%gap
				for i in range(int(c/gap)):
					cigap=c-i*gap
					cigapNext=c-(i+1)*gap
					r.drawComps(cigapNext)
					if ar[cigapNext] > temp:
						ar[cigap] = ar[cigapNext]
						r.drawWrites(cigap)
					else:
						endInd=cigap
						break
				ar[endInd] = temp
				r.drawWrites(endInd)
		for c in range(lastSwap, topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=lastSwap
		gap=int(gap/gapFactor)
		maxGap=int(topInd/gapFactor)
		if maxGap < gap:
			gap=maxGap
	insertionSort(topInd)#pending stop at topInd optimization
	
def bubbleExchangeShellsort():
	gapFactor=2.25
	
	global ar
	global listLen
	gap=int(listLen/gapFactor)
	topInd=listLen
	while gap > 1:
		lastSwap=0
		r.drawComps(0,topInd-1)
		if ar[0] > ar[topInd-1]:
			swap(0,topInd-1)
		for c in range(0,topInd-2):
			temp=ar[c+1]
			r.drawComps(c,c+1)
			if temp < ar[c]:
				lastSwap=c+1
				ar[c+1]=ar[c]
				r.drawWrites(c+1)
				endInd=c%gap
				for i in range(int(c/gap)):
					cigap=c-i*gap
					cigapNext=c-(i+1)*gap
					r.drawComps(cigapNext)
					if ar[cigapNext] > temp:
						ar[cigap] = ar[cigapNext]
						r.drawWrites(cigap)
					else:
						endInd=cigap
						break
				ar[endInd] = temp
				r.drawWrites(endInd)
			else:
				r.drawComps(c+1,topInd-1)
				if ar[c+1] > ar[topInd-1]:
					swap(c+1,topInd-1)
		for c in range(lastSwap, topInd):
			r.drawDone(c)
		pygame.display.update()
		topInd=lastSwap
		gap=int(gap/gapFactor)
		maxGap=int(topInd/gapFactor)
		if maxGap < gap:
			gap=maxGap
	insertionSort(topInd)#pending stop at topInd optimization
		


def selectionSort():
	global ar
	global listLen
	for c in range(listLen-1):
		lowInd=c
		for i in range(c+1,listLen):
			r.drawComps(lowInd,i)
			if ar[lowInd] > ar[i]:
				lowInd=i
		swap(c,lowInd)
		r.drawDone(c)
		pygame.display.update()
	r.drawDone(listLen-1)
	pygame.display.update()
	
def flipSort():
	global ar
	global listLen
	global arAux
	for c in range(listLen-1):
		arAux[0]=c
		auxInd=0
		for i in range(c+1,listLen):
			lowInd=arAux[auxInd]
			r.drawComps(lowInd,i)
			if ar[lowInd] > ar[i]:
				auxInd+=1
				arAux[auxInd]=i
		for i in range(int((auxInd+1)/2)):
			swap(arAux[i],arAux[auxInd-i])
		r.drawDone(c)
		pygame.display.update()
	r.drawDone(listLen-1)
	pygame.display.update()
	
def flipPushSort():#unfinished
	global ar
	global listLen
	global arAux
	for c in range(listLen-1):
		arPushMin=ar[c]
		arAux[0]=c
		auxInd=0
		for i in range(c+1,listLen):
			lowInd=arAux[auxInd]
			r.drawComps(lowInd,i)
			if ar[lowInd] > ar[i]:
				auxInd+=1
				arAux[auxInd]=i
				
		
		for i in range(int((auxInd+1)/2)):
			swap(arAux[i],arAux[auxInd-i])
		r.drawDone(c)
		
		#push
		auxInd2=0
		auxSkip=0
		pushInd=0
		avInd=0
		for i in range(c+1,arAux[auxInd]):
			if i == auxInd2:
				ar[i]=ar[arAux[auxInd2+auxSkip]]
				r.drawWrites(i)
				auxInd2+=1
			else:
				isAvInd=pushInd>avInd
				if isAvInd:
					isAvInd=i==arAux[listLen-1-avInd]
				if isAvInd:
					ar[i]=ar[arAux[auxInd2+auxSkip]]
					r.drawWrites(i)
					auxInd2+=1
					auxSkip+=1
				else:
					r.drawComps(i)
					if ar[i] > arPushMin:
						arAux[pushInd]=ar[i]
						pushInd-=1
						if auxInd == auxInd2+auxSkip:
							break
		ar[arAux[auxInd2]]=ar[arAux[auxInd]]
		for i in range(pushInd,listLen):
			ar[arAux[auxInd2]]=0
		
		pygame.display.update()
	r.drawDone(listLen-1)
	pygame.display.update()
	
	
def bubbleFlipSort():
	global ar
	global listLen
	global arAux
	topInd=listLen-1
	lowerInd=0;
	while topInd - lowerInd > 0:
		lastSwap=0
		arAux[0]=lowerInd
		auxInd=0
		
		r.drawComps(lowerInd,topInd)
		if ar[lowerInd] > ar[topInd]:
			swap(lowerInd,topInd)
		
		r.drawComps(lowerInd,lowerInd+1)
		if ar[lowerInd] > ar[lowerInd+1]:
			swap(lowerInd,lowerInd+1)
		
		for c in range(lowerInd+1,topInd):
			r.drawComps(c,c+1)
			if ar[c] > ar[c+1]:
				swap(c,c+1)
				lastSwap=c
				
				lowInd=arAux[auxInd]
				r.drawComps(lowInd,c)
				if ar[lowInd] > ar[c]:
					auxInd+=1
					arAux[auxInd]=c
					
		for i in range(int((auxInd+1)/2)):
			swap(arAux[i],arAux[auxInd-i])
		r.drawDone(lowerInd)
				
		for c in range(lastSwap+1,topInd+1):
			r.drawDone(c)
		pygame.display.update()
		topInd=lastSwap
		lowerInd+=1
		
	for c in range(topInd+1):
		r.drawDone(c)
	pygame.display.update()
	

def bubbleFlipExchangeSort():
	global ar
	global listLen
	global arAux
	topInd=listLen-1
	lowerInd=0;
	while topInd - lowerInd > 0:
		arAux[0]=lowerInd
		auxInd=0
		lastSwap=0
		
		'''
		r.drawComps(lowerInd,topInd)
		if ar[lowerInd] > ar[topInd]:
			swap(lowerInd,topInd)
			
		r.drawComps(lowerInd+1,topInd)
		if ar[lowerInd+1] > ar[topInd]:
			swap(lowerInd+1,topInd)
			
		r.drawComps(lowerInd,lowerInd+1)
		if ar[lowerInd] > ar[lowerInd+1]:
			swap(lowerInd,lowerInd+1)
		#'''
		
		sort3(lowerInd,lowerInd+1,topInd)
			
		
		for i in range(lowerInd+1,topInd-1):
			r.drawComps(i,i+1)
			if ar[i] > ar[i+1]:
				swap(i,i+1)
				lastSwap=i
				
				lowInd=arAux[auxInd]
				r.drawComps(lowInd,i)
				if ar[lowInd] > ar[i]:
					auxInd+=1
					arAux[auxInd]=i
			else:
				r.drawComps(i+1,topInd)
				if ar[i+1] > ar[topInd]:
					swap(i+1,topInd)
		for i in range(int((auxInd+1)/2)):
			swap(arAux[i],arAux[auxInd-i])
		r.drawDone(lowerInd)
		for i in range(lastSwap+1,topInd+1):
			r.drawDone(i)
		pygame.display.update()
		topInd=lastSwap
		lowerInd+=1
	
def flipExchangeSort():
	global ar
	global listLen
	global arAux
	for c in range(int(listLen/2)):
		arAux[0]=c
		auxInd=0
		topInd=listLen-c-1
		
		r.drawComps(c,topInd)
		if ar[c] > ar[topInd]:
			swap(c,topInd)
		
		for i in range(c+1,topInd):
			lowInd=arAux[auxInd]
			r.drawComps(lowInd,i)
			if ar[lowInd] > ar[i]:
				auxInd+=1
				arAux[auxInd]=i
			else:
				r.drawComps(i,topInd)
				if ar[i] > ar[topInd]:
					swap(i,topInd)
		for i in range(int((auxInd+1)/2)):
			swap(arAux[i],arAux[auxInd-i])
		r.drawDone(c)
		r.drawDone(topInd)
		pygame.display.update()
		
	if listLen % 2 == 1:
		r.drawDone(int(listLen / 2))
		pygame.display.update()
		
	
			
	
def doubleSelectionSort():
	global ar
	global listLen
	upperInd=listLen-1
	for c in range(int(listLen/2)):
		
		lowInd=c
		topInd=upperInd
		r.drawComps(lowInd,topInd)
		if ar[lowInd] > ar[topInd]:
			swap(lowInd,topInd)
		
		for i in range(c+1,upperInd):
			r.drawComps(lowInd,i)
			if ar[lowInd] > ar[i]:
				lowInd=i
			else:
				r.drawComps(topInd,i)
				if ar[topInd] < ar[i]:
					topInd=i
		swap(c,lowInd)
		swap(upperInd,topInd)
		r.drawDone(c)
		r.drawDone(upperInd)
		pygame.display.update()
		upperInd-=1
	if listLen % 2 == 1:
		r.drawDone(int(listLen / 2))
		pygame.display.update()
		
