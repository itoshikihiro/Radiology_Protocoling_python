# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nlp_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_nlp_gui(object):
    def setupUi(self, nlp_gui):
        if not nlp_gui.objectName():
            nlp_gui.setObjectName(u"nlp_gui")
        nlp_gui.resize(641, 472)
        self.selection_tab = QTabWidget(nlp_gui)
        self.selection_tab.setObjectName(u"selection_tab")
        self.selection_tab.setGeometry(QRect(0, 0, 641, 471))
        self.cpt_tab = QWidget()
        self.cpt_tab.setObjectName(u"cpt_tab")
        self.cpt_input_text = QPlainTextEdit(self.cpt_tab)
        self.cpt_input_text.setObjectName(u"cpt_input_text")
        self.cpt_input_text.setGeometry(QRect(30, 100, 211, 211))
        self.cpt_input_text.setFocusPolicy(Qt.ClickFocus)
        self.cpt_input_text.setTabChangesFocus(True)
        self.cpt_input_text.setPlainText(u"")
        self.line = QFrame(self.cpt_tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 30, 591, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.cpt_input_label = QLabel(self.cpt_tab)
        self.cpt_input_label.setObjectName(u"cpt_input_label")
        self.cpt_input_label.setGeometry(QRect(100, 10, 61, 21))
        font = QFont()
        font.setPointSize(22)
        self.cpt_input_label.setFont(font)
        self.cpt_input_label.setAlignment(Qt.AlignCenter)
        self.cpt_text_label = QLabel(self.cpt_tab)
        self.cpt_text_label.setObjectName(u"cpt_text_label")
        self.cpt_text_label.setGeometry(QRect(90, 50, 101, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.cpt_text_label.setFont(font1)
        self.cpt_predict_button = QPushButton(self.cpt_tab)
        self.cpt_predict_button.setObjectName(u"cpt_predict_button")
        self.cpt_predict_button.setGeometry(QRect(250, 190, 121, 41))
        self.cpt_predict_button.setFont(font1)
        self.cpt_output_label = QLabel(self.cpt_tab)
        self.cpt_output_label.setObjectName(u"cpt_output_label")
        self.cpt_output_label.setGeometry(QRect(450, 10, 81, 21))
        self.cpt_output_label.setFont(font1)
        self.cpt_output_label.setAlignment(Qt.AlignCenter)
        self.cpt_output_text = QPlainTextEdit(self.cpt_tab)
        self.cpt_output_text.setObjectName(u"cpt_output_text")
        self.cpt_output_text.setGeometry(QRect(380, 100, 231, 211))
        font2 = QFont()
        font2.setPointSize(15)
        self.cpt_output_text.setFont(font2)
        self.cpt_output_text.setFocusPolicy(Qt.ClickFocus)
        self.cpt_output_text.setTabChangesFocus(True)
        self.cpt_output_text.setPlainText(u"")
        self.cpt_correct_button = QPushButton(self.cpt_tab)
        self.cpt_correct_button.setObjectName(u"cpt_correct_button")
        self.cpt_correct_button.setGeometry(QRect(480, 360, 121, 41))
        self.cpt_correct_button.setFont(font1)
        self.line_4 = QFrame(self.cpt_tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(40, 330, 591, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.cpt_correct_text = QPlainTextEdit(self.cpt_tab)
        self.cpt_correct_text.setObjectName(u"cpt_correct_text")
        self.cpt_correct_text.setGeometry(QRect(40, 360, 431, 61))
        self.cpt_correct_text.setFont(font2)
        self.cpt_correct_text.setFocusPolicy(Qt.ClickFocus)
        self.cpt_correct_text.setTabChangesFocus(True)
        self.cpt_correct_text.setPlainText(u"")
        self.cpt_output_label_2 = QLabel(self.cpt_tab)
        self.cpt_output_label_2.setObjectName(u"cpt_output_label_2")
        self.cpt_output_label_2.setGeometry(QRect(440, 50, 91, 31))
        self.cpt_output_label_2.setFont(font1)
        self.success_label = QLabel(self.cpt_tab)
        self.success_label.setObjectName(u"success_label")
        self.success_label.setEnabled(False)
        self.success_label.setGeometry(QRect(270, 110, 91, 61))
        font3 = QFont()
        font3.setPointSize(18)
        self.success_label.setFont(font3)
        self.success_label.setAlignment(Qt.AlignCenter)
        self.success_label_2 = QLabel(self.cpt_tab)
        self.success_label_2.setObjectName(u"success_label_2")
        self.success_label_2.setEnabled(False)
        self.success_label_2.setGeometry(QRect(270, 240, 91, 61))
        self.success_label_2.setFont(font3)
        self.success_label_2.setAlignment(Qt.AlignCenter)
        self.correct_label = QLabel(self.cpt_tab)
        self.correct_label.setObjectName(u"correct_label")
        self.correct_label.setEnabled(False)
        self.correct_label.setGeometry(QRect(510, 410, 91, 21))
        font4 = QFont()
        font4.setPointSize(16)
        self.correct_label.setFont(font4)
        self.selection_tab.addTab(self.cpt_tab, "")
        self.icd_tab = QWidget()
        self.icd_tab.setObjectName(u"icd_tab")
        self.icd_input_text = QPlainTextEdit(self.icd_tab)
        self.icd_input_text.setObjectName(u"icd_input_text")
        self.icd_input_text.setGeometry(QRect(30, 100, 211, 211))
        self.icd_input_text.setFocusPolicy(Qt.ClickFocus)
        self.icd_input_text.setTabChangesFocus(True)
        self.icd_input_text.setPlainText(u"")
        self.icd_predict_button = QPushButton(self.icd_tab)
        self.icd_predict_button.setObjectName(u"icd_predict_button")
        self.icd_predict_button.setGeometry(QRect(250, 190, 121, 41))
        self.icd_predict_button.setFont(font1)
        self.icd_output_label = QLabel(self.icd_tab)
        self.icd_output_label.setObjectName(u"icd_output_label")
        self.icd_output_label.setGeometry(QRect(450, 10, 81, 21))
        self.icd_output_label.setFont(font1)
        self.icd_output_label.setAlignment(Qt.AlignCenter)
        self.line_2 = QFrame(self.icd_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 30, 591, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.icd_output_text = QPlainTextEdit(self.icd_tab)
        self.icd_output_text.setObjectName(u"icd_output_text")
        self.icd_output_text.setGeometry(QRect(380, 100, 231, 211))
        self.icd_output_text.setFont(font2)
        self.icd_output_text.setFocusPolicy(Qt.ClickFocus)
        self.icd_output_text.setTabChangesFocus(True)
        self.icd_output_text.setPlainText(u"")
        self.icd_output_label_2 = QLabel(self.icd_tab)
        self.icd_output_label_2.setObjectName(u"icd_output_label_2")
        self.icd_output_label_2.setGeometry(QRect(440, 50, 91, 31))
        self.icd_output_label_2.setFont(font1)
        self.line_5 = QFrame(self.icd_tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(40, 330, 591, 20))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.icd_text_label = QLabel(self.icd_tab)
        self.icd_text_label.setObjectName(u"icd_text_label")
        self.icd_text_label.setGeometry(QRect(90, 50, 101, 31))
        self.icd_text_label.setFont(font1)
        self.icd_correct_text = QPlainTextEdit(self.icd_tab)
        self.icd_correct_text.setObjectName(u"icd_correct_text")
        self.icd_correct_text.setGeometry(QRect(40, 360, 431, 61))
        self.icd_correct_text.setFont(font2)
        self.icd_correct_text.setFocusPolicy(Qt.ClickFocus)
        self.icd_correct_text.setTabChangesFocus(True)
        self.icd_correct_text.setPlainText(u"")
        self.icd_correct_button = QPushButton(self.icd_tab)
        self.icd_correct_button.setObjectName(u"icd_correct_button")
        self.icd_correct_button.setGeometry(QRect(480, 360, 121, 41))
        self.icd_correct_button.setFont(font1)
        self.icd_input_label = QLabel(self.icd_tab)
        self.icd_input_label.setObjectName(u"icd_input_label")
        self.icd_input_label.setGeometry(QRect(100, 10, 61, 21))
        self.icd_input_label.setFont(font)
        self.icd_input_label.setAlignment(Qt.AlignCenter)
        self.success_label_5 = QLabel(self.icd_tab)
        self.success_label_5.setObjectName(u"success_label_5")
        self.success_label_5.setEnabled(False)
        self.success_label_5.setGeometry(QRect(270, 110, 91, 61))
        self.success_label_5.setFont(font3)
        self.success_label_5.setAlignment(Qt.AlignCenter)
        self.success_label_6 = QLabel(self.icd_tab)
        self.success_label_6.setObjectName(u"success_label_6")
        self.success_label_6.setEnabled(False)
        self.success_label_6.setGeometry(QRect(270, 240, 91, 61))
        self.success_label_6.setFont(font3)
        self.success_label_6.setAlignment(Qt.AlignCenter)
        self.correct_label_4 = QLabel(self.icd_tab)
        self.correct_label_4.setObjectName(u"correct_label_4")
        self.correct_label_4.setEnabled(False)
        self.correct_label_4.setGeometry(QRect(510, 410, 71, 20))
        self.correct_label_4.setFont(font4)
        self.selection_tab.addTab(self.icd_tab, "")
        self.com_tab = QWidget()
        self.com_tab.setObjectName(u"com_tab")
        self.whole_input_text = QPlainTextEdit(self.com_tab)
        self.whole_input_text.setObjectName(u"whole_input_text")
        self.whole_input_text.setGeometry(QRect(30, 100, 211, 211))
        self.whole_input_text.setFocusPolicy(Qt.ClickFocus)
        self.whole_input_text.setTabChangesFocus(True)
        self.whole_input_text.setPlainText(u"")
        self.whole_predict_button = QPushButton(self.com_tab)
        self.whole_predict_button.setObjectName(u"whole_predict_button")
        self.whole_predict_button.setGeometry(QRect(250, 190, 121, 41))
        self.whole_predict_button.setFont(font1)
        self.whole_output_label = QLabel(self.com_tab)
        self.whole_output_label.setObjectName(u"whole_output_label")
        self.whole_output_label.setGeometry(QRect(450, 10, 81, 21))
        self.whole_output_label.setFont(font1)
        self.whole_output_label.setAlignment(Qt.AlignCenter)
        self.line_3 = QFrame(self.com_tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 30, 591, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.whole_cpt_output_text = QPlainTextEdit(self.com_tab)
        self.whole_cpt_output_text.setObjectName(u"whole_cpt_output_text")
        self.whole_cpt_output_text.setGeometry(QRect(380, 100, 221, 61))
        self.whole_cpt_output_text.setFont(font2)
        self.whole_cpt_output_text.setFocusPolicy(Qt.ClickFocus)
        self.whole_cpt_output_text.setTabChangesFocus(True)
        self.whole_cpt_output_text.setPlainText(u"")
        self.whole_cpt_output_label = QLabel(self.com_tab)
        self.whole_cpt_output_label.setObjectName(u"whole_cpt_output_label")
        self.whole_cpt_output_label.setGeometry(QRect(440, 50, 91, 31))
        self.whole_cpt_output_label.setFont(font1)
        self.line_6 = QFrame(self.com_tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(30, 310, 591, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.whole_text_label = QLabel(self.com_tab)
        self.whole_text_label.setObjectName(u"whole_text_label")
        self.whole_text_label.setGeometry(QRect(70, 50, 131, 31))
        self.whole_text_label.setFont(font1)
        self.whole_cpt_correct_text = QPlainTextEdit(self.com_tab)
        self.whole_cpt_correct_text.setObjectName(u"whole_cpt_correct_text")
        self.whole_cpt_correct_text.setGeometry(QRect(40, 330, 191, 61))
        self.whole_cpt_correct_text.setFont(font2)
        self.whole_cpt_correct_text.setFocusPolicy(Qt.ClickFocus)
        self.whole_cpt_correct_text.setTabChangesFocus(True)
        self.whole_cpt_correct_text.setPlainText(u"")
        self.whole_cpt_correct_button = QPushButton(self.com_tab)
        self.whole_cpt_correct_button.setObjectName(u"whole_cpt_correct_button")
        self.whole_cpt_correct_button.setGeometry(QRect(60, 400, 141, 41))
        self.whole_cpt_correct_button.setFont(font1)
        self.whole_input_label = QLabel(self.com_tab)
        self.whole_input_label.setObjectName(u"whole_input_label")
        self.whole_input_label.setGeometry(QRect(100, 10, 61, 21))
        self.whole_input_label.setFont(font)
        self.whole_input_label.setAlignment(Qt.AlignCenter)
        self.whole_icd_output_text = QPlainTextEdit(self.com_tab)
        self.whole_icd_output_text.setObjectName(u"whole_icd_output_text")
        self.whole_icd_output_text.setGeometry(QRect(380, 240, 221, 61))
        self.whole_icd_output_text.setFont(font2)
        self.whole_icd_output_text.setFocusPolicy(Qt.ClickFocus)
        self.whole_icd_output_text.setTabChangesFocus(True)
        self.whole_icd_output_text.setPlainText(u"")
        self.whole_icd_output_label = QLabel(self.com_tab)
        self.whole_icd_output_label.setObjectName(u"whole_icd_output_label")
        self.whole_icd_output_label.setGeometry(QRect(440, 190, 91, 31))
        self.whole_icd_output_label.setFont(font1)
        self.whole_icd_correct_text = QPlainTextEdit(self.com_tab)
        self.whole_icd_correct_text.setObjectName(u"whole_icd_correct_text")
        self.whole_icd_correct_text.setGeometry(QRect(390, 330, 191, 61))
        self.whole_icd_correct_text.setFont(font2)
        self.whole_icd_correct_text.setFocusPolicy(Qt.ClickFocus)
        self.whole_icd_correct_text.setTabChangesFocus(True)
        self.whole_icd_correct_text.setPlainText(u"")
        self.whole_icd_correct_button = QPushButton(self.com_tab)
        self.whole_icd_correct_button.setObjectName(u"whole_icd_correct_button")
        self.whole_icd_correct_button.setGeometry(QRect(420, 400, 141, 41))
        self.whole_icd_correct_button.setFont(font1)
        self.success_label_3 = QLabel(self.com_tab)
        self.success_label_3.setObjectName(u"success_label_3")
        self.success_label_3.setEnabled(False)
        self.success_label_3.setGeometry(QRect(270, 240, 91, 61))
        self.success_label_3.setFont(font3)
        self.success_label_3.setAlignment(Qt.AlignCenter)
        self.success_label_4 = QLabel(self.com_tab)
        self.success_label_4.setObjectName(u"success_label_4")
        self.success_label_4.setEnabled(False)
        self.success_label_4.setGeometry(QRect(270, 110, 91, 61))
        self.success_label_4.setFont(font3)
        self.success_label_4.setAlignment(Qt.AlignCenter)
        self.correct_label_2 = QLabel(self.com_tab)
        self.correct_label_2.setObjectName(u"correct_label_2")
        self.correct_label_2.setEnabled(False)
        self.correct_label_2.setGeometry(QRect(210, 411, 71, 20))
        self.correct_label_2.setFont(font4)
        self.correct_label_3 = QLabel(self.com_tab)
        self.correct_label_3.setObjectName(u"correct_label_3")
        self.correct_label_3.setEnabled(False)
        self.correct_label_3.setGeometry(QRect(350, 410, 71, 20))
        self.correct_label_3.setFont(font4)
        self.selection_tab.addTab(self.com_tab, "")

        self.retranslateUi(nlp_gui)

        self.selection_tab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(nlp_gui)
    # setupUi

    def retranslateUi(self, nlp_gui):
        nlp_gui.setWindowTitle(QCoreApplication.translate("nlp_gui", u"Form", None))
        self.cpt_input_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"Please enter CPT text here", None))
        self.cpt_input_text.clear()
        self.cpt_input_label.setText(QCoreApplication.translate("nlp_gui", u"Input", None))
        self.cpt_text_label.setText(QCoreApplication.translate("nlp_gui", u"CPT text", None))
        self.cpt_predict_button.setText(QCoreApplication.translate("nlp_gui", u"Predict", None))
        self.cpt_output_label.setText(QCoreApplication.translate("nlp_gui", u"Output: ", None))
        self.cpt_output_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"predicted CPT code", None))
        self.cpt_output_text.clear()
        self.cpt_correct_button.setText(QCoreApplication.translate("nlp_gui", u"Correct", None))
        self.cpt_correct_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"if the predicted label was wrong, please enter the correct label here and click the 'correct' button", None))
        self.cpt_correct_text.clear()
        self.cpt_output_label_2.setText(QCoreApplication.translate("nlp_gui", u"CPT Code", None))
        self.success_label.setText(QCoreApplication.translate("nlp_gui", u"Prediction\n"
"Completed", None))
        self.success_label_2.setText(QCoreApplication.translate("nlp_gui", u"Prediction\n"
"Completed", None))
        self.correct_label.setText(QCoreApplication.translate("nlp_gui", u"corrected", None))
        self.selection_tab.setTabText(self.selection_tab.indexOf(self.cpt_tab), QCoreApplication.translate("nlp_gui", u"CPT_Prediction", None))
        self.icd_input_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"Please enter ICD text here", None))
        self.icd_input_text.clear()
        self.icd_predict_button.setText(QCoreApplication.translate("nlp_gui", u"Predict", None))
        self.icd_output_label.setText(QCoreApplication.translate("nlp_gui", u"Output: ", None))
        self.icd_output_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"predicted ICD code", None))
        self.icd_output_text.clear()
        self.icd_output_label_2.setText(QCoreApplication.translate("nlp_gui", u"ICD Code", None))
        self.icd_text_label.setText(QCoreApplication.translate("nlp_gui", u"ICD text", None))
        self.icd_correct_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"if the predicted label was wrong, please enter the correct label here and click the 'correct' button", None))
        self.icd_correct_text.clear()
        self.icd_correct_button.setText(QCoreApplication.translate("nlp_gui", u"Correct", None))
        self.icd_input_label.setText(QCoreApplication.translate("nlp_gui", u"Input", None))
        self.success_label_5.setText(QCoreApplication.translate("nlp_gui", u"Prediction\n"
"Completed", None))
        self.success_label_6.setText(QCoreApplication.translate("nlp_gui", u"Prediction\n"
"Completed", None))
        self.correct_label_4.setText(QCoreApplication.translate("nlp_gui", u"corrected", None))
        self.selection_tab.setTabText(self.selection_tab.indexOf(self.icd_tab), QCoreApplication.translate("nlp_gui", u"ICD_Prediction", None))
        self.whole_input_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"Please enter radioloogy text", None))
        self.whole_input_text.clear()
        self.whole_predict_button.setText(QCoreApplication.translate("nlp_gui", u"Predict", None))
        self.whole_output_label.setText(QCoreApplication.translate("nlp_gui", u"Output: ", None))
        self.whole_cpt_output_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"predicted CPT code", None))
        self.whole_cpt_output_text.clear()
        self.whole_cpt_output_label.setText(QCoreApplication.translate("nlp_gui", u"CPT Code", None))
        self.whole_text_label.setText(QCoreApplication.translate("nlp_gui", u"Radiology Text", None))
        self.whole_cpt_correct_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"if wrong, correct CPT code here", None))
        self.whole_cpt_correct_text.clear()
        self.whole_cpt_correct_button.setText(QCoreApplication.translate("nlp_gui", u"CPT_correct", None))
        self.whole_input_label.setText(QCoreApplication.translate("nlp_gui", u"Input", None))
        self.whole_icd_output_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"predicted ICD code", None))
        self.whole_icd_output_text.clear()
        self.whole_icd_output_label.setText(QCoreApplication.translate("nlp_gui", u"ICD Code", None))
        self.whole_icd_correct_text.setPlaceholderText(QCoreApplication.translate("nlp_gui", u"if wrong, correct ICD code here", None))
        self.whole_icd_correct_text.clear()
        self.whole_icd_correct_button.setText(QCoreApplication.translate("nlp_gui", u"ICD_correct", None))
        self.success_label_3.setText(QCoreApplication.translate("nlp_gui", u"Prediction\n"
"Completed", None))
        self.success_label_4.setText(QCoreApplication.translate("nlp_gui", u"Prediction\n"
"Completed", None))
        self.correct_label_2.setText(QCoreApplication.translate("nlp_gui", u"corrected", None))
        self.correct_label_3.setText(QCoreApplication.translate("nlp_gui", u"corrected", None))
        self.selection_tab.setTabText(self.selection_tab.indexOf(self.com_tab), QCoreApplication.translate("nlp_gui", u"Whole_Text_Prediction", None))
    # retranslateUi

