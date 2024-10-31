# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Start.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Start(object):
    def setupUi(self, Start):
        if not Start.objectName():
            Start.setObjectName(u"Start")
        Start.resize(493, 249)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Start.sizePolicy().hasHeightForWidth())
        Start.setSizePolicy(sizePolicy)
        Start.setMinimumSize(QSize(350, 200))
        Start.setMaximumSize(QSize(500, 400))
        Start.setAutoFillBackground(False)
        Start.setStyleSheet(u"")
        self.centralwidget = QWidget(Start)
        self.centralwidget.setObjectName(u"centralwidget")
        self.but_login = QPushButton(self.centralwidget)
        self.but_login.setObjectName(u"but_login")
        self.but_login.setGeometry(QRect(276, 120, 131, 41))
        font = QFont()
        font.setPointSize(12)
        self.but_login.setFont(font)
        self.but_new_login = QPushButton(self.centralwidget)
        self.but_new_login.setObjectName(u"but_new_login")
        self.but_new_login.setGeometry(QRect(96, 120, 131, 41))
        self.but_new_login.setFont(font)
        self.label_user = QLabel(self.centralwidget)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(170, 40, 291, 20))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.label_user.setFont(font1)
        self.label_photo = QLabel(self.centralwidget)
        self.label_photo.setObjectName(u"label_photo")
        self.label_photo.setGeometry(QRect(20, 10, 131, 81))
        self.label_photo.setStyleSheet(u"image: url(:/newPrefix/default_user.png);")
        Start.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Start)
        self.statusbar.setObjectName(u"statusbar")
        Start.setStatusBar(self.statusbar)

        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)
    # setupUi

    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"MainWindow", None))
        self.but_login.setText(QCoreApplication.translate("Start", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.but_new_login.setText(QCoreApplication.translate("Start", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_user.setText(QCoreApplication.translate("Start", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043f\u043e\u043b\u044c\u0437\u0432\u0430\u0442\u0435\u043b\u0438: None", None))
        self.label_photo.setText("")
    # retranslateUi

