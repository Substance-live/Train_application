# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Passenger.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Passenger(object):
    def setupUi(self, Passenger):
        if not Passenger.objectName():
            Passenger.setObjectName(u"Passenger")
        Passenger.resize(690, 281)
        Passenger.setMinimumSize(QSize(0, 0))
        Passenger.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(Passenger)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 663, 241))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_num_document = QLineEdit(self.layoutWidget)
        self.line_num_document.setObjectName(u"line_num_document")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_num_document.sizePolicy().hasHeightForWidth())
        self.line_num_document.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        self.line_num_document.setFont(font)

        self.gridLayout.addWidget(self.line_num_document, 6, 1, 1, 1)

        self.line_surname = QLineEdit(self.layoutWidget)
        self.line_surname.setObjectName(u"line_surname")
        self.line_surname.setFont(font)

        self.gridLayout.addWidget(self.line_surname, 3, 0, 1, 2)

        self.check_patronymic = QCheckBox(self.layoutWidget)
        self.check_patronymic.setObjectName(u"check_patronymic")
        self.check_patronymic.setFont(font)

        self.gridLayout.addWidget(self.check_patronymic, 4, 3, 1, 1)

        self.label_birthday = QLabel(self.layoutWidget)
        self.label_birthday.setObjectName(u"label_birthday")
        self.label_birthday.setFont(font)

        self.gridLayout.addWidget(self.label_birthday, 2, 6, 1, 1)

        self.label_name = QLabel(self.layoutWidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font)

        self.gridLayout.addWidget(self.label_name, 2, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_passnger = QLabel(self.layoutWidget)
        self.label_passnger.setObjectName(u"label_passnger")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_passnger.sizePolicy().hasHeightForWidth())
        self.label_passnger.setSizePolicy(sizePolicy1)
        self.label_passnger.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_passnger.setFont(font1)

        self.verticalLayout.addWidget(self.label_passnger)

        self.combo_passenger = QComboBox(self.layoutWidget)
        self.combo_passenger.setObjectName(u"combo_passenger")
        sizePolicy1.setHeightForWidth(self.combo_passenger.sizePolicy().hasHeightForWidth())
        self.combo_passenger.setSizePolicy(sizePolicy1)
        self.combo_passenger.setMinimumSize(QSize(0, 0))
        self.combo_passenger.setFont(font)

        self.verticalLayout.addWidget(self.combo_passenger)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)

        self.but_back = QPushButton(self.layoutWidget)
        self.but_back.setObjectName(u"but_back")
        self.but_back.setFont(font)

        self.gridLayout.addWidget(self.but_back, 7, 4, 1, 3)

        self.label_patronymic = QLabel(self.layoutWidget)
        self.label_patronymic.setObjectName(u"label_patronymic")
        self.label_patronymic.setFont(font)

        self.gridLayout.addWidget(self.label_patronymic, 2, 3, 1, 1)

        self.radio_male = QRadioButton(self.layoutWidget)
        self.radio_male.setObjectName(u"radio_male")
        self.radio_male.setFont(font)

        self.gridLayout.addWidget(self.radio_male, 3, 4, 1, 1)

        self.combo_document = QComboBox(self.layoutWidget)
        self.combo_document.setObjectName(u"combo_document")
        self.combo_document.setFont(font)

        self.gridLayout.addWidget(self.combo_document, 6, 0, 1, 1)

        self.label_num_documnt = QLabel(self.layoutWidget)
        self.label_num_documnt.setObjectName(u"label_num_documnt")
        self.label_num_documnt.setFont(font)

        self.gridLayout.addWidget(self.label_num_documnt, 5, 1, 1, 1)

        self.line_name = QLineEdit(self.layoutWidget)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setFont(font)

        self.gridLayout.addWidget(self.line_name, 3, 2, 1, 1)

        self.date_birthday = QDateEdit(self.layoutWidget)
        self.date_birthday.setObjectName(u"date_birthday")
        self.date_birthday.setFont(font)
        self.date_birthday.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_birthday, 3, 6, 1, 1)

        self.but_buy = QPushButton(self.layoutWidget)
        self.but_buy.setObjectName(u"but_buy")
        sizePolicy.setHeightForWidth(self.but_buy.sizePolicy().hasHeightForWidth())
        self.but_buy.setSizePolicy(sizePolicy)
        self.but_buy.setMinimumSize(QSize(0, 0))
        self.but_buy.setFont(font)

        self.gridLayout.addWidget(self.but_buy, 7, 0, 1, 2)

        self.but_question = QToolButton(self.layoutWidget)
        self.but_question.setObjectName(u"but_question")
        font2 = QFont()
        font2.setPointSize(12)
        self.but_question.setFont(font2)
        self.but_question.setStyleSheet(u"")

        self.gridLayout.addWidget(self.but_question, 7, 3, 1, 1)

        self.line_patronymic = QLineEdit(self.layoutWidget)
        self.line_patronymic.setObjectName(u"line_patronymic")
        self.line_patronymic.setFont(font)

        self.gridLayout.addWidget(self.line_patronymic, 3, 3, 1, 1)

        self.label_surname = QLabel(self.layoutWidget)
        self.label_surname.setObjectName(u"label_surname")
        self.label_surname.setFont(font)

        self.gridLayout.addWidget(self.label_surname, 2, 0, 1, 2)

        self.label_gender = QLabel(self.layoutWidget)
        self.label_gender.setObjectName(u"label_gender")
        self.label_gender.setFont(font)

        self.gridLayout.addWidget(self.label_gender, 2, 4, 1, 2)

        self.label_document = QLabel(self.layoutWidget)
        self.label_document.setObjectName(u"label_document")
        self.label_document.setFont(font)

        self.gridLayout.addWidget(self.label_document, 5, 0, 1, 1)

        self.radio_female = QRadioButton(self.layoutWidget)
        self.radio_female.setObjectName(u"radio_female")
        self.radio_female.setFont(font)

        self.gridLayout.addWidget(self.radio_female, 3, 5, 1, 1)

        self.label_price = QLabel(self.layoutWidget)
        self.label_price.setObjectName(u"label_price")
        sizePolicy1.setHeightForWidth(self.label_price.sizePolicy().hasHeightForWidth())
        self.label_price.setSizePolicy(sizePolicy1)
        self.label_price.setMinimumSize(QSize(100, 0))
        self.label_price.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(14)
        self.label_price.setFont(font3)
        self.label_price.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_price, 7, 2, 1, 1)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 2)

        Passenger.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Passenger)
        self.statusbar.setObjectName(u"statusbar")
        Passenger.setStatusBar(self.statusbar)

        self.retranslateUi(Passenger)

        QMetaObject.connectSlotsByName(Passenger)
    # setupUi

    def retranslateUi(self, Passenger):
        Passenger.setWindowTitle(QCoreApplication.translate("Passenger", u"Passenger", None))
        self.line_surname.setPlaceholderText("")
        self.check_patronymic.setText(QCoreApplication.translate("Passenger", u"\u041d\u0435\u0442 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u0430", None))
        self.label_birthday.setText(QCoreApplication.translate("Passenger", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_name.setText(QCoreApplication.translate("Passenger", u"\u0418\u043c\u044f", None))
        self.label_passnger.setText(QCoreApplication.translate("Passenger", u"\u041f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u044b", None))
        self.but_back.setText(QCoreApplication.translate("Passenger", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_patronymic.setText(QCoreApplication.translate("Passenger", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.radio_male.setText(QCoreApplication.translate("Passenger", u"\u041c", None))
        self.label_num_documnt.setText(QCoreApplication.translate("Passenger", u"\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.line_name.setPlaceholderText("")
        self.but_buy.setText(QCoreApplication.translate("Passenger", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.but_question.setText(QCoreApplication.translate("Passenger", u"i", None))
        self.line_patronymic.setPlaceholderText("")
        self.label_surname.setText(QCoreApplication.translate("Passenger", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_gender.setText(QCoreApplication.translate("Passenger", u"\u041f\u043e\u043b", None))
        self.label_document.setText(QCoreApplication.translate("Passenger", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.radio_female.setText(QCoreApplication.translate("Passenger", u"\u0416", None))
        self.label_price.setText(QCoreApplication.translate("Passenger", u"100$", None))
        self.checkBox.setText(QCoreApplication.translate("Passenger", u"\u042d\u0442\u043e\u0442 \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440 - \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c", None))
    # retranslateUi

