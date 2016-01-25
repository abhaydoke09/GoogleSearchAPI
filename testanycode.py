__author__ = 'abhay'
import cv2.cv


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
import random
import time


cv2.namedWindow('image')
img=cv2.imread('/home/abhay/M0.jpg')

while True:
    cv2.imshow('image',img)
    k=cv2.waitKey(10)
    if(k==27):
        break
