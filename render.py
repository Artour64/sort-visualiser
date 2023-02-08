import pygame

import config as co

delay=co.delay

vis=co.vis
#vis=False;

tileSize=co.tileSize

listLen=co.listLen

xGridTotal=listLen*tileSize
yGridTotal=listLen*tileSize

screenX=xGridTotal#+sizebarright+sizebarleft
screenY=yGridTotal#+sizebartop+sizebarbottom

screen=pygame.display.set_mode((screenX, screenY))

arVis=list(range(listLen));
for c in range(listLen):
	arVis[c]=-1

blcolor=(0, 0, 0)
clrgrey=(110, 110, 110)
clrwhite=(255, 255, 255)
clrred=(255, 0, 0)
clrgreen=(0, 255, 0)
clrblue=(0, 0, 255)


compAr=[]
writeAr=[]
	
def drawClear():
	global compAr
	global writeAr
	for c in compAr:
		drawEl(c,True)
	compAr=[]
	for c in writeAr:
		drawEl(c,True)
	writeAr=[]
		
def drawWrites(*indexes):
	drawClear()
	for i in indexes:
		drawWrite(i)
	pygame.display.update()
	pygame.time.wait(delay)

def drawWrite(index):
	global ar
	global writeAr
	drawEl(index,True)
	pygame.draw.rect(
		screen,
		clrred,
		pygame.Rect(
			tileSize*index,
			screenY-tileSize*(ar[index]+1),
			tileSize,
			tileSize*(ar[index]+1)
		)
	)
	writeAr.append(index)

def drawComps(*indexes):
	drawClear()
	for i in indexes:
		drawComp(i)
	pygame.display.update()
	pygame.time.wait(delay)

def drawComp(index):
	global ar
	global compAr
	drawEl(index,True)
	pygame.draw.rect(
		screen,
		clrblue,
		pygame.Rect(
			tileSize*index,
			screenY-tileSize*(ar[index]+1),
			tileSize,
			tileSize*(ar[index]+1)
		)
	)
	compAr.append(index)

def drawAux(*indexes):
	drawClear()
	print(indexes)
	for i in indexes:
		drawAuxEl(i)
	pygame.display.update()
	pygame.time.wait(delay)
	
def drawAuxAr(indexes):
	drawClear()
	print(indexes)
	for i in indexes:
		drawAuxEl(i)
	pygame.display.update()
	pygame.time.wait(delay)
	
def drawAuxEl(index):
	global ar
	global compAr
	drawEl(index,True)
	pygame.draw.rect(
		screen,
		clrgrey,
		pygame.Rect(
			tileSize*index,
			screenY-tileSize*(ar[index]+1),
			tileSize,
			tileSize*(ar[index]+1)
		)
	)
	compAr.append(index)

def drawEl(index,force=False):
	global vis
	if not vis:
		return
	global ar
	global arVis
	if ar[index] != arVis[index] or force:
		if arVis[index] == -1 or force:
			pygame.draw.rect(
				screen,
				clrwhite,
				pygame.Rect(
					tileSize*index,
					screenY-tileSize*(ar[index]+1),
					tileSize,
					tileSize*(ar[index]+1)
				)
			)
			pygame.draw.rect(
				screen,
				blcolor,
				pygame.Rect(
					tileSize*index,
					0,
					tileSize,
					screenY-tileSize*(ar[index]+1)
				)
			)
		elif ar[index] > arVis[index]:
			pygame.draw.rect(
				screen,
				clrwhite,
				pygame.Rect(
					tileSize*index,
					screenY-tileSize*(ar[index]+1),
					tileSize,
					tileSize*(ar[index]+1)
				)
			)
		elif ar[index] < arVis[index]:
			pygame.draw.rect(
				screen,
				blcolor,
				pygame.Rect(
					tileSize*index,
					0,
					tileSize,
					screenY-tileSize*(ar[index]+1)
				)
			)
		arVis[index]=ar[index]
	
def drawDone(index):
	drawClear()
	global vis
	if not vis:
		return
	global ar
	pygame.draw.rect(
		screen,
		clrgreen,
		pygame.Rect(
			tileSize*index,
			screenY-tileSize*(ar[index]+1),
			tileSize,
			tileSize*(ar[index]+1)
		)
	)
	
def drawAr():
	global ar
	global listLen
	for c in range(listLen):
		drawEl(c,True)
	pygame.display.update()
	
def drawDoneAr():
	global ar
	global listLen
	for c in range(listLen):
		drawDone(c)
	pygame.display.update()
