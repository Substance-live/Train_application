# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminTickets.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AdminTickets(object):
    def setupUi(self, AdminTickets):
        if not AdminTickets.objectName():
            AdminTickets.setObjectName(u"AdminTickets")
        AdminTickets.resize(929, 495)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(AdminTickets.sizePolicy().hasHeightForWidth())
        AdminTickets.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        AdminTickets.setFont(font)
        self.centralwidget = QWidget(AdminTickets)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_timetable = QTableWidget(self.centralwidget)
        if (self.table_timetable.columnCount() < 7):
            self.table_timetable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_timetable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_timetable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_timetable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_timetable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_timetable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_timetable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_timetable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.table_timetable.rowCount() < 1):
            self.table_timetable.setRowCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_timetable.setVerticalHeaderItem(0, __qtablewidgetitem7)
        self.table_timetable.setObjectName(u"table_timetable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(15)
        sizePolicy1.setVerticalStretch(15)
        sizePolicy1.setHeightForWidth(self.table_timetable.sizePolicy().hasHeightForWidth())
        self.table_timetable.setSizePolicy(sizePolicy1)
        self.table_timetable.setMinimumSize(QSize(699, 0))
        self.table_timetable.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        self.table_timetable.setFont(font1)
        self.table_timetable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_timetable.setSortingEnabled(True)
        self.table_timetable.setRowCount(1)
        self.table_timetable.horizontalHeader().setVisible(True)
        self.table_timetable.horizontalHeader().setCascadingSectionResizes(False)
        self.table_timetable.horizontalHeader().setMinimumSectionSize(32)
        self.table_timetable.horizontalHeader().setDefaultSectionSize(129)
        self.table_timetable.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_timetable.horizontalHeader().setStretchLastSection(False)
        self.table_timetable.verticalHeader().setVisible(False)
        self.table_timetable.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.table_timetable, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.but_add = QPushButton(self.centralwidget)
        self.but_add.setObjectName(u"but_add")
        self.but_add.setFont(font1)

        self.horizontalLayout.addWidget(self.but_add)

        self.but_del = QPushButton(self.centralwidget)
        self.but_del.setObjectName(u"but_del")
        self.but_del.setFont(font1)

        self.horizontalLayout.addWidget(self.but_del)

        self.but_back = QPushButton(self.centralwidget)
        self.but_back.setObjectName(u"but_back")
        self.but_back.setFont(font1)

        self.horizontalLayout.addWidget(self.but_back)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        AdminTickets.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(AdminTickets)
        self.statusbar.setObjectName(u"statusbar")
        AdminTickets.setStatusBar(self.statusbar)

        self.retranslateUi(AdminTickets)

        QMetaObject.connectSlotsByName(AdminTickets)
    # setupUi

    def retranslateUi(self, AdminTickets):
        AdminTickets.setWindowTitle(QCoreApplication.translate("AdminTickets", u"AdminTickets", None))
        ___qtablewidgetitem = self.table_timetable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminTickets", u"ID", None));
        ___qtablewidgetitem1 = self.table_timetable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminTickets", u"\u041e\u0442\u043a\u0443\u0434\u0430", None));
        ___qtablewidgetitem2 = self.table_timetable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminTickets", u"\u041a\u0443\u0434\u0430", None));
        ___qtablewidgetitem3 = self.table_timetable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminTickets", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438", None));
        ___qtablewidgetitem4 = self.table_timetable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdminTickets", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None));
        ___qtablewidgetitem5 = self.table_timetable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdminTickets", u"\u041a\u043e\u043b-\u0432\u043e \u043c\u0435\u0441\u0442", None));
        ___qtablewidgetitem6 = self.table_timetable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AdminTickets", u"\u0426\u0435\u043d\u0430", None));
        ___qtablewidgetitem7 = self.table_timetable.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AdminTickets", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        self.but_add.setText(QCoreApplication.translate("AdminTickets", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.but_del.setText(QCoreApplication.translate("AdminTickets", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.but_back.setText(QCoreApplication.translate("AdminTickets", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

