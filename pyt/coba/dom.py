import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt
from copy import deepcopy
from random import randint
from PIL import Image

np.set_printoptions(threshold=np.nan)
#img = cv2.imread('blur.jpg')
PILImage = Image.open("blur.jpg")
img = np.array(PILImage)



height = np.size(img, 0)
width = np.size(img, 1)
print ("height",height)
print ("width",width)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),3)
#cv2.imshow('original',img)
#cv2.imshow('grayscale',gray)
#cv2.imshow('gaussian blur',blur)


# tes = np.empty([5,5])
# tes[0][0] = 100
# tes[0][1] = 90
# tes[0][2] = 150
# tes[0][3] = 200
# tes[0][4] = 50

# tes[1][0] = 120
# tes[1][1] = 130
# tes[1][2] = 80
# tes[1][3] = 60
# tes[1][4] = 90

# tes[2][0] = 80
# tes[2][1] = 100
# tes[2][2] = 140
# tes[2][3] = 70
# tes[2][4] = 110

# tes[3][0] = 170
# tes[3][1] = 110
# tes[3][2] = 100
# tes[3][3] = 50
# tes[3][4] = 75

# tes[4][0] = 200
# tes[4][1] = 40
# tes[4][2] = 80
# tes[4][3] = 100
# tes[4][4] = 150

# del gray
# gray = tes
# height = 5
# width = 5


# saveout = sys.stdout
# fsock = open('ori.txt', 'w')
# sys.stdout = fsock
# for x in range(0,height):
# 	for y in range(0,width):
# 		if y == 0:
# 			print(str(gray[x][y]),end="")
# 		else:
# 			print("\t" + str(gray[x][y]),end="")
# 	print("")
# # print (img)
# sys.stdout = saveout


hasil = gray.copy()
# print (hasil)
for x in range(0,height):
	for y in range(0,width):
		matrik = []
		matrik.append(deepcopy(int(gray[x][y])))
		if x - 1 >= 0:
			matrik.append(deepcopy(int(gray[x-1][y])))
		if x + 1 < height:
			matrik.append(deepcopy(int(gray[x+1][y])))
		if y - 1 >= 0:
			matrik.append(deepcopy(int(gray[x][y-1])))
		if y + 1 < width:
			matrik.append(deepcopy(int(gray[x][y+1])))
		if x - 1 >= 0 and y - 1 >= 0:
			matrik.append(deepcopy(int(gray[x - 1][y - 1])))
		if x - 1 >= 0 and y + 1 < width:
			matrik.append(deepcopy(int(gray[x - 1][y + 1])))
		if x + 1 < height and y - 1 >= 0:
			matrik.append(deepcopy(int(gray[x + 1][y - 1])))
		if x + 1 < height and y + 1 < width:
			matrik.append(deepcopy(int(gray[x + 1][y + 1])))

		terbesar = 0
		terkecil = 0
		for z in range(len(matrik)):
			if z == 0:
				terbesar = matrik[z]
				terkecil = matrik[z]

			if matrik[z] > terbesar:
				terbesar = matrik[z]
			if matrik[z] < terkecil:
				terkecil = matrik[z]

		hasil[x,y] = terbesar-terkecil
		del matrik



# terbesar = 0
# terkecil = 0
# for x in range(0,height):
# 	for y in range(0,width):
# 		if x == 0 and y == 0:
# 			terbesar = gray[x][y]
# 			terkecil = gray[x][y]
# 		if gray[x][y] > terbesar :
# 			terbesar = gray[x][y]
# 		if gray[x][y] < terkecil:
# 			terkecil = gray[x][y]
# print (terbesar)
# print (terkecil)
#print (hasil)


# saveout = sys.stdout
# fsock = open('hasil.txt', 'w')
# sys.stdout = fsock
# for x in range(0,height):
# 	for y in range(0,width):
# 		if y == 0:
# 			print(str(hasil[x][y]),end="")
# 		else:
# 			print("\t" + str(hasil[x][y]),end="")
# 	print("")
# sys.stdout = saveout
# fsock.close()

# print(type(gray))
# print(type(hasil))

cv2.imshow('image gray',gray)
cv2.imshow('image hasil',hasil)
blur = cv2.GaussianBlur(hasil,(5,5),3)
cv2.imshow('image hasil + gaussian',blur)
# edges = cv2.Canny(img,100,200)
# cv2.imshow('edges',gray)


cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(131),plt.imshow(gray),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(132),plt.imshow(hasil),plt.title('hasil')
# plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.imshow(blur),plt.title('GaussianBlur')
# plt.xticks([]), plt.yticks([])
# plt.show()