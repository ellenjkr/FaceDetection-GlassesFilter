import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys

def defineOculos(numeroOculos):
	if numeroOculos == '1':
		oculos = pygame.image.load(r'images/hp.png')
		oculosX = -67
		oculosY = -72

	elif numeroOculos == '2':
		oculos = pygame.image.load(r'images/classic.png')
		oculosX = -65
		oculosY = -50

	elif numeroOculos == '3':
		oculos = pygame.image.load(r'images/thug.png')
		oculosX = -70
		oculosY = -29

	return oculos, oculosX, oculosY

def detectaOlhos(rosto, olhos, oculosX, oculosY):

	for x, y, w, h in rosto:
		xRosto = x
	try:
		for x, y, w, h in olhos:
			#cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
			if x - xRosto > 70:
				posX = 640 - x + oculosX
				posY = y + h + oculosY
				return posX, posY
	except:
		pass


def main(numeroOculos):

	oculos, oculosX, oculosY = defineOculos(numeroOculos)

	camera = cv2.VideoCapture(0)
	pygame.init()
	pygame.display.set_caption("Trabalho Algoritmos II")
	janela = pygame.display.set_mode((640, 480))

	try:
		while True:

			rosto_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
			olho_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

			ret, frame = camera.read()
			cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			rosto = rosto_cascade.detectMultiScale(cinza, 1.1, 4)
			olhos = olho_cascade.detectMultiScale(cinza, 1.1, 4)

			try:
				posX, posY = detectaOlhos(rosto, olhos, oculosX, oculosY)
			except:
				pass

			frame = np.rot90(frame)
			frame = pygame.surfarray.make_surface(frame)
			janela.blit(frame, (0,0))

			try:
				if len(olhos) == 2:
					janela.blit(oculos, (posX, posY))
			except:
				pass

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == KEYDOWN or event.type ==  QUIT:
					sys.exit(0)
	except (KeyboardInterrupt,SystemExit):
		pygame.quit()
		cv2.destroyAllWindows()