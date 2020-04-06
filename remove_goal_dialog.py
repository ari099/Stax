from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *
from db import *

class RemoveGoal(QtWidgets.QDialog):
   '''
   'Add Goal' Dialog Form Box
   '''
   def __init__(self):
      super(RemoveGoal, self).__init__()
      uic.loadUi("remove_goal.ui", self)
      self.show()

      self.ok = self.findChild(QtWidgets.QPushButton, "RemoveGoalOKButton")
      self.cancel = self.findChild(QtWidgets.QPushButton, "RemoveGoalCancelButton")
      self.cancel.clicked.connect(self.closeWindow)
   
   def closeWindow(self):
      '''
      Close Window
      '''
      self.close()