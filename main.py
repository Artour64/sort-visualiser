import pygame

import config as co
import render as r
import sort as s

listLen=co.listLen
ar=list(range(listLen));

r.ar=ar
s.ar=ar

r.drawAr()
pygame.time.wait(1000)

s.shuffle()

#pygame.time.wait(500)
#s.randSortSwaps(200)

#s.minishuffle(20)
#s.minishuffle(100)
#s.minishuffle(1000)
#s.reverse()

pygame.time.wait(1000)

#s.sortRuns()
#s.sortRunsInversions()
#pygame.time.wait(1000)
#pygame.display.update()

#s.selectionSort()
#s.doubleSelectionSort()

#s.flipSort()
#s.flipExchangeSort()
#s.bubbleFlipSort()
#s.bubbleFlipExchangeSort()

#s.bubbleSort()
#s.tribubbleSort()
#s.bigbubblesort()
#s.bigbubblemergeSort()
#s.megabubblesort()
#s.gigabubbleSort()
#s.megacocktailshakersort()
#s.bubbleExchangeSort()
#s.bubbleExchangePullSort()
#s.cocktailShakerSort()
#s.bigcocktailshakersort()
#s.exchangeSort()
#s.gnomeSort()

#s.insertionSort()

s.shellsort()
#s.shellsort2()
#s.shellsort23()
#s.bubbleShellsort()
#s.bubbleExchangeShellsort()
#s.bigbubbleShellsort()
#s.megabubbleShellsort()
#s.combSort()
#s.triswapCombSort()

print("done")

if co.stay:
	import events as ev
	while ev.running:
		for event in pygame.event.get():
			ev.event(event)
