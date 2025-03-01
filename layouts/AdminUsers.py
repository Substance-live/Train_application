# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminUsers.ui'
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

class Ui_AdminUsers(object):
    def setupUi(self, AdminUsers):
        if not AdminUsers.objectName():
            AdminUsers.setObjectName(u"AdminUsers")
        AdminUsers.resize(825, 379)
        self.centralwidget = QWidget(AdminUsers)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.but_add = QPushButton(self.centralwidget)
        self.but_add.setObjectName(u"but_add")
        font = QFont()
        font.setPointSize(9)
        self.but_add.setFont(font)

        self.gridLayout.addWidget(self.but_add, 1, 0, 1, 1)

        self.but_del = QPushButton(self.centralwidget)
        self.but_del.setObjectName(u"but_del")
        self.but_del.setFont(font)

        self.gridLayout.addWidget(self.but_del, 1, 1, 1, 1)

        self.but_return = QPushButton(self.centralwidget)
        self.but_return.setObjectName(u"but_return")
        self.but_return.setFont(font)

        self.gridLayout.addWidget(self.but_return, 1, 2, 1, 1)

        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 8):
            self.table.setColumnCount(8)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.table.setObjectName(u"table")
        self.table.setMinimumSize(QSize(502, 0))
        self.table.setMaximumSize(QSize(1200, 16777215))
        self.table.setFont(font)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setVisible(True)
        self.table.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.table, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        AdminUsers.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(AdminUsers)
        self.statusbar.setObjectName(u"statusbar")
        AdminUsers.setStatusBar(self.statusbar)

        self.retranslateUi(AdminUsers)

        QMetaObject.connectSlotsByName(AdminUsers)
    # setupUi

    def retranslateUi(self, AdminUsers):
        AdminUsers.setWindowTitle(QCoreApplication.translate("AdminUsers", u"AdminUsers", None))
        self.but_add.setText(QCoreApplication.translate("AdminUsers", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.but_del.setText(QCoreApplication.translate("AdminUsers", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.but_return.setText(QCoreApplication.translate("AdminUsers", u"\u041d\u0430\u0437\u0430\u0434", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminUsers", u"ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminUsers", u"\u041f\u043e\u0447\u0442\u0430", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminUsers", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminUsers", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdminUsers", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdminUsers", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AdminUsers", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AdminUsers", u"\u0414\u0435\u043d\u044c \u0420\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
    # retranslateUi

