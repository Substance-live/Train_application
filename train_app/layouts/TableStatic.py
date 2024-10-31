# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableStatic.ui'
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

class Ui_TableStatic(object):
    def setupUi(self, TableStatic):
        if not TableStatic.objectName():
            TableStatic.setObjectName(u"TableStatic")
        TableStatic.resize(715, 442)
        self.table = QTableWidget(TableStatic)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 20, 671, 331))
        self.but_reload = QPushButton(TableStatic)
        self.but_reload.setObjectName(u"but_reload")
        self.but_reload.setGeometry(QRect(240, 370, 261, 51))
        self.but_return = QPushButton(TableStatic)
        self.but_return.setObjectName(u"but_return")
        self.but_return.setGeometry(QRect(580, 370, 111, 51))

        self.retranslateUi(TableStatic)

        QMetaObject.connectSlotsByName(TableStatic)
    # setupUi

    def retranslateUi(self, TableStatic):
        TableStatic.setWindowTitle(QCoreApplication.translate("TableStatic", u"Form", None))
        self.but_reload.setText(QCoreApplication.translate("TableStatic", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.but_return.setText(QCoreApplication.translate("TableStatic", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

