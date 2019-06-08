# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from network import fast_style_transfer
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
from PyQt5.QtCore import *
from os import listdir
from PIL import Image
import matplotlib.pyplot as plt

style=['candy','cubist','mosaic','muse','rain','scream','shipwreck','starry','udnie','wave']
seq=0  # style[seq]
img=''
flag_t='p'
img_odd=''
result=''
#	原始图像
img_new=''
#	转换后图像
img_show=''
#	两个图像横向拼接后图像
img_style=''
#	原始风格图像
img_path=list(range(0,10))
#	原始图像路径

for i in range(0,10):
    img_path[i]='styles/'+style[i]+'.jpg'
cnn = fast_style_transfer()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 960))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menuBar)
        self.OpenImage = QtWidgets.QAction(MainWindow)
        self.OpenImage.setObjectName("OpenImage")
        self.SaveImage = QtWidgets.QAction(MainWindow)
        self.SaveImage.setObjectName("SaveImage")
        self.ActionExit = QtWidgets.QAction(MainWindow)
        self.ActionExit.setObjectName("ActionExit")
        self.ActionDemo = QtWidgets.QAction(MainWindow)
        self.ActionDemo.setObjectName("ActionDemo")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.ActionInfo = QtWidgets.QAction(MainWindow)
        self.ActionInfo.setObjectName("ActionInfo")
        self.Actionhomepage = QtWidgets.QAction(MainWindow)
        self.Actionhomepage.setObjectName("Actionhomepage")
        self.FreshImage = QtWidgets.QAction(MainWindow)
        self.FreshImage.setObjectName("FreshImage")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")
        self.action6 = QtWidgets.QAction(MainWindow)
        self.action6.setObjectName("action6")
        self.action7 = QtWidgets.QAction(MainWindow)
        self.action7.setObjectName("action7")
        self.action8 = QtWidgets.QAction(MainWindow)
        self.action8.setObjectName("action8")
        self.action9 = QtWidgets.QAction(MainWindow)
        self.action9.setObjectName("action9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_show = QtWidgets.QAction(MainWindow)
        self.action_show.setObjectName("action_show")
        self.action_example = QtWidgets.QAction(MainWindow)
        self.action_example.setObjectName("action_example")
        self.menu_2.addAction(self.action1)
        self.menu_2.addAction(self.action2)
        self.menu_2.addAction(self.action3)
        self.menu_2.addAction(self.action4)
        self.menu_2.addAction(self.action5)
        self.menu_2.addAction(self.action6)
        self.menu_2.addAction(self.action7)
        self.menu_2.addAction(self.action8)
        self.menu_2.addAction(self.action9)
        self.menu_2.addAction(self.action_10)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.OpenImage)
        self.menu.addAction(self.SaveImage)
        self.menu.addAction(self.FreshImage)
        self.menu.addSeparator()
        self.menu.addAction(self.ActionExit)
        self.menu_3.addAction(self.action_show)
        self.menu_3.addAction(self.action_example)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.ActionExit.triggered.connect(MainWindow.close)
        self.OpenImage.triggered.connect(MainWindow.open)
        self.SaveImage.triggered.connect(MainWindow.save)
        self.FreshImage.triggered.connect(MainWindow.fresh)
        self.action1.triggered.connect(MainWindow.changestyle1)
        self.action2.triggered.connect(MainWindow.changestyle2)
        self.action_show.triggered.connect(MainWindow.changestyleshow)
        self.action3.triggered.connect(MainWindow.changestyle3)
        self.action4.triggered.connect(MainWindow.changestyle4)
        self.action5.triggered.connect(MainWindow.changestyle5)
        self.action6.triggered.connect(MainWindow.changestyle6)
        self.action7.triggered.connect(MainWindow.changestyle7)
        self.action8.triggered.connect(MainWindow.changestyle8)
        self.action9.triggered.connect(MainWindow.changestyle9)
        self.action_10.triggered.connect(MainWindow.changestyle10)
        self.action_example.triggered.connect(MainWindow.example)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "风格"))
        self.menu_3.setTitle(_translate("MainWindow", "开始转换"))
        self.OpenImage.setText(_translate("MainWindow", "打开"))
        self.SaveImage.setText(_translate("MainWindow", "保存"))
        self.ActionExit.setText(_translate("MainWindow", "关闭"))
        self.ActionDemo.setText(_translate("MainWindow", "howtodo"))
        self.action_5.setText(_translate("MainWindow", "平台信息"))
        self.ActionInfo.setText(_translate("MainWindow", "平台信息"))
        self.Actionhomepage.setText(_translate("MainWindow", "课程主页"))
        self.FreshImage.setText(_translate("MainWindow", "清空"))
        self.action1.setText(_translate("MainWindow", "candy"))
        self.action2.setText(_translate("MainWindow", "cubist"))
        self.action3.setText(_translate("MainWindow", "mosaic"))
        self.action4.setText(_translate("MainWindow", "muse"))
        self.action5.setText(_translate("MainWindow", "rain"))
        self.action6.setText(_translate("MainWindow", "scream"))
        self.action7.setText(_translate("MainWindow", "shipwreck"))
        self.action8.setText(_translate("MainWindow", "starry"))
        self.action9.setText(_translate("MainWindow", "udnie"))
        self.action_10.setText(_translate("MainWindow", "wave"))
        self.action_show.setText(_translate("MainWindow", "转换"))
        self.action_example.setText(_translate("MainWindow", "示例"))

    def open(self):
        global  img_odd,img,img_new,flag_t
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','JPEG Files(*.jpg);PNG Files(*.png);all files(*.*)')
        print(openfile_name)
        if (openfile_name[0]!=''):
            flag_t='a';
            img = cv2.imread(openfile_name[0])  # 读取图像
            img_odd = cv2.imread(openfile_name[0])  # 读取图像
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
            x = img.shape[1]  # 获取图像大小
            y = img.shape[0]
            self.zoomscale = 1  # 图片放缩尺度
            frame = QImage(img, x, y, x * 3, QImage.Format_RGB888)
            #frame = QtGui.QImage(img2[:],img2.shape[1], img2.shape[0],img2.shape[1] * 3, QtGui.QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            # self.item.setScale(self.zoomscale)
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView.setScene(self.scene)
            #cv2.imshow(img)
    def save(self):
        file_path =  QFileDialog.getSaveFileName(self,"保存文件","" ,"JPEG Files(*.jpg);all files(*.*)")
        print( type(file_path[0]))
        if file_path[0] != '':
            cv2.imwrite(file_path[0], cv2.cvtColor(256 * img_new, cv2.COLOR_BGR2RGB),[int(cv2.IMWRITE_JPEG_QUALITY),95])
    def fresh(self):
        global flag_t;
        flag_t='p'
        img = cv2.imread('blank.jpg')  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        self.zoomscale = 1  # 图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)
    def changestyle1(self):
        global seq,img_new;
        seq = 0;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyle2(self):
        global seq,img_new;
        seq = 1;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def changestyle3(self):
        global seq,img_new;
        seq = 2;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyle4(self):
        global seq,img_new;
        seq = 3;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyle5(self):
        global seq,img_new;
        seq = 4;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyle6(self):
        global seq,img_new;
        seq = 5;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyle7(self):
        global seq,img_new;
        seq = 6;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyle8(self):
        global seq,img_new;
        seq = 7;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyle9(self):
        global seq,img_new;
        seq = 8;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyle10(self):
        global seq,img_new;
        seq = 9;
        img = cv2.imread(img_path[seq])  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def  example (self):
        img = cv2.imread('samples_'+style[seq]+'/sample_0.jpg')  # 读取图像
        cv2.imshow('style',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def changestyleshow(self):
        global img_new

        if flag_t=='a':
            img_new=cnn.transfer(img_odd, style[seq])
            #img =np.concatenate((cv2.cvtColor(img_odd, cv2.COLOR_BGR2RGB), np.uint8(img_new*255)),axis=1)
            img = np.uint8(img_new*255)
            x = img.shape[1]  # 获取图像大小
            y = img.shape[0]
            self.zoomscale = 1  # 图片放缩尺度
            frame = QImage(img, x, y, x*3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            #self.item.setScale(self.zoomscale)
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView.setScene(self.scene)
            pass
