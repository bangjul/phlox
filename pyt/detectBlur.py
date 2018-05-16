import cv2
import numpy as np
from matplotlib import pyplot as plt

class Preprocessing(object):
	"""docstring for preprocessing"""
	def __init__(self):
		super(Preprocessing, self)

	def readImages(self,filename):
	    img = cv2.imread('project/static/public/images/test/' + filename)
	    return img

	def resize(self,img):
		newHeight = 720
		newWidth = 1280
		reImg = cv2.resize(img,(newWidth, newHeight))
		cv2.imwrite('project/static/public/images/test/resize.png',reImg)
		return reImg

	def filterGray(self,img):
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# cv2.imwrite('hasil/hasilgray.jpg',gray)
		return gray

	def filterGaus(self,img):
		blur = cv2.GaussianBlur(img,(3,3),3)
		# cv2.imwrite('hasil/gasuusian.jpg',blur)
		return blur

	def sobel(self,blur):
		scale = 1
		delta = 0
		ddepth = cv2.CV_16S
		# Gradient-X
		grad_xA = cv2.Sobel(blur,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
		#grad_x = cv2.Scharr(gray,ddepth,1,0)
		# Gradient-Y
		# cv2.imwrite('hasil/sobelx.jpg',grad_xA)
		grad_yA = cv2.Sobel(blur,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
		#grad_y = cv2.Scharr(gray,ddepth,0,1)
		# cv2.imwrite('hasil/sobely.jpg',grad_yA)
		abs_grad_xA = cv2.convertScaleAbs(grad_xA)   # converting back to uint8
		abs_grad_yA = cv2.convertScaleAbs(grad_yA)

		dst = cv2.addWeighted(abs_grad_xA,0.5,abs_grad_yA,0.5,0)
		# cv2.imwrite('hasil/hasilsobel.jpg',dst)
		return dst

	def blurDetection(self, dst, height, width):
		# tes = np.array([
		# 	[1,4,6],
		# 	[2,5,2],
		# 	[8,2,7],
		# 	[1,8,9]])
		tes = np.matrix(dst.copy())
		tesImage = dst.copy()
		mak = tes.max()
		makx, maky = np.unravel_index(np.argmax(tes, axis=None), tes.shape)
		
		posBlury, posBlurx = np.where(tes > 30)
		posBlurKiri = np.min(posBlurx)
		posBlurKanan = np.max(posBlurx)
		
		posMaky, posMakx = np.where(tes > mak-20)
		posMakKiri = np.min(posMakx)
		posMakKanan = np.max(posMakx)

		for x in range(0,width):
			if x == posBlurKiri:
				for y in range(0,height):
					tesImage[y][x] = 255
			elif x == posMakKiri:
				for y in range(0,height):
					tesImage[y][x] = 255
			elif x == posMakKanan:
				for y in range(0,height):
					tesImage[y][x] = 255
			elif x == posBlurKanan:
				for y in range(0,height):
					tesImage[y][x] = 255
		cv2.imwrite('project/static/public/images/test/hasil.png',tesImage)

		lengthBlurKiri = posMakKiri - posBlurKiri
		lengthBlurKanan = posBlurKanan - posMakKanan
		if lengthBlurKiri > lengthBlurKanan:
			return lengthBlurKanan
		if lengthBlurKiri == lengthBlurKanan:
			return lengthBlurKiri
		else:
			return lengthBlurKiri

		

		#lawas---------------- 

		# cv2.imwrite('static/public/images/hasil/hasil.png',tes)
		# return lengthBlurKanan
		
		# ---manual
		
		# tes = dst.copy()
		# nilaiMax = 0
		# mak = 0
		# for x in range(0,width):
		# 	for y in range(0,height):
		# 		mak = tes[y][x]
		# 		if nilaiMax < mak:
		# 			nilaiMax = mak
		# # print ("nilai maksimal = " + str(nilaiMax))
		# return nilaiMax

		# # kiri ke kanan
		# cek = 0
		# cek2 = 0
		# global plotB, plotA
		# for x in range(0,width):
		# 	for y in range(0,height):
		# 		if cek2 == 0:
		# 			if tes[y][x] in range(20, nilaiMax):
		# 				# print ("posisi blur = " + str(x))
		# 				plotA = x
		# 				for z in range(0, height):
		# 					tes[z][x] = 255
		# 				cek2 = 10
		# 				break
		# 			if cek2 == 10:
		# 				break
		# 		if tes[y][x] in range(nilaiMax-30, nilaiMax):
		# 			# print ("posisi objek = " + str(x))
		# 			plotB = x
		# 			for z in range(0, height):
		# 				tes[z][x] = 255
		# 			cek = 1
		# 			break
		# 		if cek == 1:
		# 			break

		# lengthBlur = plotB - plotA
		# return plotA
		# print ("----------panjang blur kiri = " + str(lengthBlur))

		# kanan ke kiri
		# cek = 0
		# cek2 = 0
		# global plotC, plotD
		# for x in range(width-1,0,-1):
		# 	for y in range(0,height):
		# 		if cek2 == 0:
		# 			if tes[y][x] in range(20, nilaiMax):
		# 				# print ("posisi blur = " + str(x))
		# 				plotC = x
		# 				for z in range(0, height):
		# 					tes[z][x] = 255
		# 				cek2 = 10
		# 				break
		# 			if cek2 == 10:
		# 				break
		# 		if tes[y][x] in range(nilaiMax-30, nilaiMax):
		# 			# print ("posisi objek = " + str(x))
		# 			plotD = x
		# 			for z in range(0, height):
		# 				tes[z][x] = 255
		# 			cek = 1
		# 			break
		# 		if cek == 1:
		# 			break

		# lengthBlur2 = plotC - plotD
		# print ("----------panjang blur kanan = " + str(lengthBlur2))

		# if (lengthBlur > lengthBlur2):
		# 	panjangBlurFinal = lengthBlur
		# else:
		# 	panjangBlurFinal = lengthBlur2

		# print ("----------blur terpanjang = " + str(panjangBlurFinal))
		# return tes
		# cv2.imwrite('static/public/images/hasil/hasil.png',tes)
		# return panjangBlurFinal
		# -----------------------------------------------------

	def show(blur, dst, tes):
		plt.subplot(131), plt.imshow(blur, 'gray')
		plt.subplot(132), plt.imshow(dst, 'gray')
		plt.subplot(133), plt.imshow(tes, 'gray')

		plt.show()

