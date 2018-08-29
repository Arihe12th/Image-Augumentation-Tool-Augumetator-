#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:50:10 2018

@author: nanoyotta
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:43:20 2018

@author: nanoyotta
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:27:02 2018

@author: nanoyotta
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AugmentV2ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import keras
import tensorflow as tf
import os
import cv2
import numpy as np
import StringIO
import PIL as im
import sys
from PIL import Image,ImageEnhance
import sip
import imgaug as ia
from imgaug import augmenters as iaa
import imutils
from PyQt4 import QtCore, QtGui
from thread import start_new_thread
from multiprocessing import Process
import time
import xml.etree.ElementTree as ET
from xml.dom import minidom
import xml.dom.minidom
import shutil
import threading
import multiprocessing
import concurrent.futures

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class Ui_Dialog(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        global images
        images=[]
        global imgname
        imgname=[]
        global xmlname
        xmlname=[]
        global le
        self.workerthread=WorkerThread()
        
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setText("Open Folder")
        self.pushButton.setGeometry(QtCore.QRect(930, 40, 112, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.open_directory)
        self.listView = QtGui.QListView(self)
        self.listView.setGeometry(QtCore.QRect(220, 80, 851, 731))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.checkBox = QtGui.QCheckBox(self)
        self.checkBox.setText("Horizontal Flip")
        self.checkBox.setGeometry(QtCore.QRect(260, 90, 141, 24))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        #self.checkBox.stateChanged.connect(self.horizontalflip)
        self.checkBox_2 = QtGui.QCheckBox(self)
        self.checkBox_2.setText("Vertical Flip")
        self.checkBox_2.setGeometry(QtCore.QRect(260, 120, 131, 24))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_4 = QtGui.QCheckBox(self)
        self.checkBox_4.setText("Rotate")
        self.checkBox_4.setGeometry(QtCore.QRect(260, 150, 110, 24))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        #self.checkBox_4.stateChanged.connect(self.rotate)
        self.checkBox_5 = QtGui.QCheckBox(self)
        self.checkBox_5.setText("Brightness")
        self.checkBox_5.setGeometry(QtCore.QRect(260, 180, 110, 24))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self)
        self.checkBox_6.setText("Contrast")
        self.checkBox_6.setGeometry(QtCore.QRect(260, 210, 110, 24))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self)
        self.checkBox_7.setText("Hue")
        self.checkBox_7.setGeometry(QtCore.QRect(260, 240, 110, 24))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_8 = QtGui.QCheckBox(self)
        self.checkBox_8.setText("Gamma")
        self.checkBox_8.setGeometry(QtCore.QRect(260, 270, 110, 24))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox_9 = QtGui.QCheckBox(self)
        self.checkBox_9.setText("Saturation")
        self.checkBox_9.setGeometry(QtCore.QRect(260, 300, 110, 24))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_10 = QtGui.QCheckBox('Crop', self)
        self.checkBox_10.setText("Crop Center")
        self.checkBox_10.setGeometry(QtCore.QRect(260, 330, 141, 24))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.checkBox_11 = QtGui.QCheckBox(self)
        self.checkBox_11.setText("Transpose")
        self.checkBox_11.setGeometry(QtCore.QRect(260, 360, 110, 24))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.checkBox_12 = QtGui.QCheckBox(self)
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setText("Augumentate")
        self.pushButton_2.setGeometry(QtCore.QRect(760, 820, 161, 29))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.check)
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setText("cancel")
        self.pushButton_3.setGeometry(QtCore.QRect(960, 820, 112, 29))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self)
        self.pushButton_4.setText("Saving Directory")
        self.pushButton_4.setGeometry(QtCore.QRect(250, 820, 151, 29))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.select_dir)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self)
        self.doubleSpinBox.setGeometry(QtCore.QRect(850, 320, 66, 29))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.doubleSpinBox.valueChanged.connect(self.cropvalue)
        self.checkBox_14 = QtGui.QCheckBox(self)
        self.checkBox_14.setText("Rotate")
        self.checkBox_14.setGeometry(QtCore.QRect(260, 390, 108, 24))
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.lineEdit_5 = QtGui.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(850, 380, 113, 29))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_5.textChanged.connect(self.Rotatevalue)
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setText("Enter Rotate Angle")
        self.label_5.setGeometry(QtCore.QRect(450, 390, 161, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.checkBox_15 = QtGui.QCheckBox(self)
        self.checkBox_15.setText("Salt&peper")
        self.checkBox_15.setGeometry(QtCore.QRect(260, 420, 121, 24))
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.checkBox_16 = QtGui.QCheckBox(self)
        self.checkBox_16.setText("Shading")
        self.checkBox_16.setGeometry(QtCore.QRect(260, 450, 111, 24))
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.checkBox_3 = QtGui.QCheckBox(self)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 480, 108, 24))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_3.setText("Shearing")
        self.lineEdit_8 = QtGui.QLineEdit(self)
        self.lineEdit_8.setGeometry(QtCore.QRect(850, 410, 113, 29))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_8.textChanged.connect(self.saltpepper)
        self.lineEdit_9 = QtGui.QLineEdit(self)
        self.lineEdit_9.setGeometry(QtCore.QRect(850, 440, 111, 31))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_9.textChanged.connect(self.shading1)
        self.lineEdit_10 = QtGui.QLineEdit(self)
        self.lineEdit_10.setGeometry(QtCore.QRect(470, 820, 151, 29))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self)
        self.lineEdit_11.setGeometry(QtCore.QRect(470, 870, 151, 29))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setText("Enter salt amount")
        self.label_7.setGeometry(QtCore.QRect(450, 420, 151, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setText("Enter Shade value(-40to+0 is recommended)")
        self.label_8.setGeometry(QtCore.QRect(450, 450, 351, 19))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setText("Create New Directory")
        self.label_9.setGeometry(QtCore.QRect(250, 870, 181, 19))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label = QtGui.QLabel(self)
        self.label.setText("EnterCrop Value(0.5 - 2)")
        self.label.setGeometry(QtCore.QRect(450, 330, 221, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox_12 = QtGui.QCheckBox(self)
        self.checkBox_12.setText("Shear Left")
        self.checkBox_12.setGeometry(QtCore.QRect(260, 540, 181, 24))
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.checkBox_13 = QtGui.QCheckBox(self)
        self.checkBox_13.setText("RotateBoundBox")
        self.checkBox_13.setGeometry(QtCore.QRect(260, 510, 161, 24))
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setText("File name to save files")
        self.label_2.setGeometry(QtCore.QRect(260, 910, 191, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(470, 910, 151, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.textChanged.connect(self.allfilename)
        self.pushButton_5 = QtGui.QPushButton("Create",self)
        self.pushButton_5.setGeometry(QtCore.QRect(630,870,110,29))
        self.pushButton_5.clicked.connect(self.makedir)
        self.pushButton_6 = QtGui.QPushButton("Refresh",self)
        self.pushButton_6.setGeometry(QtCore.QRect(960, 880, 110, 29))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(self.refresh)
        self.checkBox_17 = QtGui.QCheckBox(self)
        self.checkBox_17.setText("Resize")
        self.checkBox_17.setGeometry(QtCore.QRect(260, 570, 108, 24))
        self.checkBox_17.setObjectName(_fromUtf8("checkBox_17"))
        

#function for checking whether check box is selected or not       
    def check(self):
        if self.checkBox.isChecked():
            start_new_thread(self.horizontalflip,())
        if self.checkBox_2.isChecked():
            start_new_thread(self.verticalflip,())
        if self.checkBox_3.isChecked():
            self.shearing()
        if self.checkBox_4.isChecked():
            start_new_thread(self.rotate90,())
        if self.checkBox_5.isChecked():
            start_new_thread(self.Brightness,())
        if self.checkBox_10.isChecked():
            start_new_thread(self.crop,())
        if self.checkBox_14.isChecked():
            start_new_thread(self.rotate,())
        if self.checkBox_9.isChecked():
            start_new_thread(self.saturation,())
        if self.checkBox_8.isChecked():
            start_new_thread(self.gamma,())
        if self.checkBox_7.isChecked():
            start_new_thread(self.hue,())
        if self.checkBox_6.isChecked():
            start_new_thread(self.contrast,())
        if self.checkBox_11.isChecked():
            start_new_thread(self.transpose,())
        if self.checkBox_15.isChecked():
            start_new_thread(self.saltpeper1,())
        if self.checkBox_16.isChecked():
            start_new_thread(self.Shading,())
        if self.checkBox_12.isChecked():
            self.shear_left()
        if self.checkBox_13.isChecked():
            self.rotate_boundbox()
        if self.checkBox_17.isChecked():
            start_new_thread(self.Resize,())
        else:
            QtGui.QMessageBox.information(ui,"warning","please tick checkbox")


        
#function to get global path of annotated image datasets.
    def open_directory(self):
        start = time.time()    
        global path1
        path1="/home/nanoyotta/Desktop/Augumentatin/Result/1/"
        global k
        global path
        path=QtGui.QFileDialog.getExistingDirectory(self)
        end = time.time()
        print("load"+"----"+str(end - start))

    def cropvalue(self, ev):
        global va
        va=self.doubleSpinBox.value()
    def Rotatevalue(self):
        global ro
        ro=float(self.lineEdit_5.text())
    def resizevalue(self):
        global re
        global re2
        re=self.lineEdit_6.text()
        re2=self.lineEdit_7.text()
    def saltpepper(self):
        global salt
        salt=self.lineEdit_8.text()
    def shading1(self):
        global shade
        shade=self.lineEdit_9.text()
    def select_dir(self):
        global selectfolderpath
        selectfolderpath=QtGui.QFileDialog.getExistingDirectory(self)
        self.lineEdit_10.setText(selectfolderpath)
    def makedir(self):
        global dirname
        global dirpath
        dirname=self.lineEdit_11.text()
        dirpath=selectfolderpath+"/"+dirname+"/"
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
    def allfilename(self):
        global allfilenames
        allfilenames=self.lineEdit.text()
'''copy xml from source to destination folder for augumentation which is non 
prespective(eg. only for augumentation like brightness, shade, salt and pepper, 
contrast etc whic don't do any prespective change in image like rotation ect)'''
    def copyto(self,xfilena):
        start=time.time()
        vl=0
        xmco=0
        for xfiles in sorted(os.listdir(path)):
            patt=os.path.join(path,xfiles)
            if patt.endswith('.xml'):
                rename=allfilenames+"_"+xfilena+str(vl)+".xml"
                dirpath=selectfolderpath+"/"+dirname+"/"+rename
                shutil.copy(patt,dirpath)
                vl=vl+1
        end=time.time()
        print('copyto'+'----'+str(end-start))
    def refresh(self):
        del images[:]
        self.checkBox_3.ser
#crop function
    def crop(self):
        start = time.time()        
        count=1
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.central_crop(tfimg,va)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+"Crop"+str(count)+".jpg",numpy_array_2)
                    count=count+1
                end = time.time()
        print("crop"+"----"+str(end - start))
#horizontal Flip        
    def horizontalflip(self):
        start = time.time()
        xfilena="Horizontalflip"
        coun1=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.flip_left_right(tfimg)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+xfilena+str(coun1)+".jpg",numpy_array_2)
                coun1=coun1+1
        end = time.time()
        self.copyto(xfilena)
        print("horizontalFlip"+"----"+str(end - start))
    def verticalflip(self):
        start = time.time()
        xfilena="Verticalflip"
        coun=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.flip_up_down(tfimg)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+"verticalflip"+str(coun)+".jpg",numpy_array_2)
                coun=coun+1
        self.copyto(xfilena)
        end = time.time()
        print("verticalFlip"+"----"+str(end - start))   
    def rotate90(self):
        start = time.time()
        coun=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.rot90(tfimg, k = 1)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+"rotate90degree"+str(coun)+".jpg",numpy_array_2)
                coun=coun+1
        end = time.time()
        print("rotate90"+"----"+str(end - start))
    def Brightness(self):
        start = time.time()
        count=0
        xfilena4="brightness"
        count1=0
        global filenamu
        filenamu="Egypt_vs_Uruguay"
        global li
        li=[]
        global boundupdateli
        boundupdateli=[]
        global updatexmlli
        updatexmlli=[]
        for i in sorted(os.listdir(path)):
            filepath=os.path.join(path,i)
            if filepath.endswith(".jpg"):
                imgpa=filepath
                image=cv2.imread(imgpa)
                seq = iaa.Sequential([iaa.Multiply((1.2, 1.2)),
                                           ]) # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
                seq_det = seq.to_deterministic()
                images_aug = seq_det.augment_images(image)
                cv2.imwrite(dirpath+allfilenames+"_"+"brightness"+str(count)+".jpg",images_aug)
                count=count+1        
        end = time.time()
        self.copyto(xfilena4)
        print("Brightness"+"----"+str(end - start))   
    def rotate(self):
        start = time.time()
        coun=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                rotated = imutils.rotate_bound(a, ro)
                cv2.imwrite(dirpath+allfilenames+"_"+"rotatetovalue"+str(coun)+".jpg",rotated)
                coun=coun+1
        end = time.time()
        print("rotate"+"----"+str(end - start))   
    def resize1(self):
        start = time.time()
        coun=0
        for j in images:
            d=j.shape
            tfimg = tf.convert_to_tensor(j)
            brght_img = tf.image.resize_images(tfimg,re,re2)
            sess = tf.Session()
            with sess.as_default():
                numpy_array_2 = brght_img.eval()
                cv2.imwrite(dirpath+allfilenames+"_"+"resize"+str(coun)+".jpg",numpy_array_2)
                coun=coun+1
        end = time.time()
        print("resize"+"----"+str(end - start)) 
    def saturation(self):
        start = time.time()
        satuname="saturation"
        coun=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.adjust_saturation(tfimg,0.5)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+"saturation"+str(coun)+".jpg",numpy_array_2)
                    coun=coun+1
        self.copyto(satuname)
        end = time.time()
        print("saturation"+"----"+str(end - start)) 
    def gamma(self):
        start = time.time()
        gamaname="gamma"
        coun=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                tom=tf.cast(tfimg, tf.float32)
                brght_img = tf.image.adjust_gamma(tom,gamma=1,gain=1)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+"gamma"+str(coun)+".jpg",numpy_array_2)
                    coun=coun+1
        self.copyto(gamaname)
        end = time.time()
        print("gamma"+"----"+str(end - start))
    def hue(self):
        start = time.time()
        huename="hue"
        coun=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen)) 
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.adjust_hue(tfimg,-0.5, name=None)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+"hue"+str(coun)+".jpg",numpy_array_2)
                    coun=coun+1
        self.copyto(huename)
        end = time.time()
        print("hue"+"----"+str(end - start))
    def contrast(self):
        start = time.time()
        counCo=0
        contrast="conrast"
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.adjust_contrast(tfimg,0.4)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+contrast+str(counCo)+".jpg",numpy_array_2)
                counCo=counCo+1
                
        self.copyto(contrast)
        end = time.time()
        print("contrast"+"----"+str(end - start))
    def croptoboundingbox(self):
        start = time.time()
        coun=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.crop_to_bounding_box(tfimg,offset_height = oh, offset_width = ow, target_height = th, target_width = tw)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+"cropboundbox"+str(coun)+".jpg",numpy_array_2)
                    coun=coun+1
        end = time.time()
        print("croptoboundingbox"+"----"+str(end - start))
    def transpose(self):
        start = time.time()
        coun=0
        for filen in sorted(os.listdir(path)):
            if filen.endswith('.jpg'):
                a=cv2.imread(os.path.join(path,filen))
                tfimg = tf.convert_to_tensor(a)
                brght_img = tf.image.transpose_image(tfimg)
                sess = tf.Session()
                with sess.as_default():
                    numpy_array_2 = brght_img.eval()
                    cv2.imwrite(dirpath+allfilenames+"_"+"transpose"+str(coun)+".jpg",numpy_array_2)
                    coun=coun+1
        end = time.time()
        print("transpose"+"----"+str(end - start))
    def saltpeper1(self):
        start = time.time()
        counsl=0
        salname="saltandpepper"
        for i in sorted(os.listdir(path)):
            filepath=os.path.join(path,i)
            if filepath.endswith(".jpg"):
                imgpa=filepath
                image=cv2.imread(imgpa)
                seq = iaa.Sequential([iaa.AdditiveGaussianNoise(scale=float(salt)*255)])
                                            # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
                seq_det = seq.to_deterministic()
                images_aug = seq_det.augment_images(image)
                cv2.imwrite(dirpath+allfilenames+"_"+salname+str(counsl)+".jpg",images_aug)
                counsl=counsl+1
        self.copyto(salname)
        end = time.time()
        print("saltpepper"+"----"+str(end - start))
    def Shading(self):
        start = time.time()
        shadename="shading"
        co=0
        for i in sorted(os.listdir(path)):
            filepath=os.path.join(path,i)
            if filepath.endswith(".jpg"):
                imgpa=filepath
                image=cv2.imread(imgpa)
                seq = iaa.Sequential([iaa.Add(int(shade))])
                seq_det = seq.to_deterministic()
                images_aug = seq_det.augment_images(image)
                cv2.imwrite(dirpath+allfilenames+"_"+"shading"+str(co)+".jpg",images_aug)
                co=co+1
        self.copyto(shadename) 
        end = time.time()
        print("shading"+"----"+str(end - start))
    def shearing(self):
        start=time.time()
        count=0
        count1=0
        global filenamu
        filenamu="Costa_Rica_vs_Serbia"
        global li
        li=[]
        global boundupdateli
        boundupdateli=[]
        global updatexmlli
        updatexmlli=[]
        for i in sorted(os.listdir(path)):
            filepath=os.path.join(path,i)
            if filepath.endswith(".jpg"):
                imgpa=filepath
                xmll=i.split('.')[0]
                xmlll=xmll+'.xml'
                new=i.split('Costa_Rica_vs_Serbia')[0]
                xmllll=os.path.join(path,xmlll)
                if xmllll.endswith('.xml'):
                    xmlp=xmllll
                    image=cv2.imread(imgpa)
                    a=xml.dom.minidom.parse(xmlp)
                    ann = a.documentElement
                    collections=ann.getElementsByTagName('object')
                    objects=ann.getElementsByTagName('object')
                    fi=ann.getElementsByTagName('filename')[0]
                    filna=fi.childNodes[0].data
                    pathn=ann.getElementsByTagName('path')[0]
                    pan = pathn.childNodes[0].data
                    coun=0
                    for co in collections:
                        k=co.getElementsByTagName('name')[0]
                        classs= k.childNodes[0].data
                        xmin=co.getElementsByTagName('xmin')[0]
                        ymin=co.getElementsByTagName('ymin')[0]
                        xmax=co.getElementsByTagName('xmax')[0]
                        ymax=co.getElementsByTagName('ymax')[0]
                        x=  xmin.childNodes[0].data
                        y=  ymin.childNodes[0].data
                        xm= xmax.childNodes[0].data
                        ym= ymax.childNodes[0].data
                        li.append((classs,x,y,xm,ym))
                    for sett in li:
                        cla=sett[0]
                        xmi1=sett[0+1]
                        ymi1=sett[0+2]
                        xma1=sett[0+3]
                        yma1=sett[0+4]
                        bbs = ia.BoundingBoxesOnImage([ia.BoundingBox(x1=float(xmi1), y1=float(ymi1), x2=float(xma1), y2=float(yma1))],image.shape)
                        seq = iaa.Sequential([
                                iaa.Affine(shear=22,scale=(0.9,0.9)
                                           ) # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
                                ])
                        seq_det = seq.to_deterministic()
                        image_aug = seq_det.augment_images([image])[0]
                        bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]
                    
                        for i in range(len(bbs.bounding_boxes)):
                            before = bbs.bounding_boxes[i]
                            after = bbs_aug.bounding_boxes[i]
                            image_before = bbs.draw_on_image(image, thickness=2)
                            image_after = bbs_aug.draw_on_image(image_aug, thickness=0, color=[0, 0, 255])
                            updatexmlli.append((cla,after.x1,after.y1,after.x2,after.y2))
                            cv2.imwrite(dirpath+allfilenames+"_"+"Shear_right"+str(count)+".jpg",image_after)                
                    root=ET.Element("annotation")
                    fold=ET.SubElement(root,"folder")
                    fold.text="augumentation"
                    xlfilename=ET.SubElement(root,"filename")
                    xlfilename.text=allfilenames+"_Shear_right"+".jpg"
                    xlpath=ET.SubElement(root,"path")
                    xlpath.text=dirpath  
                    source=ET.Element("source")
                    root.append(source)               
                    database=ET.SubElement(source,"database")
                    database.text="Unknown"              
                    size=ET.Element("size")
                    root.append(size)
                    width=ann.getElementsByTagName('width')[0]
                    wi = width.childNodes[0].data                    
                    xlwidth=ET.SubElement(size,"width")
                    xlwidth.text=wi                       
                    height=ann.getElementsByTagName('height')[0]
                    hei = height.childNodes[0].data
                    xlheight=ET.SubElement(size,"height")
                    xlheight.text=hei                         
                    depth=ann.getElementsByTagName('depth')[0]
                    de = depth.childNodes[0].data
                    xldepth=ET.SubElement(size,"depth")
                    xldepth.text=de
                    segment=ET.SubElement(root,"segmented")
                    segment.text="0"
                    for val in updatexmlli:
                        model=val[0]
                        cox=int(val[0+1])
                        coy=int(val[0+2])
                        comx=int(val[0+3])
                        comy=int(val[0+4])
                        xlobject=ET.Element("object")
                        root.append(xlobject)
                        xlbname=ET.SubElement(xlobject,"name")
                        xlbname.text=model
                        pose=ET.SubElement(xlobject,"pose")
                        pose.text="Unspecified"
                        truncate=ET.SubElement(xlobject,"truncated")
                        truncate.text="0"
                        difficult=ET.SubElement(xlobject,"difficult")
                        difficult.text="0"   
                        bndbox=ET.SubElement(xlobject,"bndbox")
                        tree = ET.ElementTree(root)
                        xlxmin=ET.SubElement(bndbox,"xmin")
                        xlxmin.text=str(cox)
                        xlymin=ET.SubElement(bndbox,"ymin")
                        xlymin.text=str(coy)
                        xlxax=ET.SubElement(bndbox,"xmax")
                        xlxax.text=str(comx)
                        xlymax=ET.SubElement(bndbox,"ymax")
                        xlymax.text=str(comy)
                        
                    tree = ET.ElementTree(root)
                    fname=allfilenames+"_"+"Shear_right"+str(count1)+".xml"
                    with open(os.path.join(dirpath,fname), "w") as fh:
                        tree.write(fh)
                count=count+1
                count1=count1+1
                updatexmlli=[]
                li=[]
                end=time.time()
                print("shear"+"----"+str(end - start))
    def shear_left(self):
        start=time.time()
        count=0
        count1=0
        global filenamu
        filenamu="Egypt_vs_Uruguay"
        global li
        li=[]
        global boundupdateli
        boundupdateli=[]
        global updatexmlli
        updatexmlli=[]
        for i in sorted(os.listdir(path)):
            filepath=os.path.join(path,i)
            if filepath.endswith(".jpg"):
                imgpa=filepath
                xmll=i.split('.')[0]
                xmlll=xmll+'.xml'
                new=i.split('Egypt_vs_Uruguay')[0]
                xmllll=os.path.join(path,xmlll)
                if xmllll.endswith('.xml'):
                    xmlp=xmllll
                    image=cv2.imread(imgpa)
                    a=xml.dom.minidom.parse(xmlp)
                    ann = a.documentElement                             
                    collections=ann.getElementsByTagName('object')
                    objects=ann.getElementsByTagName('object')
                    fi=ann.getElementsByTagName('filename')[0]
                    filna=fi.childNodes[0].data
                    pathn=ann.getElementsByTagName('path')[0]
                    pan = pathn.childNodes[0].data
                    coun=0
                    for co in collections:
                        k=co.getElementsByTagName('name')[0]
                        classs= k.childNodes[0].data
                        xmin=co.getElementsByTagName('xmin')[0]
                        ymin=co.getElementsByTagName('ymin')[0]
                        xmax=co.getElementsByTagName('xmax')[0]
                        ymax=co.getElementsByTagName('ymax')[0]
                        x=  xmin.childNodes[0].data
                        y=  ymin.childNodes[0].data
                        xm= xmax.childNodes[0].data
                        ym= ymax.childNodes[0].data
                        li.append((classs,x,y,xm,ym))
                    for sett in li:
                        cla=sett[0]
                        xmi1=sett[0+1]
                        ymi1=sett[0+2]
                        xma1=sett[0+3]
                        yma1=sett[0+4]
                        bbs = ia.BoundingBoxesOnImage([ia.BoundingBox(x1=float(xmi1), y1=float(ymi1), x2=float(xma1), y2=float(yma1))],image.shape)
                        seq = iaa.Sequential([
                                iaa.Affine(shear=-22
                                           ) # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
                                ])
                        seq_det = seq.to_deterministic()
                        image_aug = seq_det.augment_images([image])[0]
                        bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]
                    
                        for i in range(len(bbs.bounding_boxes)):
                            before = bbs.bounding_boxes[i]
                            after = bbs_aug.bounding_boxes[i]
                            image_before = bbs.draw_on_image(image, thickness=2)
                            image_after = bbs_aug.draw_on_image(image_aug, thickness=0, color=[0, 0, 255])
                            updatexmlli.append((cla,after.x1,after.y1,after.x2,after.y2))
                            cv2.imwrite(dirpath+allfilenames+"_"+"shear_left"+str(count)+".jpg",image_after)        
                    root=ET.Element("annotation")
                    fold=ET.SubElement(root,"folder")
                    fold.text="augumentation"
                    xlfilename=ET.SubElement(root,"filename")
                    xlfilename.text=allfilenames+"_shear_left"+".jpg"
                    xlpath=ET.SubElement(root,"path")
                    xlpath.text=dirpath                   
                    source=ET.Element("source")
                    root.append(source)              
                    database=ET.SubElement(source,"database")
                    database.text="Unknown"              
                    size=ET.Element("size")
                    root.append(size)
                    width=ann.getElementsByTagName('width')[0]
                    wi = width.childNodes[0].data                    
                    xlwidth=ET.SubElement(size,"width")
                    xlwidth.text=wi                        
                    height=ann.getElementsByTagName('height')[0]
                    hei = height.childNodes[0].data
                    xlheight=ET.SubElement(size,"height")
                    xlheight.text=hei                           
                    depth=ann.getElementsByTagName('depth')[0]
                    de = depth.childNodes[0].data
                    xldepth=ET.SubElement(size,"depth")
                    xldepth.text=de
                    segment=ET.SubElement(root,"segmented")
                    segment.text="0"
                    for val in updatexmlli:
                        model=val[0]
                        cox=int(val[0+1])
                        coy=int(val[0+2])
                        comx=int(val[0+3])
                        comy=int(val[0+4])
                        print(model,cox,coy,comx,comy)
                        xlobject=ET.Element("object")
                        root.append(xlobject)
                        xlbname=ET.SubElement(xlobject,"name")
                        xlbname.text=model
                        pose=ET.SubElement(xlobject,"pose")
                        pose.text="Unspecified"
                        truncate=ET.SubElement(xlobject,"truncated")
                        truncate.text="0"
                        difficult=ET.SubElement(xlobject,"difficult")
                        difficult.text="0"                        
                        bndbox=ET.SubElement(xlobject,"bndbox")
                        tree = ET.ElementTree(root)
                        xlxmin=ET.SubElement(bndbox,"xmin")
                        xlxmin.text=str(cox)
                        xlymin=ET.SubElement(bndbox,"ymin")
                        xlymin.text=str(coy)
                        xlxax=ET.SubElement(bndbox,"xmax")
                        xlxax.text=str(comx)
                        xlymax=ET.SubElement(bndbox,"ymax")
                        xlymax.text=str(comy)                        
                    tree = ET.ElementTree(root)
                    fname=allfilenames+"_"+"shear_left"+str(count1)+".xml"
                    with open(os.path.join(dirpath,fname), "w") as fh:
                        tree.write(fh)
                count=count+1
                count1=count1+1
                updatexmlli=[]
                li=[]
                end=time.time()
                print("shear_left"+"----"+str(end - start))
    def rotate_boundbox(self):
        start=time.time()
        count=0
        count1=0
        global li
        li=[]
        global boundupdateli
        boundupdateli=[]
        global filenamu
        filenamu="Egypt_vs_Uruguay"
        global updatexmlli
        updatexmlli=[]
        for i in sorted(os.listdir(path)):
            filepath=os.path.join(path,i)
            if filepath.endswith(".jpg"):
                imgpa=filepath
                xmll=i.split('.')[0]
                xmlll=xmll+'.xml'
                new=i.split('Egypt_vs_Uruguay')[0]
                xmllll=os.path.join(path,xmlll)
                if xmllll.endswith('.xml'):
                    xmlp=xmllll
                    image=cv2.imread(imgpa)
                    a=xml.dom.minidom.parse(xmlp)
                    ann = a.documentElement
                    collections=ann.getElementsByTagName('object')
                    objects=ann.getElementsByTagName('object')
                    coun=0
                    for co in collections:
                        k=co.getElementsByTagName('name')[0]
                        classs= k.childNodes[0].data
                        xmin=co.getElementsByTagName('xmin')[0]
                        ymin=co.getElementsByTagName('ymin')[0]
                        xmax=co.getElementsByTagName('xmax')[0]
                        ymax=co.getElementsByTagName('ymax')[0]
                        x=  xmin.childNodes[0].data
                        y=  ymin.childNodes[0].data
                        xm= xmax.childNodes[0].data
                        ym= ymax.childNodes[0].data
                        li.append((classs,x,y,xm,ym))
                    for sett in li:
                        cla=sett[0]
                        xmi1=sett[0+1]
                        ymi1=sett[0+2]
                        xma1=sett[0+3]
                        yma1=sett[0+4]
                        bbs = ia.BoundingBoxesOnImage([ia.BoundingBox(x1=float(xmi1), y1=float(ymi1), x2=float(xma1), y2=float(yma1))],image.shape)
                        seq = iaa.Sequential([
                                iaa.Affine(rotate=5,scale=(0.9,0.9)
                                           ) # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
                                ])
                        seq_det = seq.to_deterministic()
                        image_aug = seq_det.augment_images([image])[0]
                        bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]
                    
                        for i in range(len(bbs.bounding_boxes)):
                            before = bbs.bounding_boxes[i]
                            after = bbs_aug.bounding_boxes[i]
                            image_before = bbs.draw_on_image(image, thickness=2)
                            image_after = bbs_aug.draw_on_image(image_aug, thickness=0, color=[0, 0, 255])
                            updatexmlli.append((cla,after.x1,after.y1,after.x2,after.y2))
                            cv2.imwrite(dirpath+allfilenames+"_"+"rotate_box"+str(count)+".jpg",image_after)               
                    root=ET.Element("annotation")
                    fold=ET.SubElement(root,"folder")
                    fold.text="augumentation"
                    xlfilename=ET.SubElement(root,"filename")
                    xlfilename.text=allfilenames+"_rotate_box"+".jpg"
                    xlpath=ET.SubElement(root,"path")
                    xlpath.text=dirpath                   
                    source=ET.Element("source")
                    root.append(source)               
                    database=ET.SubElement(source,"database")
                    database.text="Unknown"               
                    size=ET.Element("size")
                    root.append(size)
                    width=ann.getElementsByTagName('width')[0]
                    wi = width.childNodes[0].data
                    xlwidth=ET.SubElement(size,"width")
                    xlwidth.text=wi                      
                    height=ann.getElementsByTagName('height')[0]
                    hei = height.childNodes[0].data
                    xlheight=ET.SubElement(size,"height")
                    xlheight.text=hei                            
                    depth=ann.getElementsByTagName('depth')[0]
                    de = depth.childNodes[0].data
                    xldepth=ET.SubElement(size,"depth")
                    xldepth.text=de
                    segment=ET.SubElement(root,"segmented")
                    segment.text="0"
                    for val in updatexmlli:
                        model=val[0]
                        cox=int(val[0+1])
                        coy=int(val[0+2])
                        comx=int(val[0+3])
                        comy=int(val[0+4])
                        xlobject=ET.Element("object")
                        root.append(xlobject)
                        xlbname=ET.SubElement(xlobject,"name")
                        xlbname.text=model
                        pose=ET.SubElement(xlobject,"pose")
                        pose.text="Unspecified"
                        truncate=ET.SubElement(xlobject,"truncated")
                        truncate.text="0"
                        difficult=ET.SubElement(xlobject,"difficult")
                        difficult.text="0"                      
                        bndbox=ET.SubElement(xlobject,"bndbox")
                        tree = ET.ElementTree(root)
                        xlxmin=ET.SubElement(bndbox,"xmin")
                        xlxmin.text=str(cox)
                        xlymin=ET.SubElement(bndbox,"ymin")
                        xlymin.text=str(coy)
                        xlxax=ET.SubElement(bndbox,"xmax")
                        xlxax.text=str(comx)
                        xlymax=ET.SubElement(bndbox,"ymax")
                        xlymax.text=str(comy)                       
                    tree = ET.ElementTree(root)
                    fname=allfilenames+"_"+"rotate_box"+str(count1)+".xml"
                    with open(os.path.join(dirpath,fname), "w") as fh:
                        tree.write(fh)
                count=count+1
                count1=count1+1
                updatexmlli=[]
                li=[]
                end=time.time()
                print("rotate_box"+"----"+str(end - start))
    def Resize(self):
        start=time.time()
        count=0
        count1=0
        global filenamu
        filenamu="Egypt_vs_Uruguay"
        global li
        li=[]
        global boundupdateli
        boundupdateli=[]
        global updatexmlli
        updatexmlli=[]
        for i in sorted(os.listdir(path)):
            filepath=os.path.join(path,i)
            if filepath.endswith(".jpg"):
                imgpa=filepath
                xmll=i.split('.')[0]
                xmlll=xmll+'.xml'
                new=i.split('Egypt_vs_Uruguay')[0]
                xmllll=os.path.join(path,xmlll)
                if xmllll.endswith('.xml'):
                    xmlp=xmllll
                    image=cv2.imread(imgpa)
                    a=xml.dom.minidom.parse(xmlp)
                    ann = a.documentElement                               
                    collections=ann.getElementsByTagName('object')
                    objects=ann.getElementsByTagName('object')
                    fi=ann.getElementsByTagName('filename')[0]
                    filna=fi.childNodes[0].data
                    pathn=ann.getElementsByTagName('path')[0]
                    pan = pathn.childNodes[0].data
                    coun=0
                    for co in collections:
                        k=co.getElementsByTagName('name')[0]
                        classs= k.childNodes[0].data
                        xmin=co.getElementsByTagName('xmin')[0]
                        ymin=co.getElementsByTagName('ymin')[0]
                        xmax=co.getElementsByTagName('xmax')[0]
                        ymax=co.getElementsByTagName('ymax')[0]
                        x=  xmin.childNodes[0].data
                        y=  ymin.childNodes[0].data
                        xm= xmax.childNodes[0].data
                        ym= ymax.childNodes[0].data
                        li.append((classs,x,y,xm,ym))
                    for sett in li:
                        cla=sett[0]
                        xmi1=sett[0+1]
                        ymi1=sett[0+2]
                        xma1=sett[0+3]
                        yma1=sett[0+4]
                        bbs = ia.BoundingBoxesOnImage([ia.BoundingBox(x1=float(xmi1), y1=float(ymi1), x2=float(xma1), y2=float(yma1))],image.shape)
                        seq = iaa.Sequential([
                                iaa.Affine(translate_px={"x": 50, "y": 50},scale=(0.5, 0.5)) # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
                                ])
                        seq_det = seq.to_deterministic()
                        image_aug = seq_det.augment_images([image])[0]
                        bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]
                    
                        for i in range(len(bbs.bounding_boxes)):
                            before = bbs.bounding_boxes[i]
                            after = bbs_aug.bounding_boxes[i]
                            image_before = bbs.draw_on_image(image, thickness=2)
                            image_after = bbs_aug.draw_on_image(image_aug, thickness=0, color=[0, 0, 255])
                            updatexmlli.append((cla,after.x1,after.y1,after.x2,after.y2))
                            cv2.imwrite(dirpath+allfilenames+"_"+"resize"+str(count)+".jpg",image_after)                                      
                    root=ET.Element("annotation")
                    fold=ET.SubElement(root,"folder")
                    fold.text="augumentation"
                    xlfilename=ET.SubElement(root,"filename")
                    xlfilename.text=allfilenames+"_resize"+".jpg"
                    xlpath=ET.SubElement(root,"path")
                    xlpath.text=dirpath                 
                    source=ET.Element("source")
                    root.append(source)               
                    database=ET.SubElement(source,"database")
                    database.text="Unknown"              
                    size=ET.Element("size")
                    root.append(size)
                    width=ann.getElementsByTagName('width')[0]
                    wi = width.childNodes[0].data                    
                    xlwidth=ET.SubElement(size,"width")
                    xlwidth.text=wi                       
                    height=ann.getElementsByTagName('height')[0]
                    hei = height.childNodes[0].data
                    xlheight=ET.SubElement(size,"height")
                    xlheight.text=hei                            
                    depth=ann.getElementsByTagName('depth')[0]
                    de = depth.childNodes[0].data
                    xldepth=ET.SubElement(size,"depth")
                    xldepth.text=de
                    segment=ET.SubElement(root,"segmented")
                    segment.text="0"
                    for val in updatexmlli:
                        model=val[0]
                        cox=int(val[0+1])
                        coy=int(val[0+2])
                        comx=int(val[0+3])
                        comy=int(val[0+4])
                        xlobject=ET.Element("object")
                        root.append(xlobject)
                        xlbname=ET.SubElement(xlobject,"name")
                        xlbname.text=model
                        pose=ET.SubElement(xlobject,"pose")
                        pose.text="Unspecified"
                        truncate=ET.SubElement(xlobject,"truncated")
                        truncate.text="0"
                        difficult=ET.SubElement(xlobject,"difficult")
                        difficult.text="0"                       
                        bndbox=ET.SubElement(xlobject,"bndbox")
                        tree = ET.ElementTree(root)
                        xlxmin=ET.SubElement(bndbox,"xmin")
                        xlxmin.text=str(cox)
                        xlymin=ET.SubElement(bndbox,"ymin")
                        xlymin.text=str(coy)
                        xlxax=ET.SubElement(bndbox,"xmax")
                        xlxax.text=str(comx)
                        xlymax=ET.SubElement(bndbox,"ymax")
                        xlymax.text=str(comy)
                        
                    tree = ET.ElementTree(root)
                    fname=allfilenames+"_"+"resize"+str(count1)+".xml"
                    with open(os.path.join(dirpath,fname), "w") as fh:
                        tree.write(fh)
                count=count+1
                count1=count1+1
                updatexmlli=[]
                li=[]
                end=time.time()
                print("resize"+"----"+str(end - start))        
class WorkerThread(QtCore.QThread):
    def __init__(self,parent=None):
        super(WorkerThread,self).__init__(parent)       
    def run(self):
        time.sleep(0)
        print("Thread is Done")       
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui= Ui_Dialog()
    ui.setWindowTitle('Image Augumentation')
    ui.resize(1047, 558)
    ui.move(300,300)
    ui.show()
    ui.resize(1920,1080)
    sys.exit(app.exec_())
   
    

