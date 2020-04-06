from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *
from db import *

class AddGoal(QtWidgets.QDialog):
   '''
   'Add Goal' Dialog Form Box
   '''
   def __init__(self):
      super(AddGoal, self).__init__()
      uic.loadUi("add_goal.ui", self)
      self.show()

      self.ok = self.findChild(QtWidgets.QPushButton, "AddGoalOKButton")
      self.cancel = self.findChild(QtWidgets.QPushButton, "AddGoalCancelButton")
      self.cancel.clicked.connect(self.closeWindow)
   
   def closeWindow(self):
      '''
      Close Window
      '''
      self.close()