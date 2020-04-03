from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *
from custom import *

class AddGoal(QtWidgets.QDialog):
   '''
   'Add Goal' Dialog Form Box
   '''
   def __init__(self):
      super(AddGoal, self).__init__()