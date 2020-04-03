import os, sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *
from custom import *
from add_goal_dialog import AddGoal

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('stax.ui', self)

      # Stax Calendar Widget
      self.calendar = self.findChild(QtWidgets.QCalendarWidget, 'StaxCalendar')
      self.calendar.clicked.connect(self.calendarSelect)

      # Stax List Table
      self.lists = self.findChild(QtWidgets.QTableWidget, 'ListTable')

      # Top Bar Menu
      self.file = self.findChild(QtWidgets.QMenu, 'TopMenuFileBar')
      self.createGoal = self.findChild(QtWidgets.QAction, 'FileActionCreateGoal')
      self.createGoal.triggered.connect(self.addListHandler)
      self.removeGoal = self.findChild(QtWidgets.QAction, 'FileActionRemoveGoal')
      self.removeGoal.triggered.connect(self.removeListHandler)
      self.updateGoal = self.findChild(QtWidgets.QAction, 'FileActionUpdateGoal')
      self.updateGoal.triggered.connect(self.updateListHandler)
      self.help = self.findChild(QtWidgets.QMenu, 'TopeMenuHelpBar')
      self.aboutStax = self.findChild(QtWidgets.QAction, 'HelpActionAboutStax')
      self.aboutStax.triggered.connect(self.aboutStaxHandler)

      # Show the app dialog
      self.show()

   # ############################ UI METHODS ############################
   def calendarSelect(self):
      '''
      Calendar Select Handler
      '''
      currentDate = self.calendar.selectedDate()
      print(getSteps(currentDate.toString(Qt.ISODate)))

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
   
   def addListHandler(self):
      """
      'Add List' Action Handler
      """
      pass

   def removeListHandler(self):
      """
      'Remove List' Action Handler
      """
      pass

   def updateListHandler(self):
      """
      'Update List' Action Handler
      """
      pass

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()