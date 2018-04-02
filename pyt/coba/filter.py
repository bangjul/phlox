import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('TestImages/test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.blur(gray,(3,3))
blur2 = cv2.blur(gray,(5,5))
blur3 = cv2.blur(gray,(7,7))

height = np.size(img, 0)
width = np.size(img, 1)


# H = np.array([[1/9, 1/9, 1/9],   #3x3 kernel
#                 [1/9, 1/9, 1/9],
#                 [1/9, 1/9, 1/9]])

H = np.array([[0, 1, 0],   #laplacian
                [1, -4, 1],
                [0, 1, 0]])

H = np.array([[0, 0, 0],   #hapus tetangga
                [0, 1, 0],
                [0, 0, 0]])

# prewit_vertical = np.array([[-1, 0, 1],
#                 [-1, 0, 1],
#                 [-1, 0, 1]])

# prewit_horizontal = np.array([[-1, -1, -1],
#                 [0, 0, 0],
#                 [1, 1, 1]])

# robert_vertical = np.array([[-1, 0],
#                 [0, 1]])

robert_horizontal = np.array([[-1, 0],
                [1, 0]])

#hasil = gray.copy()
# for x in range(0,height):
# 	for y in range(0,width):
# 		hasil[x][y] = 0
# 		for i in range(len(H - 1)):
# 			for j in range (len(H - 1)):
# 				hasil[x][y] = hasil[x][y] + (H[i][j] * gray[x][y])

output = cv2.filter2D(gray, -1, H)


# pre_ver = cv2.filter2D(gray, -1, prewit_vertical)
# pre_ho = cv2.filter2D(gray, -1, prewit_horizontal)

# robert_ver = cv2.filter2D(gray, -1, robert_vertical)
robert_ho = cv2.filter2D(gray, -1, robert_horizontal)

newBlur = blur-blur2
newBlur2 = blur-blur3
newBlur3 = blur2-blur3


newHapus = cv2.filter2D(gray, -1, newBlur)

# def dikurangi(a, b):
# 	newBlur = a - b
# 	cv2.imshow('3x3 - 5x5',newBlur)


def hapus(gambar):
	height = np.size(gambar, 0)
	width = np.size(gambar, 1)
	for x in range(0,height - 1):
		for y in range(0,width - 1):
			if y == 0:
				if x == 0:
					if gambar[x+1][y] < 100 and gambar[x+1][y+1] < 100 :
						if gambar[x][y+1] < 100:
							gambar[x][y] = 0
				if x == width:
					if gambar[x-1][y] < 100 and gambar[x-1][y+1] < 100 :
						if gambar[x][y+1] < 100:
							gambar[x][y] = 0
				if gambar[x+1][y] < 100 and gambar[x+1][y+1] < 100 :
					if gambar[x][y+1] < 100 and gambar[x-1][y+1] < 100:
						if gambar[x-1][y] < 100:
							gambar[x][y] = 0
			
			if y == height:
				if x == 0:
					if gambar[x+1][y] < 100 and gambar[x+1][y-1] < 100 :
						if gambar[x][y-1] < 100:
							gambar[x][y] = 0
				if x == width:
					if gambar[x-1][y] < 100 and gambar[x-1][y-1] < 100 :
						if gambar[x][y-1] < 100:
							gamba[x][y] = 0
				if gambar[x+1][y] < 100 and gambar[x+1][y-1] < 100 :
					if gambar[x][y-1] < 100 and gambar[x-1][y-1] < 100:
						if gambar[x-1][y] < 100:
							gambar[x][y] = 0

			
			if x == 0:
				if gambar[x][y-1] < 100 and gambar[x+1][y-1] < 100 :
					if gambar[x+1][y] < 100 and gambar[x+1][y+1] < 100:
						if gambar[x][y+1] < 100:
							gambar[x][y] = 0

			if x == width:
				if gambar[x][y-1] < 100 and gambar[x-1][y-1] < 100 :
					if gambar[x-1][y] < 100 and gambar[x-1][y+1] < 100:
						if gambar[x][y+1] < 100:
							gambar[x][y] = 0

			if gambar[x][y-1] < 100 and gambar[x+1][y-1] < 100 :
				if gambar[x+1][y] < 100 and gambar[x+1][y+1] < 100:
					if gambar[x][y+1] < 100 and gambar[x-1][y+1] < 100:
						if gambar[x-1][y] < 100 and gambar[x-1][y-1] < 100:
							gambar[x][y] = 0

	cv2.imshow('Hapus',gambar)
	for x in range (0, 20):
		for y in range (0, 1):
			print (gambar[x,y])

# cv2.imshow('original',gray)

# dikurangi(blur, blur2)
hapus(newBlur3)




# print (newBlur[5,0])
# print (newBlur[6,0])
# print (newBlur[7,0])
# print (newBlur[8,0])

# cv2.imshow('laplacian',output)
# cv2.imshow('filter 3x3',blur)
# cv2.imshow('filter 5x5',blur2)
# cv2.imshow('filter 7x7',blur3)
# cv2.imshow('filter 3x3 - 5x5',newBlur)
# cv2.imshow('filter 3x3 - 7x7',newBlur2)
# cv2.imshow('filter 5x5 - 7x7',newBlur3)

# cv2.imshow('image previt vertical',pre_ver)
# cv2.imshow('image previt horizontal',pre_ho)
# cv2.imshow('image robert vertical',robert_ver)
# cv2.imshow('image robert horizontal',robert_ho)

# hist_newBlur = cv2.calcHist([newBlur],[0],None,[255],[0,255])
# hist_newBlur2 = cv2.calcHist([newBlur2],[0],None,[255],[0,255])
# hist_newBlur3 = cv2.calcHist([newBlur3],[0],None,[255],[0,255])

plt.subplot(331), plt.imshow(blur, 'gray')
plt.subplot(332), plt.imshow(blur2, 'gray')
plt.subplot(333), plt.imshow(blur3, 'gray')
plt.subplot(334), plt.imshow(newBlur, 'gray')
plt.subplot(335), plt.imshow(newBlur2,'gray')
plt.subplot(336), plt.imshow(newBlur3,'gray')
plt.subplot(337), plt.imshow(output,'gray')
plt.subplot(338), plt.imshow(robert_ho,'gray')
plt.subplot(339), plt.imshow(newHapus,'gray')
# plt.subplot(235), plt.plot(hist_newBlur), plt.plot(hist_newBlur2), plt.plot(hist_newBlur3)
# plt.xlim([0,255])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()