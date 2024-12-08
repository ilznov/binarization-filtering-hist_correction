import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import cv2 as cv
import numpy as np
import concurrent.futures
import time
import matplotlib.pyplot as plt
from threading import Lock
from scipy.ndimage import uniform_filter
from histogram import Histogram
import filters


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1380, 800))
        MainWindow.setStyleSheet("background-color: rgb(122, 178, 211);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_Pictures = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Pictures.setObjectName("horizontalLayout_Pictures")
        self.label_Original = QtWidgets.QLabel(self.centralwidget, alignment=Qt.AlignCenter)
        self.label_Original.setMinimumSize(QtCore.QSize(450, 450))
        self.label_Original.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Original.setText("")
        self.label_Original.setObjectName("label_Original")
        self.horizontalLayout_Pictures.addWidget(self.label_Original)
        self.label_Edit = QtWidgets.QLabel(self.centralwidget, alignment=Qt.AlignCenter)
        self.label_Edit.setMinimumSize(QtCore.QSize(450, 450))
        self.label_Edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Edit.setText("")
        self.label_Edit.setObjectName("label_Edit")
        self.horizontalLayout_Pictures.addWidget(self.label_Edit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_Pictures)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 450))
        self.groupBox.setMaximumSize(QtCore.QSize(444, 16777215))
        self.groupBox.setStyleSheet("background-color: rgb(74, 98, 138);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_Histogram = Histogram(self.groupBox)
        self.label_Histogram.setMinimumSize(QtCore.QSize(420, 200))
        self.label_Histogram.setMaximumSize(QtCore.QSize(420, 200))
        self.label_Histogram.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Histogram.setProperty("text", "")
        self.label_Histogram.setObjectName("label_Histogram")
        self.horizontalLayout_4.addWidget(self.label_Histogram)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setMinimumSize(QtCore.QSize(380, 500))
        self.scrollArea.setMaximumSize(QtCore.QSize(380, 16777215))
        self.scrollArea.setStyleSheet("background-color: rgb(122, 178, 211);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 347, 1053))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_Hist = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Hist.setMinimumSize(QtCore.QSize(324, 0))
        self.groupBox_Hist.setStyleSheet("background-color: rgb(185, 229, 232);")
        self.groupBox_Hist.setObjectName("groupBox_Hist")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_Hist)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_Dark = QtWidgets.QPushButton(self.groupBox_Hist)
        self.pushButton_Dark.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_Dark.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Dark.setFont(font)
        self.pushButton_Dark.setObjectName("pushButton_Dark")
        self.horizontalLayout_21.addWidget(self.pushButton_Dark)
        self.spinBox_Dark = QtWidgets.QSpinBox(self.groupBox_Hist)
        self.spinBox_Dark.setMinimumSize(QtCore.QSize(50, 30))
        self.spinBox_Dark.setMaximumSize(QtCore.QSize(50, 30))
        self.spinBox_Dark.setSizeIncrement(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_Dark.setFont(font)
        self.spinBox_Dark.setMinimum(1)
        self.spinBox_Dark.setMaximum(10)
        self.spinBox_Dark.setObjectName("spinBox_Dark")
        self.horizontalLayout_21.addWidget(self.spinBox_Dark)
        self.gridLayout_4.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.pushButton_Bright = QtWidgets.QPushButton(self.groupBox_Hist)
        self.pushButton_Bright.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_Bright.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Bright.setFont(font)
        self.pushButton_Bright.setObjectName("pushButton_Bright")
        self.horizontalLayout_22.addWidget(self.pushButton_Bright)
        self.spinBox_Bright = QtWidgets.QSpinBox(self.groupBox_Hist)
        self.spinBox_Bright.setMinimumSize(QtCore.QSize(50, 30))
        self.spinBox_Bright.setMaximumSize(QtCore.QSize(50, 30))
        self.spinBox_Bright.setSizeIncrement(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_Bright.setFont(font)
        self.spinBox_Bright.setMinimum(1)
        self.spinBox_Bright.setMaximum(10)
        self.spinBox_Bright.setObjectName("spinBox_Bright")
        self.horizontalLayout_22.addWidget(self.spinBox_Bright)
        self.gridLayout_4.addLayout(self.horizontalLayout_22, 1, 0, 1, 1)
        self.pushButton_Linear_correction = QtWidgets.QPushButton(self.groupBox_Hist)
        self.pushButton_Linear_correction.setMinimumSize(QtCore.QSize(270, 50))
        self.pushButton_Linear_correction.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Linear_correction.setFont(font)
        self.pushButton_Linear_correction.setObjectName("pushButton_Linear_correction")
        self.gridLayout_4.addWidget(self.pushButton_Linear_correction, 2, 0, 1, 1)
        self.pushButton_Adaptive_Histogram_Equalization = QtWidgets.QPushButton(self.groupBox_Hist)
        self.pushButton_Adaptive_Histogram_Equalization.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_Adaptive_Histogram_Equalization.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Adaptive_Histogram_Equalization.setFont(font)
        self.pushButton_Adaptive_Histogram_Equalization.setObjectName("pushButton_Adaptive_Histogram_Equalization")
        self.gridLayout_4.addWidget(self.pushButton_Adaptive_Histogram_Equalization, 4, 0, 1, 1)
        self.pushButton_Histogram_Equalization = QtWidgets.QPushButton(self.groupBox_Hist)
        self.pushButton_Histogram_Equalization.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_Histogram_Equalization.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Histogram_Equalization.setFont(font)
        self.pushButton_Histogram_Equalization.setObjectName("pushButton_Histogram_Equalization")
        self.gridLayout_4.addWidget(self.pushButton_Histogram_Equalization, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_Hist, 2, 0, 1, 1)
        self.groupBox_Binarization = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.groupBox_Binarization.setFont(font)
        self.groupBox_Binarization.setStyleSheet("background-color: rgb(185, 229, 232);")
        self.groupBox_Binarization.setObjectName("groupBox_Binarization")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_Binarization)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider_Threshold = QtWidgets.QSlider(self.groupBox_Binarization)
        self.horizontalSlider_Threshold.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_Threshold.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_Threshold.setSizePolicy(sizePolicy)
        self.horizontalSlider_Threshold.setMinimumSize(QtCore.QSize(210, 15))
        self.horizontalSlider_Threshold.setMaximumSize(QtCore.QSize(210, 30))
        self.horizontalSlider_Threshold.setStyleSheet("")
        self.horizontalSlider_Threshold.setMinimum(1)
        self.horizontalSlider_Threshold.setMaximum(255)
        self.horizontalSlider_Threshold.setTracking(True)
        self.horizontalSlider_Threshold.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Threshold.setObjectName("horizontalSlider_Threshold")
        self.horizontalLayout.addWidget(self.horizontalSlider_Threshold)
        self.spinBox_Threshold = QtWidgets.QSpinBox(self.groupBox_Binarization)
        self.spinBox_Threshold.setMinimumSize(QtCore.QSize(50, 35))
        self.spinBox_Threshold.setMaximumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_Threshold.setFont(font)
        self.spinBox_Threshold.setMinimum(1)
        self.spinBox_Threshold.setMaximum(255)
        self.spinBox_Threshold.setObjectName("spinBox_Threshold")
        self.horizontalLayout.addWidget(self.spinBox_Threshold)
        self.gridLayout_5.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.pushButton_Compare_methods = QtWidgets.QPushButton(self.groupBox_Binarization)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Compare_methods.sizePolicy().hasHeightForWidth())
        self.pushButton_Compare_methods.setSizePolicy(sizePolicy)
        self.pushButton_Compare_methods.setMinimumSize(QtCore.QSize(270, 50))
        self.pushButton_Compare_methods.setMaximumSize(QtCore.QSize(270, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Compare_methods.setFont(font)
        self.pushButton_Compare_methods.setObjectName("pushButton_Compare_methods")
        self.gridLayout_5.addWidget(self.pushButton_Compare_methods, 4, 0, 1, 1)
        self.pushButton_Dithering = QtWidgets.QPushButton(self.groupBox_Binarization)
        self.pushButton_Dithering.setMinimumSize(QtCore.QSize(270, 50))
        self.pushButton_Dithering.setMaximumSize(QtCore.QSize(270, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_Dithering.setFont(font)
        self.pushButton_Dithering.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_Dithering.setObjectName("pushButton_Dithering")
        self.gridLayout_5.addWidget(self.pushButton_Dithering, 0, 0, 1, 1)
        self.checkBox_Binarization = QtWidgets.QCheckBox(self.groupBox_Binarization)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Binarization.sizePolicy().hasHeightForWidth())
        self.checkBox_Binarization.setSizePolicy(sizePolicy)
        self.checkBox_Binarization.setMinimumSize(QtCore.QSize(270, 50))
        self.checkBox_Binarization.setMaximumSize(QtCore.QSize(270, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Binarization.setFont(font)
        self.checkBox_Binarization.setObjectName("checkBox_Binarization")
        self.gridLayout_5.addWidget(self.checkBox_Binarization, 2, 0, 1, 1)
        self.groupBox_Binarization_OpenCV = QtWidgets.QGroupBox(self.groupBox_Binarization)
        self.groupBox_Binarization_OpenCV.setMinimumSize(QtCore.QSize(270, 220))
        self.groupBox_Binarization_OpenCV.setMaximumSize(QtCore.QSize(270, 220))
        self.groupBox_Binarization_OpenCV.setTitle("")
        self.groupBox_Binarization_OpenCV.setObjectName("groupBox_Binarization_OpenCV")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_Binarization_OpenCV)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Adaptive_Binarization_1 = QtWidgets.QPushButton(self.groupBox_Binarization_OpenCV)
        self.pushButton_Adaptive_Binarization_1.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_Adaptive_Binarization_1.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Adaptive_Binarization_1.setFont(font)
        self.pushButton_Adaptive_Binarization_1.setObjectName("pushButton_Adaptive_Binarization_1")
        self.gridLayout.addWidget(self.pushButton_Adaptive_Binarization_1, 2, 0, 1, 1)
        self.checkBox_OpenCV = QtWidgets.QCheckBox(self.groupBox_Binarization_OpenCV)
        self.checkBox_OpenCV.setMinimumSize(QtCore.QSize(220, 50))
        self.checkBox_OpenCV.setMaximumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_OpenCV.setFont(font)
        self.checkBox_OpenCV.setObjectName("checkBox_OpenCV")
        self.gridLayout.addWidget(self.checkBox_OpenCV, 0, 0, 1, 1)
        self.pushButton_Otsu_Binarization = QtWidgets.QPushButton(self.groupBox_Binarization_OpenCV)
        self.pushButton_Otsu_Binarization.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_Otsu_Binarization.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Otsu_Binarization.setFont(font)
        self.pushButton_Otsu_Binarization.setObjectName("pushButton_Otsu_Binarization")
        self.gridLayout.addWidget(self.pushButton_Otsu_Binarization, 1, 0, 1, 1)
        self.pushButton_Adaptive_Binarization_2 = QtWidgets.QPushButton(self.groupBox_Binarization_OpenCV)
        self.pushButton_Adaptive_Binarization_2.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_Adaptive_Binarization_2.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Adaptive_Binarization_2.setFont(font)
        self.pushButton_Adaptive_Binarization_2.setObjectName("pushButton_Adaptive_Binarization_2")
        self.gridLayout.addWidget(self.pushButton_Adaptive_Binarization_2, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_Binarization_OpenCV, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_Binarization, 0, 0, 1, 1)
        self.groupBox_Filters = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Filters.setMinimumSize(QtCore.QSize(270, 220))
        self.groupBox_Filters.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_Filters.setStyleSheet("background-color: rgb(185, 229, 232);")
        self.groupBox_Filters.setObjectName("groupBox_Filters")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_Filters)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Adaptive_Median_filter = QtWidgets.QPushButton(self.groupBox_Filters)
        self.pushButton_Adaptive_Median_filter.setMinimumSize(QtCore.QSize(270, 50))
        self.pushButton_Adaptive_Median_filter.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Adaptive_Median_filter.setFont(font)
        self.pushButton_Adaptive_Median_filter.setObjectName("pushButton_Adaptive_Median_filter")
        self.gridLayout_2.addWidget(self.pushButton_Adaptive_Median_filter, 2, 0, 1, 1)
        self.pushButton_Median_filter = QtWidgets.QPushButton(self.groupBox_Filters)
        self.pushButton_Median_filter.setMinimumSize(QtCore.QSize(270, 50))
        self.pushButton_Median_filter.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Median_filter.setFont(font)
        self.pushButton_Median_filter.setObjectName("pushButton_Median_filter")
        self.gridLayout_2.addWidget(self.pushButton_Median_filter, 1, 0, 1, 1)
        self.pushButton_Gauss_filter = QtWidgets.QPushButton(self.groupBox_Filters)
        self.pushButton_Gauss_filter.setMinimumSize(QtCore.QSize(270, 50))
        self.pushButton_Gauss_filter.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Gauss_filter.setFont(font)
        self.pushButton_Gauss_filter.setObjectName("pushButton_Gauss_filter")
        self.gridLayout_2.addWidget(self.pushButton_Gauss_filter, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_Filters, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        spacerItem2 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1380, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.retranslateUi(MainWindow)
        self.actionOpen.triggered.connect(self.loadImage)
        self.actionSave.triggered.connect(self.savePhoto)
        self.actionExit.triggered.connect(sys.exit)

        # Button "Dithering"
        self.pushButton_Dithering.clicked.connect(self.pushButton_Dithering_Clicked)

        self.checkBox_OpenCV.clicked.connect(self.checkBox_OpenCV_Clicked)

        self.pushButton_Otsu_Binarization.clicked.connect(
            self.pushButton_Otsu_Binarization_Clicked
        )
        self.pushButton_Adaptive_Binarization_1.clicked.connect(
            self.pushButton_Adaptive_Binarization_1_Clicked
        )
        self.pushButton_Adaptive_Binarization_2.clicked.connect(
            self.pushButton_Adaptive_Binarization_2_Clicked
        )

        self.pushButton_Gauss_filter.clicked.connect(
            self.pushButton_Gauss_filter_Clicked
        )
        self.pushButton_Median_filter.clicked.connect(
            self.pushButton_Median_filter_Clicked
        )
        self.pushButton_Adaptive_Median_filter.clicked.connect(
            self.pushButton_Adaptive_Median_filter_Clicked
        )

        self.checkBox_Binarization.clicked["bool"].connect(
            self.horizontalSlider_Threshold.setEnabled
        )
        self.checkBox_Binarization.clicked["bool"].connect(
            self.spinBox_Threshold.setEnabled
        )
        self.checkBox_Binarization.clicked["bool"].connect(
            self.pushButton_Dithering.setDisabled
        )
        self.checkBox_Binarization.clicked["bool"].connect(
            self.pushButton_Otsu_Binarization.setDisabled
        )
        self.checkBox_Binarization.clicked["bool"].connect(
            self.pushButton_Adaptive_Binarization_1.setDisabled
        )
        self.checkBox_Binarization.clicked["bool"].connect(
            self.pushButton_Adaptive_Binarization_2.setDisabled
        )
        self.checkBox_Binarization.clicked["bool"].connect(
            self.checkBox_OpenCV.setDisabled
        )
        self.checkBox_Binarization.clicked.connect(self.label_Edit.clear)

        self.horizontalSlider_Threshold.valueChanged["int"].connect(
            self.horizontalSlider_Threshold_scrolled
        )
        self.horizontalSlider_Threshold.valueChanged["int"].connect(
            self.spinBox_Threshold.setValue
        )
        self.spinBox_Threshold.valueChanged["int"].connect(
            self.horizontalSlider_Threshold.setValue
        )

        self.pushButton_Linear_correction.clicked.connect(
            self.pushButton_Linear_correction_Clicked)
        self.pushButton_Histogram_Equalization.clicked.connect(
            self.pushButton_Hist_Equalization_Clicked)
        self.pushButton_Adaptive_Histogram_Equalization.clicked.connect(
            self.pushButton_Adaptive_Histogram_Equalization_Clicked)
        
        self.spinBox_Dark.valueChanged["int"].connect(self.get_Dark_value)
        self.spinBox_Bright.valueChanged["int"].connect(self.get_Bright_value)

        
        self.pushButton_Dark.clicked.connect(self.pushButton_Dark_Clicked)
        self.pushButton_Bright.clicked.connect(self.pushButton_Bright_Clicked)




        # Button "Compare methods"
        self.pushButton_Compare_methods.clicked.connect(
            self.pushButton_Compare_methods_Clicked
        )

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # start
        self.Dark_value = 1
        self.Bright_value = 1
        self.filename = None
        self.filename_save = None
        self.result = None

    # ----------------------------------------------------------------

    def checkBox_OpenCV_Clicked(self):
        if self.checkBox_OpenCV.isChecked():
            self.pushButton_Adaptive_Binarization_2.setText(
                QtCore.QCoreApplication.translate(
                    "MainWindow", "Adaptive binarization (gaussian)"
                )
            )
        else:
            self.pushButton_Adaptive_Binarization_2.setText(
                QtCore.QCoreApplication.translate("MainWindow", "Sauvola method")
            )

    def pushButton_Compare_methods_Clicked(self):
        try:
            rows = 2
            columns = 4

            fig, ax = plt.subplots(
                nrows=rows, ncols=columns, figsize=(10, 7), sharex=True, sharey=True
            )

            b, g, r = cv.split(self.result)
            rgb_img = cv.merge([r, g, b])
            plt.gray()

            ax[0][0].imshow(rgb_img)
            ax[0][0].axis("off")
            ax[0][0].set_title("Original")

            res, threshold = self.otsu_binarization_cv(self.result)
            ax[0][1].imshow(res)
            ax[0][1].axis("off")
            ax[0][1].set_title("Otsu OpenCV\nThreshold is {}".format(int(threshold)))

            res = self.adaptive_binarization_cv(self.result, "mean")
            ax[0][2].imshow(res)
            ax[0][2].axis("off")
            ax[0][2].set_title("Adaptive binarization OpenCV (mean)")

            res = self.adaptive_binarization_mean(self.result)
            ax[0][3].imshow(res)
            ax[0][3].axis("off")
            ax[0][3].set_title("Adaptive binarization (mean)")

            res = self.dithering_t1(self.result)
            ax[1][0].imshow(res)
            ax[1][0].axis("off")
            ax[1][0].set_title("Dithering")

            res, threshold = self.otsu_binarization_thread(self.result)
            ax[1][1].imshow(res)
            ax[1][1].axis("off")
            ax[1][1].set_title("Otsu\nThreshold is {}".format(threshold))

            res = self.adaptive_binarization_cv(self.result, "gaussian")
            ax[1][2].imshow(res)
            ax[1][2].axis("off")
            ax[1][2].set_title("Adaptive binarization OpenCV (gaussian)")

            res = self.adaptive_binarization_sauvola(self.result)
            ax[1][3].imshow(res)
            ax[1][3].axis("off")
            ax[1][3].set_title("Sauvola method")

            fig.tight_layout()

            plt.show()
        except:
            self.checkImage()

    # ----------------------------------------------------------------

    def pushButton_Dithering_Clicked(self):
        try:
            # self.result_binarization = self.dithering(self.result)
            self.result_binarization = self.dithering_t1(self.result)
            tmp = self.checkSizeImage(self.result_binarization)
            self.setPhoto(tmp, 0)
        except Exception as e:
            print(f"Помилка: {e}")
            # self.checkImage()

    def pushButton_Otsu_Binarization_Clicked(self):
        try:
            if self.checkBox_OpenCV.isChecked():
                self.result_binarization, threshold = self.otsu_binarization_cv(
                    self.result
                )
            else:
                self.result_binarization, threshold = self.otsu_binarization_thread(
                    self.result
                )
            self.showThreshold(threshold)
            tmp = self.checkSizeImage(self.result_binarization)
            self.setPhoto(tmp, 0)
        except:
            self.checkImage()

    def pushButton_Adaptive_Binarization_1_Clicked(self):
        try:
            if self.checkBox_OpenCV.isChecked():
                self.result_binarization = self.adaptive_binarization_cv(
                    self.result, "mean"
                )
            else:
                self.result_binarization = self.adaptive_binarization_mean(self.result)
            tmp = self.checkSizeImage(self.result_binarization)
            self.setPhoto(tmp, 0)
        except:
            self.checkImage()

    def pushButton_Adaptive_Binarization_2_Clicked(self):
        try:
            if self.checkBox_OpenCV.isChecked():
                self.result_binarization = self.adaptive_binarization_cv(
                    self.result, "gaussian"
                )
            else:
                self.result_binarization = self.adaptive_binarization_sauvola(
                    self.result
                )
            tmp = self.checkSizeImage(self.result_binarization)
            self.setPhoto(tmp, 0)
        except:
            self.checkImage()

    # ----------------------------------------------------------------

    def horizontalSlider_Threshold_scrolled(self, value):
        try:
            self.result_binarization = self.binarization(self.result, value)
            tmp = self.checkSizeImage(self.result_binarization)
            self.setPhoto(tmp, 0)
        except Exception as error:
            print(error)
            self.checkImage()

    # ----------------------------------------------------------------
    def pushButton_Gauss_filter_Clicked(self):
        try:
            self.result_binarization = None
            self.result = filters.gaussOpenCV(self.result)
            # self.result = filters.gaussian_blur(self.result)
            tmp = self.checkSizeImage(self.result)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    def pushButton_Median_filter_Clicked(self):
        try:
            self.result_binarization = None
            self.result = filters.medianBlurOpenCV(self.result)
            tmp = self.checkSizeImage(self.result)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    def pushButton_Adaptive_Median_filter_Clicked(self):
        try:
            self.result_binarization = None
            self.result = filters.adaptiveMedian(self.result)
            tmp = self.checkSizeImage(self.result)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    # ----------------------------------------------------------------

    def get_Dark_value(self, value):
        self.Dark_value = value

    def get_Bright_value(self, value):
        self.Bright_value = value

    def pushButton_Dark_Clicked(self, value):
        try:
            self.result_binarization = None
            value=self.Dark_value/10
            self.result = cv.convertScaleAbs(self.result, alpha=value, beta=0)
            tmp = self.checkSizeImage(self.result)
            self.setPhoto(tmp, 0)
            self.setPhoto(tmp, 1)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    def pushButton_Bright_Clicked(self):
        try:
            self.result_binarization = None
            value=self.Bright_value/10 + 1
            self.result = cv.convertScaleAbs(self.result, alpha=value, beta=0)
            tmp = self.checkSizeImage(self.result)
            self.setPhoto(tmp, 0)
            self.setPhoto(tmp, 1)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    def pushButton_Linear_correction_Clicked(self):
        try:
            self.result_binarization = None
            self.result = self.linear_correction(self.result)
            tmp = self.checkSizeImage(self.result)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    def pushButton_Hist_Equalization_Clicked(self):
        try:
            self.result_binarization = None
            self.result = self.equalize_Hist_cv(self.result)
            # self.result = self.histogram_equalization(self.result)
            tmp = self.checkSizeImage(self.result)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    def pushButton_Adaptive_Histogram_Equalization_Clicked(self):
        try:
            self.result_binarization = None
            # self.result = self.adaptive_histogram_equalization(self.result)
            self.result = self.adaptive_histogram_equalization_cv(self.result)
            tmp = self.checkSizeImage(self.result)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result)
        except:
            self.checkImage()        


    # ----------------------------------------------------------------

    def loadImage(self):
        """
        This function will load the user selected image
        and set it to label using the setPhoto function
        """
        try:
            self.label_Edit.clear()
            self.result_binarization = None
            self.result = None
            self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
            str(self.filename)
            f = open(self.filename, "rb")
            chunk = f.read()
            chunk_arr = np.frombuffer(chunk, dtype=np.uint8)
            self.image = cv.imdecode(chunk_arr, cv.IMREAD_COLOR)
            f.close()
            tmp = self.checkSizeImage(self.image)
            self.setPhoto(tmp)
            self.show_histogram(self.image)
            self.result = self.image
        except:
            None

    def setPhoto(self, image, check=1):
        """
        This function will take image input and resize it
        only for display purpose and convert it to QImage
        to set at the label.
        """
        frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = QImage(
            frame,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            QImage.Format_RGB888,
        )
        if check == 1:
            self.label_Original.setPixmap(QtGui.QPixmap.fromImage(image))
        else:
            self.label_Edit.setPixmap(QtGui.QPixmap.fromImage(image))

    def savePhoto(self):
        """
        This function will save the result.
        """
        try:
            self.filename_save = QFileDialog.getSaveFileName(
                filter="png Image (*.png)"
            )[0]
            try:
                _, im_buf_arr = cv.imencode(".jpg", self.result_binarization)
            except:
                _, im_buf_arr = cv.imencode(".jpg", self.result)
            im_buf_arr.tofile(self.filename_save)
        except:
            self.errorSavePhoto()

    def showThreshold(self, threshold):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Threshold")
        msg.setText("Threshold is {}".format(threshold))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def check_Grayscale(self, img):
        if len(img.shape) == 2:
            out = np.copy(img)
        else:
            out = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return out

    def errorSavePhoto(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("ERROR")
        msg.setText("You have not edited the image or you have not uploaded the image!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def checkImage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("ERROR")
        msg.setText("You have not select a file!!!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def checkSizeImage(self, image):
        """
        This function will check the image's size
        and scale the image to fit window
        """
        height, width = image.shape[:2]
        if height >= width:
            k = self.label_Original.height() / height
            height = int(image.shape[0] * k)
            width = int(image.shape[1] * k)
        elif width > height:
            k = self.label_Original.width() / width
            height = int(image.shape[0] * k)
            width = int(image.shape[1] * k)
        math.floor(height)
        math.floor(width)
        return cv.resize(image, (width, height), interpolation=cv.INTER_AREA)

# --------------------------------------------------------------------


    def dithering_t1(self, img):
        print(img.shape)
        # Перетворення на чорно-біле зображення
        # GrayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY).astype(np.float32)
        GrayImage = self.check_Grayscale(img).astype(np.float32)

        Height, Width = GrayImage.shape[:2]

        for y in range(Height):
            for x in range(Width):
                old_value = GrayImage[y, x]
                new_value = 255 if old_value > 128 else 0
                GrayImage[y, x] = new_value
                quant_error = old_value - new_value

                # Розподілення помилки
                if x + 1 < Width:
                    GrayImage[y, x + 1] += quant_error * 7 / 16
                if x - 1 >= 0 and y + 1 < Height:
                    GrayImage[y + 1, x - 1] += quant_error * 3 / 16
                if y + 1 < Height:
                    GrayImage[y + 1, x] += quant_error * 5 / 16
                if x + 1 < Width and y + 1 < Height:
                    GrayImage[y + 1, x + 1] += quant_error * 1 / 16

        # Повертаємо результат з приведенням до допустимого діапазону
        return np.clip(GrayImage, 0, 255).astype(np.uint8)

    # Dithering
    def dithering(self, img):
        GrayImage = self.check_Grayscale(img)
        # GrayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        Height, Width = GrayImage.shape[:2]

        # start = time.perf_counter()

        for y in range(0, Height):
            for x in range(0, Width):
                old_value = GrayImage[y, x]
                new_value = 0
                if old_value > 128:
                    new_value = 255

                GrayImage[y, x] = new_value

                Error = old_value - new_value

                if x < Width - 1:
                    NewNumber = GrayImage[y, x + 1] + Error * 7 / 16
                    if NewNumber > 255:
                        NewNumber = 255
                    elif NewNumber < 0:
                        NewNumber = 0
                    GrayImage[y, x + 1] = NewNumber

                if x > 0 and y < Height - 1:
                    NewNumber = GrayImage[y + 1, x - 1] + Error * 3 / 16
                    if NewNumber > 255:
                        NewNumber = 255
                    elif NewNumber < 0:
                        NewNumber = 0
                    GrayImage[y + 1, x - 1] = NewNumber

                if y < Height - 1:
                    NewNumber = GrayImage[y + 1, x] + Error * 5 / 16
                    if NewNumber > 255:
                        NewNumber = 255
                    elif NewNumber < 0:
                        NewNumber = 0
                    GrayImage[y + 1, x] = NewNumber

                if y < Height - 1 and x < Width - 1:
                    NewNumber = GrayImage[y + 1, x + 1] + Error * 1 / 16
                    if NewNumber > 255:
                        NewNumber = 255
                    elif NewNumber < 0:
                        NewNumber = 0
                    GrayImage[y + 1, x + 1] = NewNumber

        # print(f"Finished", time.perf_counter() - start)
        # return res

        return GrayImage

    # Otsu Binarization OpenCV
    def otsu_binarization_cv(self, image):
        gray = self.check_Grayscale(image)
        threshold, binary = cv.threshold(
            gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU
        )
        return binary, threshold

    # Otsu Binarization thread
    def otsu_binarization_thread(self, img):
        H, W = img.shape[:2]
        # # BGR2GRAY
        # b = img[:, :, 0].copy()
        # g = img[:, :, 1].copy()
        # r = img[:, :, 2].copy()
        # # Gray scale
        # out = 0.2126 * r + 0.7152 * g + 0.0722 * b
        # out = out.astype(np.uint8)

        out = self.check_Grayscale(img)

        self.max_sigma = 0
        self.max_t = 0

        l = Lock()

        def _binarization(_t):
            v0 = out[np.where(out < _t)]
            m0 = np.mean(v0) if len(v0) > 0 else 0.0
            w0 = len(v0) / (H * W)
            v1 = out[np.where(out >= _t)]
            m1 = np.mean(v1) if len(v1) > 0 else 0.0
            w1 = len(v1) / (H * W)
            sigma = w0 * w1 * ((m0 - m1) ** 2)

            with l:
                if sigma > self.max_sigma:
                    self.max_sigma = sigma
                    self.max_t = _t

        # start = time.perf_counter()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for _t in range(1, 256):
                executor.submit(_binarization, _t)

        # print(f"Finished new", time.perf_counter() - start)

        # Binarization
        out[out < self.max_t] = 0
        out[out >= self.max_t] = 255

        return out, self.max_t

    # Adaptive binarization OpenCV
    def adaptive_binarization_cv(self, image, method: str):
        gray = self.check_Grayscale(image)

        if method == "mean":
            result = cv.adaptiveThreshold(
                gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 199, 5
            )
        elif method == "gaussian":
            result = cv.adaptiveThreshold(
                gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 199, 5
            )

        return result

    # Adaptive binarization (mean)
    def adaptive_binarization_mean(self, image, block_size=20, c=10):
        gray = self.check_Grayscale(image)
        # gray = cv.GaussianBlur(gray, (5, 5), 0)
        height, width = gray.shape

        # Створюємо пусте вихідне зображення
        binary = np.zeros_like(gray)
        # Розбиваємо зображення на блоки та застосовуємо бінарізацію до кожного блоку
        for i in range(0, height, block_size):
            for j in range(0, width, block_size):
                # Отримуємо поточний блок
                block = gray[i : i + block_size, j : j + block_size]

                # Обчислюємо порігове значення для блоку
                block_threshold = np.mean(block) - c
                # block_threshold = np.mean((np.max(block)+np.min(block))/2)

                # Бінарізуємо блок
                block_binary = np.where(block >= block_threshold, 255, 0)

                # Записуємо бінаризований блок у вихідне зображення
                binary[i : i + block_size, j : j + block_size] = block_binary

        return binary

    # Adaptive binarization Sauvola method
    def adaptive_binarization_sauvola(self, image, window_size=25, k=0.2, r=128):
        gray = self.check_Grayscale(image)
        height, width = gray.shape

        # Обчислення локального середнього значення за допомогою швидкого фільтра
        mean = uniform_filter(gray, window_size)

        # Обчислення локального стандартного відхилення за допомогою швидкого фільтра
        var = uniform_filter(gray * gray, window_size) - mean * mean
        std = np.sqrt(var)

        # Обчислення порогу Sauvola
        threshold = mean * (1 + k * (std / r - 1))

        # Застосування порогу до зображення
        binarized = np.zeros((height, width), dtype=np.uint8)
        binarized[gray > threshold] = 255

        return binarized

    # Binarization
    def binarization(self, img, a):
        # BGR2GRAY
        out = self.check_Grayscale(img)

        out[out < a] = 0
        out[out >= a] = 255

        return out

# --------------------------------------------------------------------

    def show_histogram(self, img):
        try:
            self.label_Histogram.canvas.axes.clear()
            self.label_Histogram.canvas.axes.axis("off")
            self.label_Histogram.canvas.axes.hist(img.ravel(), 256, [0, 256])
            self.label_Histogram.canvas.axes.grid()
            self.label_Histogram.canvas.draw()
        except:
            self.checkImage()

    def linear_correction(self, img):
        # img = self.check_Grayscale(image)
        H, W = img.shape[:2]
        min_val = np.min(img)
        max_val = np.max(img)

        for i in range(H):
            for j in range(W):
                img[i, j] = ((img[i, j] - min_val) / (max_val - min_val)) * 255

        print(img.shape)
        return img
    

    def equalize_Hist_cv(self, img):
        # GrayImage = self.check_Grayscale(img)
        GrayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        res = cv.equalizeHist(GrayImage)
        print(res.shape)
        return res
    
    def histogram_equalization(self, img):
        image = self.check_Grayscale(img)
        # Розрахунок гістограми
        hist, _ = np.histogram(image.flatten(), 256, [0, 256])
        cdf = hist.cumsum()  # розрахунок кумулятивної суми гістограми
        cdf = (cdf - cdf.min())*255/(cdf.max()-cdf.min())  # нормалізація CDF
        cdf = cdf.astype('uint8')  # перетворення типу на 'uint8'

        # Застосування CDF для виконання еквалізації гістограми
        img_equalized = cv.LUT(image, cdf)

        return img_equalized
    
    def adaptive_histogram_equalization_cv(self, img):
        image = self.check_Grayscale(img)
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

        # Застосування адаптивного вирівнювання гістограми
        clahe_image = clahe.apply(image)
        return clahe_image
    
    def adaptive_histogram_equalization(self, image, grid_size=(8, 8)):
        image = self.check_Grayscale(image)
        h, w = image.shape
        # Крок 1: Розбиття зображення на блоки
        block_h = h // grid_size[0]
        block_w = w // grid_size[1]

        # Створюємо порожню матрицю для нового зображення
        equalized_image = np.zeros_like(image)

        def manual_histogram_equalization(block):
            # Аналог глобального вирівнювання гістограми для кожного блоку
            hist = np.zeros(256)
            for pixel in block.flatten():
                    hist[pixel] += 1

            cdf = hist.cumsum()
            cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())

            equalized_block = np.interp(block.flatten(), range(0, 256), cdf_normalized).reshape(block.shape).astype(np.uint8)
            
            return equalized_block

        # Проходимо по кожному блоку і застосовуємо вирівнювання гістограми
        for i in range(0, h, block_h):
            for j in range(0, w, block_w):
                # Виділяємо блок зображення
                block = image[i:i+block_h, j:j+block_w]

                # Викликаємо функцію для вирівнювання гістограми для блоку
                block_equalized = manual_histogram_equalization(block)

                # Записуємо оброблений блок назад у результуюче зображення
                equalized_image[i:i+block_h, j:j+block_w] = block_equalized

        return equalized_image

# --------------------------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editor"))
        self.groupBox_Hist.setTitle(_translate("MainWindow", "Hist"))
        self.pushButton_Dark.setText(_translate("MainWindow", "Dark"))
        self.pushButton_Bright.setText(_translate("MainWindow", "Bright"))
        self.pushButton_Linear_correction.setText(_translate("MainWindow", "Linear correction"))
        self.pushButton_Adaptive_Histogram_Equalization.setText(_translate("MainWindow", "Adaptive Histogram equalization"))
        self.pushButton_Histogram_Equalization.setText(_translate("MainWindow", "Histogram equalization"))
        self.groupBox_Binarization.setTitle(_translate("MainWindow", "Binarization"))
        self.pushButton_Compare_methods.setText(_translate("MainWindow", "Compare methods"))
        self.pushButton_Dithering.setText(_translate("MainWindow", "Dithering"))
        self.checkBox_Binarization.setText(_translate("MainWindow", "Binarization"))
        self.pushButton_Adaptive_Binarization_1.setText(_translate("MainWindow", "Adaptive binarization (mean)"))
        self.checkBox_OpenCV.setText(_translate("MainWindow", "OpenCV"))
        self.pushButton_Otsu_Binarization.setText(_translate("MainWindow", "Otsu\'s binarization"))
        self.pushButton_Adaptive_Binarization_2.setText(_translate("MainWindow", "Adaptive binarization (Sauvola method)"))
        self.groupBox_Filters.setTitle(_translate("MainWindow", "Filters"))
        self.pushButton_Adaptive_Median_filter.setText(_translate("MainWindow", "Adaptive Median filter"))
        self.pushButton_Median_filter.setText(_translate("MainWindow", "Median filter"))
        self.pushButton_Gauss_filter.setText(_translate("MainWindow", "Gauss filter"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
