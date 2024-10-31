# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PassangerTable.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_UserPassanger(object):
    def setupUi(self, UserPassanger):
        if not UserPassanger.objectName():
            UserPassanger.setObjectName(u"UserPassanger")
        UserPassanger.resize(715, 485)
        self.table = QTableWidget(UserPassanger)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 20, 671, 331))
        self.but_reload = QPushButton(UserPassanger)
        self.but_reload.setObjectName(u"but_reload")
        self.but_reload.setGeometry(QRect(300, 380, 261, 51))
        self.but_return = QPushButton(UserPassanger)
        self.but_return.setObjectName(u"but_return")
        self.but_return.setGeometry(QRect(580, 380, 111, 51))
        self.comboBox_kurs = QComboBox(UserPassanger)
        self.comboBox_kurs.setObjectName(u"comboBox_kurs")
        self.comboBox_kurs.setGeometry(QRect(32, 360, 101, 22))
        self.comboBox_category = QComboBox(UserPassanger)
        self.comboBox_category.setObjectName(u"comboBox_category")
        self.comboBox_category.setGeometry(QRect(32, 390, 101, 22))
        self.comboBox_direction = QComboBox(UserPassanger)
        self.comboBox_direction.setObjectName(u"comboBox_direction")
        self.comboBox_direction.setGeometry(QRect(32, 420, 101, 22))
        self.label_kurs = QLabel(UserPassanger)
        self.label_kurs.setObjectName(u"label_kurs")
        self.label_kurs.setGeometry(QRect(160, 360, 55, 16))
        self.label_category = QLabel(UserPassanger)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(160, 390, 61, 20))
        self.label_dircetion = QLabel(UserPassanger)
        self.label_dircetion.setObjectName(u"label_dircetion")
        self.label_dircetion.setGeometry(QRect(160, 420, 81, 20))
        self.checkBox = QCheckBox(UserPassanger)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(80, 450, 191, 20))
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.retranslateUi(UserPassanger)

        QMetaObject.connectSlotsByName(UserPassanger)
    # setupUi

    def retranslateUi(self, UserPassanger):
        UserPassanger.setWindowTitle(QCoreApplication.translate("UserPassanger", u"Form", None))
        self.but_reload.setText(QCoreApplication.translate("UserPassanger", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.but_return.setText(QCoreApplication.translate("UserPassanger", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_kurs.setText(QCoreApplication.translate("UserPassanger", u"\u041a\u0443\u0440\u0441", None))
        self.label_category.setText(QCoreApplication.translate("UserPassanger", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_dircetion.setText(QCoreApplication.translate("UserPassanger", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.checkBox.setText(QCoreApplication.translate("UserPassanger", u"               \u0411\u0430\u0433\u0430\u0436", None))
    # retranslateUi

