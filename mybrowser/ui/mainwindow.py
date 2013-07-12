# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature,  QUrl

from Ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_btnNavigate_released(self):
        """
        Slot invoked when Navigate button is pressed
        #TODO: check out this code, ensure it does cover all the possibilities
        """
        theUrl = self.txtUrl.text()
        if theUrl[0:7] != 'http://':
            theUrl = 'http://' + theUrl
        self.webView.setUrl(QUrl(theUrl))
    
    @pyqtSignature("QString")
    def on_webView_titleChanged(self, title):
        """
        Change title based on site
        """
        self.setWindowTitle(title)
    
    @pyqtSignature("QUrl")
    def on_webView_urlChanged(self, url):
        """
        Slot documentation goes here.
        """
        self.txtUrl.setText(url.toString())
    
    @pyqtSignature("")
    def on_txtUrl_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.on_btnNavigate_released()
