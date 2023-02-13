import numpy as np
import cv2
#from matplotlib import pyplot as plt
img = cv2.imread('dataset/img_laser dinghy go pro capsize/frame159.jpg',0) #% count
edges = cv2.Canny(img,100,200)
cv2.imshow('edges', edges)
#blur = cv2.blur(edges,(40,40))
#cv2.imshow('blur',blur)
#edges2 = cv2.Canny(blur,2,15)
#cv2.imshow('edges2', edges2)


#convert
# Copy edges to the images that will display the results in BGR
cdst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
cdstP = np.copy(cdst) #in the sample code for the P (approximation) method


# Probabilistic Line Transform
linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, None, 100, 10)
print(linesP)
#houghlinespimg = linesP
# Draw the lines
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
#convert to uint8
print(cdstP)
#houghlinespimg=np.uint8(cdstP)
cv2.imshow("houghP",cdstP)

cv2.waitKey(0)
cv2.destroyWindow('edges')
cv2.destroyWindow('houghP')