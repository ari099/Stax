from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *
from db import *

class UpdateGoal(QtWidgets.QDialog):
   '''
   'Add Goal' Dialog Form Box
   '''
   def __init__(self):
      super(UpdateGoal, self).__init__()
      uic.loadUi("update_goal.ui", self)
      self.show()

      self.ok = self.findChild(QtWidgets.QPushButton, "UpdateGoalOKButton")
      self.cancel = self.findChild(QtWidgets.QPushButton, "UpdateGoalCancelButton")
      self.cancel.clicked.connect(self.closeWindow)
   
   def closeWindow(self):
      '''
      Close Window
      '''
      self.close()