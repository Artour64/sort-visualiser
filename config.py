
preset = 0
preset = 3
#preset = 6

presets = [
	[0,2000,1],#	0
	[0,1000,2],#	1
	[0,500,4],#		2
	[0,200,8],#		3
	[10,100,16],#	4
	[20,50,32],#	5
	[100,20,64]#		6
]

preset = presets[preset]

delay = preset[0]
listLen = preset[1]
tileSize = preset[2]

#delay=10
#listLen=9
#tileSize=64

vis=True;
#vis=False;#not working properly

stay=True
stay=False
