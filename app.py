import os, sys, pycipher
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('enigma_cipher.ui', self)

      # Rotor Sliders
      self.rotorOne = self.findChild(QtWidgets.QSlider, 'RotorI')
      self.rotorOne.valueChanged.connect(self.rotorOneSlide)
      self.rotorTwo = self.findChild(QtWidgets.QSlider, 'RotorII')
      self.rotorTwo.valueChanged.connect(self.rotorTwoSlide)
      self.rotorThree = self.findChild(QtWidgets.QSlider, 'RotorIII')
      self.rotorThree.valueChanged.connect(self.rotorThreeSlide)

      # Rotor Start Positions Combo Box
      self.rotorStartPositions = self.findChild(QtWidgets.QComboBox, 'RotorStartPositions')
      self.rotorStartPositions.addItems(['V','B','Q'])

      # Rotor Labels
      self.rotorOneValue = self.findChild(QtWidgets.QLabel, 'RotorIShiftValue')
      self.rotorTwoValue = self.findChild(QtWidgets.QLabel, 'RotorIIShiftValue')
      self.rotorThreeValue = self.findChild(QtWidgets.QLabel, 'RotorIIIShiftValue')

      # Reflector Combo Box
      self.reflector = self.findChild(QtWidgets.QComboBox, 'Reflector')
      self.reflector.addItems(['A','B','C'])

      # Ring Combo Box
      self.ring = self.findChild(QtWidgets.QComboBox, 'Ring')
      self.ring.addItems(['V','B','Q'])

      # Plugboard Settings Table
      self.plugboard = self.findChild(QtWidgets.QTableWidget, 'PlugboardSettings')
      self.plugboard.setItem(0,0, QtWidgets.QTableWidgetItem("PO"))
      self.plugboard.setItem(0,1, QtWidgets.QTableWidgetItem("ML"))
      self.plugboard.setItem(0,2, QtWidgets.QTableWidgetItem("IU"))
      self.plugboard.setItem(0,3, QtWidgets.QTableWidgetItem("KJ"))
      self.plugboard.setItem(0,4, QtWidgets.QTableWidgetItem("NH"))
      self.plugboard.setItem(0,5, QtWidgets.QTableWidgetItem("YT"))
      self.plugboard.setItem(0,6, QtWidgets.QTableWidgetItem("GB"))
      self.plugboard.setItem(0,7, QtWidgets.QTableWidgetItem("VF"))
      self.plugboard.setItem(0,8, QtWidgets.QTableWidgetItem("RE"))
      self.plugboard.setItem(0,9, QtWidgets.QTableWidgetItem("DC"))

      # Show the app dialog
      self.show()
   
   # ###################################### UI EVENT HANDLERS ######################################
   def rotorOneSlide(self):
      self.rotorOneValue.setText(str(self.rotorOne.value()))

   def rotorTwoSlide(self):
      self.rotorTwoValue.setText(str(self.rotorTwo.value()))

   def rotorThreeSlide(self):
      self.rotorThreeValue.setText(str(self.rotorThree.value()))



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
