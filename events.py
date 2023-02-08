import pygame
running=True

def event(event):
	if event.type == pygame.QUIT:
		global running
		running = False
	# key control
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:#regen map
			pass
		elif event.key == pygame.K_RETURN:
			pass
		
	#if event.type == pygame.KEYUP:
	#	pass
		
		#if event.key == pygame.K_LEFT:
		#	print("Left key released")
		#elif event.key == pygame.K_RIGHT:
		#	print("Right key released")
