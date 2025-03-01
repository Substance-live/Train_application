# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyTickets.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MyTickets(object):
    def setupUi(self, MyTickets):
        if not MyTickets.objectName():
            MyTickets.setObjectName(u"MyTickets")
        MyTickets.resize(523, 260)
        self.centralwidget = QWidget(MyTickets)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 5):
            self.table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table.setObjectName(u"table")
        self.table.setMinimumSize(QSize(0, 0))
        self.table.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.table.setFont(font)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setVisible(True)
        self.table.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.table, 0, 1, 1, 5)

        self.but_print = QPushButton(self.centralwidget)
        self.but_print.setObjectName(u"but_print")

        self.gridLayout.addWidget(self.but_print, 1, 1, 1, 1)

        self.but_refund = QPushButton(self.centralwidget)
        self.but_refund.setObjectName(u"but_refund")
        self.but_refund.setFont(font)

        self.gridLayout.addWidget(self.but_refund, 1, 2, 1, 1)

        self.but_del = QPushButton(self.centralwidget)
        self.but_del.setObjectName(u"but_del")
        self.but_del.setFont(font)

        self.gridLayout.addWidget(self.but_del, 1, 3, 1, 1)

        self.but_return = QPushButton(self.centralwidget)
        self.but_return.setObjectName(u"but_return")
        self.but_return.setFont(font)

        self.gridLayout.addWidget(self.but_return, 1, 4, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MyTickets.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MyTickets)
        self.statusbar.setObjectName(u"statusbar")
        MyTickets.setStatusBar(self.statusbar)

        self.retranslateUi(MyTickets)

        QMetaObject.connectSlotsByName(MyTickets)
    # setupUi

    def retranslateUi(self, MyTickets):
        MyTickets.setWindowTitle(QCoreApplication.translate("MyTickets", u"MyTickets", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MyTickets", u"ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MyTickets", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MyTickets", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MyTickets", u"\u0426\u0435\u043d\u0430", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MyTickets", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430", None));
        self.but_print.setText(QCoreApplication.translate("MyTickets", u"\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c", None))
        self.but_refund.setText(QCoreApplication.translate("MyTickets", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c \u0431\u0438\u043b\u0435\u0442", None))
        self.but_del.setText(QCoreApplication.translate("MyTickets", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.but_return.setText(QCoreApplication.translate("MyTickets", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

