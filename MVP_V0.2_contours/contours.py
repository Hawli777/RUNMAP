# -*- coding: utf-8 -*-
# 2015��12��14�� �����ı��鿴����list-->txt
# runmap  by shawn0lee0

import cv2
import sys,codecs
import json #��֤��javascript���ݸ�ʽͳһ
import cv2.cv as cv
import numpy

position = 100 #����canny��ʼ��ֵ

img = cv2.imread('C:\\Users\\robo_one\\Desktop\\fx.jpg') #C:\Users\robo_one\Desktop\fx.jpg
print type(img) #<type 'numpy.ndarray'>
img = cv2.GaussianBlur(img,(3,3),0)
print type(img)
print (numpy.size(img)) #��˹ƽ����ͼ�����ص�-->685452
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print (numpy.size(gray))#�Ҷ�ͼ�����ص�-->228484

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
print type(binary)
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),3)

str_len_contours = str(len(contours)) #ȡ��������

print "contours num:%s" %str_len_contours


print (type(contours))
print (type(contours[0]))


print contours[0]


contours_list = contours[-1].tolist()
print contours_list
print contours_list[0][0]

img_pix = str(numpy.size(img))
gray_pix = str(numpy.size(gray))
#�����嵥ת�ı����
s = open("Contours.txt",'a')
s.write("Img GaussianBlur pix nums:" +"%s" %img_pix + "\n") 
s.write("Gausss to gray pix nums:" +"%s" %gray_pix + "\n") 
s.write("contours num:" +"%s" %str_len_contours + "\n") 
for ele in contours:
 s.write("%s\n" % ele)
s.write("**"*50  + "\n")
s.close()

l = open("contours_list.txt",'a')
l.write("contours_list"  + "\n")
for ele in contours_list:
 l.write("%s\n" % ele)
l.write("**"*50  + "\n")
l.close()

cv2.imshow("img", img)

cv2.waitKey(0)
