import numpy as np
import cv2
#from matplotlib import pyplot as plt
img = cv2.imread('dataset/img_laser dinghy go pro capsize/frame159.jpg',0) #% count
edges = cv2.Canny(img,100,200)
cv2.imshow('edges', edges)
blur = cv2.blur(edges,(40,40))
cv2.imshow('blur',blur)
edges2 = cv2.Canny(blur,2,15)
cv2.imshow('edges2', edges2)
cv2.waitKey(0)
