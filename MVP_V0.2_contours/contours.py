# -*- coding: utf-8 -*-
# 2015��12��14�� �����ı��鿴����list-->txt
# runmap  by shawn0lee0

import cv2
import sys,codecs
import json #��֤��javascript���ݸ�ʽͳһ

img = cv2.imread('C:\\Users\\robo_one\\Desktop\\fx.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),3)

print (type(contours))
print (type(contours[0]))
print (len(contours))

print contours[0]

contours_list = contours[0].tolist()
print contours_list

#�����嵥ת�ı����
s = open("WXJ_contours.txt",'a')
s.write("contours list"  + "\n")
for ele in contours:
 s.write("%s\n" % ele)
s.write("**"*50  + "\n")
s.close()


cv2.imshow("img", img)

cv2.waitKey(0)
