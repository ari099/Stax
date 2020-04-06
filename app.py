import os, sys
from datetime import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *
from db import *
from add_goal_dialog import AddGoal
from remove_goal_dialog import RemoveGoal
from update_goal_dialog import UpdateGoal

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('stax.ui', self)

      # Stax Calendar Widget
      self.calendar = self.findChild(QtWidgets.QCalendarWidget, 'StaxCalendar')
      self.calendar.clicked.connect(self.calendarSelect)

      # Stax Goal Table
      self.goals = self.findChild(QtWidgets.QTableWidget, 'ListTable')

      # Top Bar Menu
      self.file = self.findChild(QtWidgets.QMenu, 'TopMenuFileBar')
      self.createGoal = self.findChild(QtWidgets.QAction, 'FileActionCreateGoal')
      self.createGoal.triggered.connect(self.createGoalHandler)
      self.removeGoal = self.findChild(QtWidgets.QAction, 'FileActionRemoveGoal')
      self.removeGoal.triggered.connect(self.removeGoalHandler)
      self.updateGoal = self.findChild(QtWidgets.QAction, 'FileActionUpdateGoal')
      self.updateGoal.triggered.connect(self.updateGoalHandler)
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
      # Remove previous data
      self.goals.setRowCount(0)

      # Get the current date
      currentDate = self.calendar.selectedDate()

      # Get the steps based on the date
      steps = getSteps(currentDate.toString(Qt.ISODate))

      # Set the row count to the amount of steps found
      self.goals.setRowCount(len(steps))

      # Add in the steps as rows in the 'self.goals' table
      for i in range(0, len(steps)):
         sectionItem = QtWidgets.QTableWidgetItem(steps[i][0])
         sectionItem.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
         stepDescriptionItem = QtWidgets.QTableWidgetItem(steps[i][1])
         stepDescriptionItem.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
         stepDoneItem = QtWidgets.QTableWidgetItem("Done" if steps[i][2] == True else "Not Done")
         stepDoneItem.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
         self.goals.setItem(i, 0, sectionItem)
         self.goals.setItem(i, 1, stepDescriptionItem)
         self.goals.setItem(i, 2, stepDoneItem)

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
   
   def createGoalHandler(self):
      """
      'Add List' Action Handler
      """
      # Start 'Add Goal' Dialog
      dlg = AddGoal()
      dlg.exec_()

   def removeGoalHandler(self):
      """
      'Remove List' Action Handler
      """
      # Start 'Remove Goal' Dialog
      dlg = RemoveGoal()
      dlg.exec_()

   def updateGoalHandler(self):
      """
      'Update List' Action Handler
      """
      # Start 'Update Goal' Dialog
      dlg = UpdateGoal()
      dlg.exec_()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()