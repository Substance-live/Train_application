# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ticket.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGridLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Ticket(object):
    def setupUi(self, Ticket):
        if not Ticket.objectName():
            Ticket.setObjectName(u"Ticket")
        Ticket.resize(653, 437)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(Ticket.sizePolicy().hasHeightForWidth())
        Ticket.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        Ticket.setFont(font)
        self.centralwidget = QWidget(Ticket)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 624, 401))
        font1 = QFont()
        font1.setPointSize(9)
        self.layoutWidget.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.combo_departure = QComboBox(self.layoutWidget)
        self.combo_departure.setObjectName(u"combo_departure")
        self.combo_departure.setFont(font1)
        self.combo_departure.setEditable(True)

        self.gridLayout.addWidget(self.combo_departure, 1, 0, 1, 1)

        self.but_switch = QToolButton(self.layoutWidget)
        self.but_switch.setObjectName(u"but_switch")
        self.but_switch.setFont(font1)

        self.gridLayout.addWidget(self.but_switch, 1, 1, 1, 1)

        self.combo_destination = QComboBox(self.layoutWidget)
        self.combo_destination.setObjectName(u"combo_destination")
        self.combo_destination.setFont(font1)
        self.combo_destination.setEditable(True)

        self.gridLayout.addWidget(self.combo_destination, 1, 2, 1, 1)

        self.date_edit = QDateEdit(self.layoutWidget)
        self.date_edit.setObjectName(u"date_edit")
        self.date_edit.setFont(font1)
        self.date_edit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_edit, 1, 3, 1, 1)

        self.but_search = QPushButton(self.layoutWidget)
        self.but_search.setObjectName(u"but_search")
        self.but_search.setFont(font1)

        self.gridLayout.addWidget(self.but_search, 1, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_timetable = QTableWidget(self.layoutWidget)
        if (self.table_timetable.columnCount() < 6):
            self.table_timetable.setColumnCount(6)
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
        if (self.table_timetable.rowCount() < 2):
            self.table_timetable.setRowCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_timetable.setVerticalHeaderItem(0, __qtablewidgetitem6)
        self.table_timetable.setObjectName(u"table_timetable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(15)
        sizePolicy1.setVerticalStretch(15)
        sizePolicy1.setHeightForWidth(self.table_timetable.sizePolicy().hasHeightForWidth())
        self.table_timetable.setSizePolicy(sizePolicy1)
        self.table_timetable.setMinimumSize(QSize(620, 0))
        self.table_timetable.setMaximumSize(QSize(620, 16777215))
        self.table_timetable.setFont(font1)
        self.table_timetable.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_timetable.setSortingEnabled(True)
        self.table_timetable.horizontalHeader().setVisible(True)
        self.table_timetable.horizontalHeader().setCascadingSectionResizes(False)
        self.table_timetable.horizontalHeader().setMinimumSectionSize(32)
        self.table_timetable.horizontalHeader().setDefaultSectionSize(103)
        self.table_timetable.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_timetable.horizontalHeader().setStretchLastSection(False)
        self.table_timetable.verticalHeader().setVisible(False)
        self.table_timetable.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.table_timetable, 0, 0, 1, 2)

        self.but_back = QPushButton(self.layoutWidget)
        self.but_back.setObjectName(u"but_back")
        self.but_back.setFont(font1)

        self.gridLayout_2.addWidget(self.but_back, 2, 1, 1, 1)

        self.but_confirm = QPushButton(self.layoutWidget)
        self.but_confirm.setObjectName(u"but_confirm")
        self.but_confirm.setFont(font1)

        self.gridLayout_2.addWidget(self.but_confirm, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        Ticket.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Ticket)
        self.statusbar.setObjectName(u"statusbar")
        Ticket.setStatusBar(self.statusbar)

        self.retranslateUi(Ticket)

        QMetaObject.connectSlotsByName(Ticket)
    # setupUi

    def retranslateUi(self, Ticket):
        Ticket.setWindowTitle(QCoreApplication.translate("Ticket", u"Ticket", None))
        self.label.setText(QCoreApplication.translate("Ticket", u"\u041e\u0442\u043a\u0443\u0434\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Ticket", u"\u041a\u0443\u0434\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Ticket", u"\u0414\u0430\u0442\u0430", None))
        self.combo_departure.setCurrentText("")
        self.combo_departure.setProperty(u"placeholderText", QCoreApplication.translate("Ticket", u"\u041e\u0442\u043a\u0443\u0434\u0430", None))
        self.but_switch.setText(QCoreApplication.translate("Ticket", u"><", None))
        self.combo_destination.setCurrentText("")
        self.combo_destination.setProperty(u"placeholderText", QCoreApplication.translate("Ticket", u"\u041a\u0443\u0434\u0430", None))
        self.but_search.setText(QCoreApplication.translate("Ticket", u"\u041d\u0430\u0439\u0442\u0438 \u0431\u0438\u043b\u0435\u0442", None))
        ___qtablewidgetitem = self.table_timetable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Ticket", u"\u041e\u0442\u043a\u0443\u0434\u0430", None));
        ___qtablewidgetitem1 = self.table_timetable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Ticket", u"\u041a\u0443\u0434\u0430", None));
        ___qtablewidgetitem2 = self.table_timetable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Ticket", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None));
        ___qtablewidgetitem3 = self.table_timetable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Ticket", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438", None));
        ___qtablewidgetitem4 = self.table_timetable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Ticket", u"\u041a\u043e\u043b-\u0432\u043e \u043c\u0435\u0441\u0442", None));
        ___qtablewidgetitem5 = self.table_timetable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Ticket", u"\u0426\u0435\u043d\u0430", None));
        ___qtablewidgetitem6 = self.table_timetable.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Ticket", u"2", None));
        self.but_back.setText(QCoreApplication.translate("Ticket", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.but_confirm.setText(QCoreApplication.translate("Ticket", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043c\u0435\u0441\u0442\u0430", None))
    # retranslateUi
