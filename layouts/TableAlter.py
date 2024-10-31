# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableAlter.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_TableAlter(object):
    def setupUi(self, TableAlter):
        if not TableAlter.objectName():
            TableAlter.setObjectName(u"TableAlter")
        TableAlter.resize(715, 442)
        self.table = QTableWidget(TableAlter)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 20, 671, 331))
        self.but_return = QPushButton(TableAlter)
        self.but_return.setObjectName(u"but_return")
        self.but_return.setGeometry(QRect(580, 370, 111, 51))
        self.but_task_1 = QPushButton(TableAlter)
        self.but_task_1.setObjectName(u"but_task_1")
        self.but_task_1.setGeometry(QRect(250, 370, 221, 51))
        self.but_reload = QPushButton(TableAlter)
        self.but_reload.setObjectName(u"but_reload")
        self.but_reload.setGeometry(QRect(20, 370, 101, 51))

        self.retranslateUi(TableAlter)

        QMetaObject.connectSlotsByName(TableAlter)
    # setupUi

    def retranslateUi(self, TableAlter):
        TableAlter.setWindowTitle(QCoreApplication.translate("TableAlter", u"Form", None))
        self.but_return.setText(QCoreApplication.translate("TableAlter", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.but_task_1.setText(QCoreApplication.translate("TableAlter", u"\u0417\u0430\u0434\u0430\u0447\u0430 1", None))
        self.but_reload.setText(QCoreApplication.translate("TableAlter", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

