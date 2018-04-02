import cv2
import numpy as np
from matplotlib import pyplot as plt


scale = 1
delta = 0
ddepth = cv2.CV_16S


img = cv2.imread('TestImages/tes2.jpg')
img2 = cv2.imread('TestImages/gaussian2.jpg')


height = np.size(img, 0)
width = np.size(img, 1)
height2 = np.size(img2, 0)
width2 = np.size(img2, 1)

# print (height)
# print (width)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(3,3),3)
blur2 = cv2.GaussianBlur(gray2,(3,3),3)
# blur2 = cv2.blur(gray,(5,5))
# blur3 = cv2.blur(gray,(7,7))
# blur4 = cv2.blur(gray,(9,9))
# blur5 = cv2.blur(gray,(11,11))


# sobel detection -----------------------------------

# Gradient-X
grad_xA = cv2.Sobel(blur,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
#grad_x = cv2.Scharr(gray,ddepth,1,0)
# Gradient-Y
grad_yA = cv2.Sobel(blur,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
#grad_y = cv2.Scharr(gray,ddepth,0,1)
abs_grad_xA = cv2.convertScaleAbs(grad_xA)   # converting back to uint8
abs_grad_yA = cv2.convertScaleAbs(grad_yA)

# Gradient-X
grad_xB = cv2.Sobel(blur2,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
#grad_x = cv2.Scharr(gray,ddepth,1,0)
# Gradient-Y
grad_yB = cv2.Sobel(blur2,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
#grad_y = cv2.Scharr(gray,ddepth,0,1)
abs_grad_xB = cv2.convertScaleAbs(grad_xB)   # converting back to uint8
abs_grad_yB = cv2.convertScaleAbs(grad_yB)

# # Gradient-X
# grad_xC = cv2.Sobel(blur3,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
# #grad_x = cv2.Scharr(gray,ddepth,1,0)
# # Gradient-Y
# grad_yC = cv2.Sobel(blur3,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
# #grad_y = cv2.Scharr(gray,ddepth,0,1)
# abs_grad_xC = cv2.convertScaleAbs(grad_xC)   # converting back to uint8
# abs_grad_yC = cv2.convertScaleAbs(grad_yC)

# # Gradient-X
# grad_xD = cv2.Sobel(blur4,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
# #grad_x = cv2.Scharr(gray,ddepth,1,0)
# # Gradient-Y
# grad_yD = cv2.Sobel(blur4,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
# #grad_y = cv2.Scharr(gray,ddepth,0,1)
# abs_grad_xD = cv2.convertScaleAbs(grad_xD)   # converting back to uint8
# abs_grad_yD = cv2.convertScaleAbs(grad_yD)

# # Gradient-X
# grad_xE = cv2.Sobel(blur5,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
# #grad_x = cv2.Scharr(gray,ddepth,1,0)
# # Gradient-Y
# grad_yE = cv2.Sobel(blur5,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
# #grad_y = cv2.Scharr(gray,ddepth,0,1)
# abs_grad_xE = cv2.convertScaleAbs(grad_xE)   # converting back to uint8
# abs_grad_yE = cv2.convertScaleAbs(grad_yE)



dst = cv2.addWeighted(abs_grad_xA,0.5,abs_grad_yA,0.5,0)
dst2 = cv2.addWeighted(abs_grad_xB,0.5,abs_grad_yB,0.5,0)
tes = dst.copy()
tes2 = dst2.copy()

nilaiMax = 0
mak = 0
for x in range(0,width):
	for y in range(0,height):
		mak = tes[y][x]
		if nilaiMax < mak:
			nilaiMax = mak
print ("nilai maksimal = " + str(nilaiMax))

# kiri ke kanan
cek = 0
for x in range(0,width):
	for y in range(0,height):
		if tes[y][x] in range(nilaiMax-10, nilaiMax):
			print ("posisi plot 1 = " + str(x))
			plotA = x
			for z in range(0, height):
				tes[z][x] = 255
			cek = 1
			break
		if cek == 1:
			break

cek = 0
for x in range(0,width):
	for y in range(0,height):
		if tes[y][x] in range(20, nilaiMax):
			print ("posisi plot 2 = " + str(x))
			plotB = x
			for z in range(0, height):
				tes[z][x] = 255
			cek = 1
			break
		if cek == 1:
			break

lengthBlur = plotA - plotB
print ("panjang blur kiri = " + str(lengthBlur))

# kanan ke kiri
cek = 0
for x in range(width-1,0,-1):
	for y in range(0,height):
		if tes[y][x] in range(nilaiMax-10, nilaiMax):
			print ("posisi plot 3 = " + str(x))
			plotC = x
			for z in range(0, height):
				tes[z][x] = 255
			cek = 1
			break
		if cek == 1:
			break

cek = 0
for x in range(width-1,0,-1):
	for y in range(0,height):
		if tes[y][x] in range(20, nilaiMax):
			print ("posisi plot 4 = " + str(x))
			plotD = x
			for z in range(0, height):
				tes[z][x] = 255
			cek = 1
			break
		if cek == 1:
			break

lengthBlur2 = plotD - plotC
print ("panjang blur kanan = " + str(lengthBlur2))

if (lengthBlur > lengthBlur2):
	panjangBlurFinal = lengthBlur
else:
	panjangBlurFinal = lengthBlur2

print ("panjang blur terpanjang = " + str(panjangBlurFinal))	

# cek = 0
# for x in range(height-1,1,-1):
# 	for y in range(0,width):
# 		if tes[x][y] in range(nilaiMax-10, nilaiMax):
# 			for z in range(0, width):
# 				# tes[x][z] = 255
# 				tes[x+1][z] = 255
# 				tes[x+2][z] = 255
# 				tes[x+3][z] = 255
# 			cek = 1
# 			break
# 		if cek == 1:
# 			break

# for x in range(0,height):
# 	for y in range(0,width):
# 		mak = tes[x][y]
# 		if nilaiMax < mak:
# 			nilaiMax = mak

# cek = 0
# for x in range(0,height):
# 	for y in range(0,width):
# 		if tes[x][y] in range(nilaiMax-10, nilaiMax):
# 			for z in range(0, width):
# 				tes[x][z] = 255
# 				tes[x+1][z] = 255
# 				tes[x+2][z] = 255
# 			cek = 1
# 			break
# 		if cek == 1:
# 			break

# cek = 0
# for x in range(height-1,1,-1):
# 	for y in range(0,width):
# 		if tes[x][y] in range(nilaiMax-10, nilaiMax):
# 			for z in range(0, width):
# 				# tes[x][z] = 255
# 				tes[x+1][z] = 255
# 				tes[x+2][z] = 255
# 				tes[x+3][z] = 255
# 			cek = 1
# 			break
# 		if cek == 1:
# 			break



# gambarB-----------------------------
# cek horizontal 

# gambar huruf------------------------
# nilaiMax2 = 0
# mak2 = 0
# for x in range(0,height2):
# 	for y in range(0,width2):
# 		mak2 = tes2[x][y]
# 		if nilaiMax2 < mak2:
# 			nilaiMax2 = mak2

# cek2 = 0
# for x in range(0,height2):
# 	for y in range(0,width2):
# 		if tes2[x][y] in range(nilaiMax2-10, nilaiMax2):
# 			for z in range(0, width2):
# 				tes2[x][z] = 255
# 			cek2 = 1
# 			break
# 		if cek2 == 1:
# 			break

# cek2 = 0
# for x in range(height2-1,1,-1):
# 	for y in range(0,width2):
# 		if tes2[x][y] in range(nilaiMax2-10, nilaiMax2):
# 			for z in range(0, width2):
# 				# tes[x][z] = 255
# 				tes2[x+1][z] = 255
# 			cek2 = 1
# 			break
# 		if cek2 == 1:
# 			break

# gambar huruf------------------------

# cek2 = 0
# for x in range(width2-1,1,-1):
# 	for y in range(0,height2):
# 		if tes3[x][y] in batasMax2:
# 			for z in range(0, height2):
# 				# tes[x][z] = 255
# 				tes3[x][z] = 255
# 			cek2 = 1
# 			break
# 		if cek2 == 1:
# 			break


# dst2 = cv2.addWeighted(abs_grad_xB,0.5,abs_grad_yB,0.5,0)
# dst3 = cv2.addWeighted(abs_grad_xC,0.5,abs_grad_yC,0.5,0)
# dst4 = cv2.addWeighted(abs_grad_xD,0.5,abs_grad_yD,0.5,0)
# dst5 = cv2.addWeighted(abs_grad_xE,0.5,abs_grad_yE,0.5,0)
#dst = cv2.add(abs_grad_x,abs_grad_y)


# sobelSumx = (abs_grad_xA + abs_grad_xB + abs_grad_xC + abs_grad_xD + abs_grad_xE)/5
# sobelSumy = (abs_grad_yA + abs_grad_yB + abs_grad_yC + abs_grad_yD + abs_grad_yE)/5
# dst6 = cv2.addWeighted(sobelSumx, 0.5, sobelSumy, 0.5, 0)


# thesholding
# retval, threshold = cv2.threshold(dst6,0,255,cv2.THRESH_BINARY)



# robet detection -----------------------------------
# robert_horizontal = np.array([[-1, 0],
#                 [1, 0]])

# robert_vertical = np.array([[-1, 0],
#                 [0, 1]])

# blurA_ho = cv2.filter2D(blur, -1, robert_horizontal)
# blurA_ver = cv2.filter2D(blur, -1, robert_vertical)
# addWeight1 = cv2.add(blurA_ho, blurA_ver)

# blurB_ho = cv2.filter2D(blur2, -1, robert_horizontal)
# blurB_ver = cv2.filter2D(blur2, -1, robert_vertical)
# addWeight2 = cv2.add(blurB_ho, blurB_ver)

# blurC_ho = cv2.filter2D(blur3, -1, robert_horizontal)
# blurC_ver = cv2.filter2D(blur3, -1, robert_vertical)
# addWeight3 = cv2.add(blurC_ho, blurC_ver)

# blurD_ho = cv2.filter2D(blur4, -1, robert_horizontal)
# blurD_ver = cv2.filter2D(blur4, -1, robert_vertical)
# addWeight4 = cv2.add(blurD_ho, blurD_ver)

# blurE_ho = cv2.filter2D(blur5, -1, robert_horizontal)
# blurE_ver = cv2.filter2D(blur5, -1, robert_vertical)
# addWeight5 = cv2.add(blurE_ho, blurE_ver)

# plt.subplot(341), plt.imshow(gray, 'gray')
plt.subplot(131), plt.imshow(blur, 'gray')
plt.subplot(132), plt.imshow(dst, 'gray')
plt.subplot(133), plt.imshow(tes, 'gray')

# plt.subplot(234), plt.imshow(blur2, 'gray')
# plt.subplot(235), plt.imshow(dst2, 'gray')
# plt.subplot(236), plt.imshow(tes2, 'gray')

# plt.subplot(357), plt.imshow(dst2, 'gray')
# plt.subplot(358), plt.imshow(dst3, 'gray')
# plt.subplot(359), plt.imshow(dst4, 'gray')
# plt.subplot(3,5,10), plt.imshow(dst5, 'gray')
# plt.subplot(3,5,11), plt.imshow(dst6, 'gray')
# plt.subplot(3,5,12), plt.imshow(threshold, 'gray')
# plt.subplot(3,5,13), plt.imshow(dst3, 'gray')
# plt.subplot(3,5,14), plt.imshow(dst4, 'gray')
# plt.subplot(3,5,15), plt.imshow(dst5, 'gray')



plt.show()
