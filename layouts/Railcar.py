# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Railcar.ui'
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
    QHeaderView, QLabel, QLayout, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QSplitter, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Railcar(object):
    def setupUi(self, Railcar):
        if not Railcar.objectName():
            Railcar.setObjectName(u"Railcar")
        Railcar.resize(619, 562)
        self.centralwidget = QWidget(Railcar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 21, 581, 516))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setHorizontalSpacing(105)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(148, 0))
        self.label_5.setMaximumSize(QSize(16777215, 300))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(125, 16777215))
        font1 = QFont()
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.TextFormat.RichText)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(0)
        self.label_4.setIndent(-1)

        self.horizontalLayout.addWidget(self.label_4)

        self.spinBox_3 = QSpinBox(self.layoutWidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.spinBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(125, 16777215))
        self.label_3.setTextFormat(Qt.TextFormat.RichText)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.spinBox_2 = QSpinBox(self.layoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.spinBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(125, 16777215))
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.listWidget = QListWidget(self.layoutWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidget.setSortingEnabled(True)

        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_3.addWidget(self.label_6)

        self.table_timetable = QTableWidget(self.layoutWidget1)
        if (self.table_timetable.columnCount() < 5):
            self.table_timetable.setColumnCount(5)
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
        if (self.table_timetable.rowCount() < 3):
            self.table_timetable.setRowCount(3)
        self.table_timetable.setObjectName(u"table_timetable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.table_timetable.sizePolicy().hasHeightForWidth())
        self.table_timetable.setSizePolicy(sizePolicy)
        self.table_timetable.setMinimumSize(QSize(0, 240))
        font2 = QFont()
        font2.setPointSize(8)
        self.table_timetable.setFont(font2)
        self.table_timetable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_timetable.setSortingEnabled(True)
        self.table_timetable.horizontalHeader().setVisible(True)
        self.table_timetable.horizontalHeader().setMinimumSectionSize(32)
        self.table_timetable.horizontalHeader().setDefaultSectionSize(115)
        self.table_timetable.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_timetable.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.table_timetable)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.layoutWidget2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 34))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(15)
        self.label_7.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.toolButton = QToolButton(self.layoutWidget2)
        self.toolButton.setObjectName(u"toolButton")
        font4 = QFont()
        font4.setPointSize(12)
        self.toolButton.setFont(font4)
        self.toolButton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.toolButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.pushButton_2 = QPushButton(self.layoutWidget2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.splitter.addWidget(self.layoutWidget2)
        Railcar.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Railcar)
        self.statusbar.setObjectName(u"statusbar")
        Railcar.setStatusBar(self.statusbar)

        self.retranslateUi(Railcar)

        QMetaObject.connectSlotsByName(Railcar)
    # setupUi

    def retranslateUi(self, Railcar):
        Railcar.setWindowTitle(QCoreApplication.translate("Railcar", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Railcar", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432", None))
        self.label_5.setText(QCoreApplication.translate("Railcar", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.label_4.setText(QCoreApplication.translate("Railcar", u"\u041c\u0430\u043b\u044b\u0448\u0438 \u0434\u043e 5 \u043b\u0435\u0442 \u0431\u0435\u0437 \u043c\u0435\u0441\u0442\u0430, \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e", None))
        self.label_3.setText(QCoreApplication.translate("Railcar", u"\u0414\u0435\u0442\u0438 \u0434\u043e 10 \u043b\u0435\u0442 \u0441 \u043c\u0435\u0441\u0442\u043e\u043c, \u0434\u0435\u0448\u0435\u0432\u043b\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Railcar", u"\u0412\u0437\u0440\u043e\u0441\u043b\u044b\u0435 \u0438 \u0434\u0435\u0442\u0438\n"
"\u0441\u0442\u0430\u0440\u0448\u0435 10 \u043b\u0435\u0442", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Railcar", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Railcar", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Railcar", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Railcar", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_6.setText(QCoreApplication.translate("Railcar", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0430\u0433\u043e\u043d \u0438 \u043c\u0435\u0441\u0442\u0430", None))
        ___qtablewidgetitem = self.table_timetable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Railcar", u"\u041d\u043e\u043c\u0435\u0440 \u0432\u0430\u0433\u043e\u043d\u0430", None));
        ___qtablewidgetitem1 = self.table_timetable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Railcar", u"\u041a\u043e\u043b-\u0432\u043e \u043c\u0435\u0441\u0442", None));
        ___qtablewidgetitem2 = self.table_timetable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Railcar", u"\u041a\u043b\u0430\u0441\u0441 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem3 = self.table_timetable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Railcar", u"\u0422\u0438\u043f \u0432\u0430\u0433\u043e\u043d\u0430", None));
        ___qtablewidgetitem4 = self.table_timetable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Railcar", u"\u0426\u0435\u043d\u0430", None));
        self.pushButton.setText(QCoreApplication.translate("Railcar", u"\u041a \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u0430\u043c", None))
        self.label_7.setText(QCoreApplication.translate("Railcar", u"100$", None))
        self.toolButton.setText(QCoreApplication.translate("Railcar", u"i", None))
        self.pushButton_2.setText(QCoreApplication.translate("Railcar", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

