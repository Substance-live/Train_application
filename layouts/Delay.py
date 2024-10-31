# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Delay.ui'
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
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_Delay(object):
    def setupUi(self, Delay):
        if not Delay.objectName():
            Delay.setObjectName(u"Delay")
        Delay.resize(181, 144)
        self.centralwidget = QWidget(Delay)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(30, 10, 151, 31))
        self.but_ok = QPushButton(self.centralwidget)
        self.but_ok.setObjectName(u"but_ok")
        self.but_ok.setGeometry(QRect(30, 80, 121, 28))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(30, 50, 81, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 50, 31, 16))
        Delay.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Delay)
        self.statusbar.setObjectName(u"statusbar")
        Delay.setStatusBar(self.statusbar)

        self.retranslateUi(Delay)

        QMetaObject.connectSlotsByName(Delay)
    # setupUi

    def retranslateUi(self, Delay):
        Delay.setWindowTitle(QCoreApplication.translate("Delay", u"MainWindow", None))
        self.label_1.setText(QCoreApplication.translate("Delay", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0443", None))
        self.but_ok.setText(QCoreApplication.translate("Delay", u"\u043e\u043a", None))
        self.label.setText(QCoreApplication.translate("Delay", u"\u041c\u0418\u041d", None))
    # retranslateUi

