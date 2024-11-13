# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Profile.ui'
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
    QSizePolicy, QWidget)

class Ui_Profile(object):
    def setupUi(self, Profile):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(507, 295)
        self.centralwidget = QWidget(Profile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_photo = QLabel(self.centralwidget)
        self.label_photo.setObjectName(u"label_photo")
        self.label_photo.setGeometry(QRect(30, 30, 111, 101))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_photo.sizePolicy().hasHeightForWidth())
        self.label_photo.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        self.label_photo.setFont(font)
        self.label_photo.setLayoutDirection(Qt.LeftToRight)
        self.label_user = QLabel(self.centralwidget)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(160, 60, 161, 51))
        sizePolicy.setHeightForWidth(self.label_user.sizePolicy().hasHeightForWidth())
        self.label_user.setSizePolicy(sizePolicy)
        self.label_user.setFont(font)
        self.label_mail = QLabel(self.centralwidget)
        self.label_mail.setObjectName(u"label_mail")
        self.label_mail.setGeometry(QRect(160, 110, 141, 41))
        sizePolicy.setHeightForWidth(self.label_mail.sizePolicy().hasHeightForWidth())
        self.label_mail.setSizePolicy(sizePolicy)
        self.label_mail.setFont(font)
        self.but_edit = QPushButton(self.centralwidget)
        self.but_edit.setObjectName(u"but_edit")
        self.but_edit.setGeometry(QRect(42, 190, 181, 28))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.but_edit.sizePolicy().hasHeightForWidth())
        self.but_edit.setSizePolicy(sizePolicy1)
        self.but_edit.setFont(font)
        self.but_timetable = QPushButton(self.centralwidget)
        self.but_timetable.setObjectName(u"but_timetable")
        self.but_timetable.setGeometry(QRect(240, 190, 151, 28))
        sizePolicy1.setHeightForWidth(self.but_timetable.sizePolicy().hasHeightForWidth())
        self.but_timetable.setSizePolicy(sizePolicy1)
        self.but_timetable.setFont(font)
        self.but_orders = QPushButton(self.centralwidget)
        self.but_orders.setObjectName(u"but_orders")
        self.but_orders.setGeometry(QRect(400, 190, 93, 28))
        sizePolicy1.setHeightForWidth(self.but_orders.sizePolicy().hasHeightForWidth())
        self.but_orders.setSizePolicy(sizePolicy1)
        self.but_orders.setFont(font)
        self.but_logout = QPushButton(self.centralwidget)
        self.but_logout.setObjectName(u"but_logout")
        self.but_logout.setGeometry(QRect(342, 260, 151, 28))
        sizePolicy1.setHeightForWidth(self.but_logout.sizePolicy().hasHeightForWidth())
        self.but_logout.setSizePolicy(sizePolicy1)
        self.but_logout.setFont(font)
        Profile.setCentralWidget(self.centralwidget)

        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Profile", None))
        self.label_photo.setText(QCoreApplication.translate("Profile", u"\u0424\u041e\u0422\u041e", None))
        self.label_user.setText(QCoreApplication.translate("Profile", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c:******", None))
        self.label_mail.setText(QCoreApplication.translate("Profile", u"\u041f\u043e\u0447\u0442\u0430:******", None))
        self.but_edit.setText(QCoreApplication.translate("Profile", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.but_timetable.setText(QCoreApplication.translate("Profile", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0438 \u0446\u0435\u043d\u044b", None))
        self.but_orders.setText(QCoreApplication.translate("Profile", u"\u041c\u043e\u0438 \u0431\u0438\u043b\u0435\u0442\u044b", None))
        self.but_logout.setText(QCoreApplication.translate("Profile", u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
    # retranslateUi

