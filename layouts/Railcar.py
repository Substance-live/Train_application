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
    QHeaderView, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QSplitter,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Railcar(object):
    def setupUi(self, Railcar):
        if not Railcar.objectName():
            Railcar.setObjectName(u"Railcar")
        Railcar.resize(901, 400)
        self.centralwidget = QWidget(Railcar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(14)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setHorizontalSpacing(105)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_passenger = QLabel(self.layoutWidget)
        self.label_passenger.setObjectName(u"label_passenger")
        self.label_passenger.setMinimumSize(QSize(237, 0))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_passenger.setFont(font)

        self.gridLayout.addWidget(self.label_passenger, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_baby = QLabel(self.layoutWidget)
        self.label_baby.setObjectName(u"label_baby")
        self.label_baby.setMaximumSize(QSize(125, 16777215))
        font1 = QFont()
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_baby.setFont(font1)
        self.label_baby.setTextFormat(Qt.TextFormat.RichText)
        self.label_baby.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_baby.setWordWrap(True)
        self.label_baby.setMargin(0)
        self.label_baby.setIndent(-1)

        self.horizontalLayout.addWidget(self.label_baby)

        self.spin_box_baby = QSpinBox(self.layoutWidget)
        self.spin_box_baby.setObjectName(u"spin_box_baby")
        self.spin_box_baby.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.spin_box_baby)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_children = QLabel(self.layoutWidget)
        self.label_children.setObjectName(u"label_children")
        self.label_children.setMaximumSize(QSize(125, 16777215))
        self.label_children.setTextFormat(Qt.TextFormat.RichText)
        self.label_children.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_children.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_children)

        self.spin_box_children = QSpinBox(self.layoutWidget)
        self.spin_box_children.setObjectName(u"spin_box_children")
        self.spin_box_children.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.spin_box_children)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_adult = QLabel(self.layoutWidget)
        self.label_adult.setObjectName(u"label_adult")
        self.label_adult.setMaximumSize(QSize(125, 16777215))
        self.label_adult.setTextFormat(Qt.TextFormat.RichText)
        self.label_adult.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_adult.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_adult)

        self.spin_box_adult = QSpinBox(self.layoutWidget)
        self.spin_box_adult.setObjectName(u"spin_box_adult")
        self.spin_box_adult.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.spin_box_adult)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_railcar = QLabel(self.layoutWidget1)
        self.label_railcar.setObjectName(u"label_railcar")
        self.label_railcar.setFont(font)

        self.verticalLayout_3.addWidget(self.label_railcar)

        self.table_railcar = QTableWidget(self.layoutWidget1)
        if (self.table_railcar.columnCount() < 5):
            self.table_railcar.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_railcar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_railcar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_railcar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_railcar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_railcar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.table_railcar.rowCount() < 3):
            self.table_railcar.setRowCount(3)
        self.table_railcar.setObjectName(u"table_railcar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.table_railcar.sizePolicy().hasHeightForWidth())
        self.table_railcar.setSizePolicy(sizePolicy)
        self.table_railcar.setMinimumSize(QSize(583, 250))
        font2 = QFont()
        font2.setPointSize(8)
        self.table_railcar.setFont(font2)
        self.table_railcar.setAlternatingRowColors(False)
        self.table_railcar.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_railcar.setSortingEnabled(True)
        self.table_railcar.horizontalHeader().setVisible(True)
        self.table_railcar.horizontalHeader().setMinimumSectionSize(32)
        self.table_railcar.horizontalHeader().setDefaultSectionSize(122)
        self.table_railcar.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_railcar.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.table_railcar)

        self.splitter.addWidget(self.layoutWidget1)
        self.splitter_2.addWidget(self.splitter)
        self.layoutWidget2 = QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.but_to_passenger = QPushButton(self.layoutWidget2)
        self.but_to_passenger.setObjectName(u"but_to_passenger")
        self.but_to_passenger.setMinimumSize(QSize(0, 34))

        self.horizontalLayout_5.addWidget(self.but_to_passenger)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_price = QLabel(self.layoutWidget2)
        self.label_price.setObjectName(u"label_price")
        font3 = QFont()
        font3.setPointSize(15)
        self.label_price.setFont(font3)
        self.label_price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_price)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.but_back = QPushButton(self.layoutWidget2)
        self.but_back.setObjectName(u"but_back")

        self.horizontalLayout_6.addWidget(self.but_back)

        self.splitter_2.addWidget(self.layoutWidget2)

        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)

        Railcar.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Railcar)
        self.statusbar.setObjectName(u"statusbar")
        Railcar.setStatusBar(self.statusbar)

        self.retranslateUi(Railcar)

        QMetaObject.connectSlotsByName(Railcar)
    # setupUi

    def retranslateUi(self, Railcar):
        Railcar.setWindowTitle(QCoreApplication.translate("Railcar", u"Railcar", None))
        self.label_passenger.setText(QCoreApplication.translate("Railcar", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432", None))
        self.label_baby.setText(QCoreApplication.translate("Railcar", u"\u041c\u0430\u043b\u044b\u0448\u0438 \u0434\u043e 5 \u043b\u0435\u0442 \u0431\u0435\u0437 \u043c\u0435\u0441\u0442\u0430, \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e", None))
        self.label_children.setText(QCoreApplication.translate("Railcar", u"\u0414\u0435\u0442\u0438 \u0434\u043e 10 \u043b\u0435\u0442 \u0441 \u043c\u0435\u0441\u0442\u043e\u043c, \u0434\u0435\u0448\u0435\u0432\u043b\u0435", None))
        self.label_adult.setText(QCoreApplication.translate("Railcar", u"\u0412\u0437\u0440\u043e\u0441\u043b\u044b\u0435 \u0438 \u0434\u0435\u0442\u0438\n"
"\u0441\u0442\u0430\u0440\u0448\u0435 10 \u043b\u0435\u0442", None))
        self.label_railcar.setText(QCoreApplication.translate("Railcar", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0430\u0433\u043e\u043d \u0438 \u043c\u0435\u0441\u0442\u0430", None))
        ___qtablewidgetitem = self.table_railcar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Railcar", u"\u041d\u043e\u043c\u0435\u0440 \u0432\u0430\u0433\u043e\u043d\u0430", None));
        ___qtablewidgetitem1 = self.table_railcar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Railcar", u"\u041a\u043e\u043b-\u0432\u043e \u043c\u0435\u0441\u0442", None));
        ___qtablewidgetitem2 = self.table_railcar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Railcar", u"\u041a\u043b\u0430\u0441\u0441 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem3 = self.table_railcar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Railcar", u"\u0422\u0438\u043f \u0432\u0430\u0433\u043e\u043d\u0430", None));
        ___qtablewidgetitem4 = self.table_railcar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Railcar", u"\u0426\u0435\u043d\u0430", None));
        self.but_to_passenger.setText(QCoreApplication.translate("Railcar", u"\u041a \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u0430\u043c", None))
        self.label_price.setText(QCoreApplication.translate("Railcar", u"100$", None))
        self.but_back.setText(QCoreApplication.translate("Railcar", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

