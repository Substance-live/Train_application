# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewLogin.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_NewLogin(object):
    def setupUi(self, NewLogin):
        if not NewLogin.objectName():
            NewLogin.setObjectName(u"NewLogin")
        NewLogin.resize(245, 218)
        self.centralwidget = QWidget(NewLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_main = QLabel(self.centralwidget)
        self.label_main.setObjectName(u"label_main")
        self.label_main.setGeometry(QRect(20, 20, 201, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_main.setFont(font)
        self.button_ok = QPushButton(self.centralwidget)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setGeometry(QRect(24, 160, 200, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.button_ok.setFont(font1)
        self.entry_login = QLineEdit(self.centralwidget)
        self.entry_login.setObjectName(u"entry_login")
        self.entry_login.setGeometry(QRect(110, 80, 113, 22))
        self.entry_passwd = QLineEdit(self.centralwidget)
        self.entry_passwd.setObjectName(u"entry_passwd")
        self.entry_passwd.setGeometry(QRect(110, 120, 113, 22))
        self.label_log = QLabel(self.centralwidget)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setGeometry(QRect(20, 80, 71, 21))
        self.label_log.setFont(font1)
        self.label_passwd = QLabel(self.centralwidget)
        self.label_passwd.setObjectName(u"label_passwd")
        self.label_passwd.setGeometry(QRect(20, 120, 71, 21))
        self.label_passwd.setFont(font1)
        NewLogin.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(NewLogin)
        self.statusbar.setObjectName(u"statusbar")
        NewLogin.setStatusBar(self.statusbar)

        self.retranslateUi(NewLogin)

        QMetaObject.connectSlotsByName(NewLogin)
    # setupUi

    def retranslateUi(self, NewLogin):
        NewLogin.setWindowTitle(QCoreApplication.translate("NewLogin", u"Avtorization", None))
        self.label_main.setText(QCoreApplication.translate("NewLogin", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.button_ok.setText(QCoreApplication.translate("NewLogin", u"OK", None))
        self.label_log.setText(QCoreApplication.translate("NewLogin", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_passwd.setText(QCoreApplication.translate("NewLogin", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

