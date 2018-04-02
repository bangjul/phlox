import cv2
import glob
import numpy as np


for img in glob.glob("TestImages/coba/DSC03512.jpg"):
    image = cv2.imread(img)
    # blur = cv2.GaussianBlur(image,(11,11),11)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(image,50,150,apertureSize=3)
    # cv2.imwrite('TestImages/blur.jpg',blur)
    minLineLength=100
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=100)
    a,b,c = lines.shape
    for i in range(a):
    	cv2.line(image, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
    	cv2.imwrite('TestImages/coba/houghlines5.jpg',image)

    # scale = 1
    # delta = 0
    # ddepth = cv2.CV_16S
    # grad_yA = cv2.Sobel(gray,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
    # cv2.imwrite('TestImages/sobely.jpg',grad_yA)
    cv2.imshow('hasil',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# for img in glob.glob("TestImages/coba/*.jpg"):
#     image = cv2.imread(img)
#     gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray,50,150,apertureSize=3)
#     lines = cv2.HoughLines(edges,1,np.pi/180,200)
#     for rho,theta in lines[0]:
#     	a = np.cos(theta)
#     	b = np.sin(theta)
#     	x0 = a*rho
#     	y0 = b*rho
#     	x1 = int(x0 + 1000*(-b))
#     	y1 = int(y0 + 1000*(a))
#     	x2 = int(x0 - 1000*(-b))
#     	y2 = int(y0 - 1000*(a))
#     	cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)

#     # minLineLength = 100
#     # maxLineGap = 10
#     # lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
#     # for x1,y1,x2,y2 in lines[0]:
#     # 	cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)

#     cv2.imshow('hasil',image)
#     # cv2.imshow('canny',edges)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # -------------------------

# gray = cv2.imread('TestImages/coba/1.jpg',0)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# #cv2.imwrite('edges-50-150.jpg',edges)
# minLineLength=100
# lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)
 	
# a,b,c = lines.shape
# for i in range(a):
#     cv2.line(gray, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
#     cv2.imwrite('houghlines5.jpg',gray)


# cv2.imshow('hasil',gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()