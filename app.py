import os, sys, pycipher
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('stax.ui', self)

      # Stax Calendar Widget
      self.calendar = self.findChild(QtWidgets.QCalendarWidget, 'StaxCalendar')

      # Stax List Table
      self.lists = self.findChild(QtWidgets.QTableWidget, 'ListTable')

      # Top Bar Menu
      self.file = self.findChild(QtWidgets.QMenu, 'TopMenuFileBar')
      self.addList = self.findChild(QtWidgets.QAction, 'FileActionAddList')
      self.removeList = self.findChild(QtWidgets.QAction, 'FileActionRemoveList')
      self.updateList = self.findChild(QtWidgets.QAction, 'FileActionUpdateList')
      self.help = self.findChild(QtWidgets.QMenu, 'TopeMenuHelpBar')
      self.aboutStax = self.findChild(QtWidgets.QAction, 'HelpActionAboutStax')
      self.aboutStax.triggered.connect(self.aboutStaxHandler)

      # Show the app dialog
      self.show()

   # ############################ UI METHODS ############################
   def aboutStaxHandler(self):
      """
      'About Stax' Action Handler
      """
      aboutText = '''
      Stax is a to-do list app. Basically, you add your to-do list for the day (could be one, could be a whole bunch, which is why it's called Stax) and you write what you have to get done for that particular list. You can view it via the calendar when you click on it and update it or remove it whenever you want.
      Each to-do list also has individual sections to organize what subtasks are needed to get the overall to-do list done. These sections are part of overall goals you set for yourself.
      '''
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)
      msg.setText(aboutText)
      msg.setWindowTitle("About Stax")
      msg.setStandardButtons(QMessageBox.Ok)
      msg.exec_()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()