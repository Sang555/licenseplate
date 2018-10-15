import cv2
import numpy as np
from statistics import mode
#read image
im1=cv2.imread("v1.jpeg")
#scale up
im2=cv2.pyrUp(im1)
#smoothen and convert to grayscale
im3=cv2.GaussianBlur(im2,(5,5),0)
im4=cv2.cvtColor(im3,cv2.COLOR_BGR2GRAY)
#edge detection( computes intensity gradients and filters those inrange)
im5=cv2.Canny(im4,30,200)
#find contours
i,cnt,h=cv2.findContours(im5,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
hl=[]
for c in cnt:
	x,y,w,h = cv2.boundingRect(c)
	hl.append(h)
m=mode(hl)
print(type(m))
for c in cnt:
	x,y,w,h = cv2.boundingRect(c)
	if((h<m+3) and (h>m-3)):
	        cv2.rectangle(im2,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("im5",im2)
cv2.waitKey(0)
