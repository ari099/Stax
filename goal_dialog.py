import os, sys
from datetime import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *
from db import *

class Goal(QtWidgets.QDialog):
   '''
   'Add Goal' Dialog Form Box
   '''
   def __init__(self):
      super(Goal, self).__init__()
      uic.loadUi("goal.ui", self)
      self.show()

      self.ok = self.findChild(QtWidgets.QPushButton, "AddGoalOKButton")
      self.cancel = self.findChild(QtWidgets.QPushButton, "AddGoalCancelButton")
      self.cancel.clicked.connect(self.closeWindow)
      self.search = self.findChild(QtWidgets.QTextEdit, "SubjectTextbox")
      self.search.textChanged.connect(self.searchHandler)

      self.goalTable = self.findChild(QtWidgets.QTableWidget, "GoalTable")
      goals = getGoals()
      self.goalTable.setRowCount(len(goals))
      for i in range(0, len(goals)):
         s = QtWidgets.QTableWidgetItem(goals[i][0])
         d = QtWidgets.QTableWidgetItem(goals[i][1])
         s.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
         d.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
         self.goalTable.setItem(i, 0, s)
         self.goalTable.setItem(i, 1, d)
   
   def closeWindow(self):
      '''
      Close Window
      '''
      self.close()
   
   def searchHandler(self):
      '''
      Search Box Handler
      '''
      self.goalTable.setRowCount(0)
      goals = searchGoals(self.search.toPlainText())
      self.goalTable.setRowCount(len(goals))
      for i in range(0, len(goals)):
         self.goalTable.setItem(i, 0, goals[i][0])
         self.goalTable.setItem(i, 1, goals[i][1])