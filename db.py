import os, random, sys, sqlite3
from datetime import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *

# Database Methods
def query(sql):
   '''
   Query the SQLite 3 database
   :param sql: SQL Query
   '''
   results = None
   try:
      db = sqlite3.connect("./db/stax.sqlite3")
      if sql[0:6].lower() == 'select':
         cursor = db.execute(sql)
         results = list()
         for row in cursor:
            results.append(row)
      else:
         db.execute(sql)
         db.commit()
   except ValueError as e:
      print('Error on line {}:'.format(sys.exc_info()[-1].tb_lineno), e)
   finally:
      db.close()
      if results is not None:
         return results

def addGoal(subject, description):
   '''
   Add Goal to Database
   :param subject: Goal Subject
   :param description: Goal List
   '''
   goalID = random.randint(1, 100)
   sql = '''
   INSERT INTO Goal
   VALUES ({0}, '{1}', '{2}')
   '''.format(goalID, subject, description)
   return query(sql)

def removeGoal(goalID):
   '''
   Remove Goal from Database
   :param goalID: Goal ID
   '''
   sql = '''
   DELETE FROM Goal
   WHERE ID = {0}
   '''.format(goalID)
   return query(sql)

def getGoals():
   '''
   Get all the goals
   '''
   return query("SELECT Subject, [Description] FROM Goal")

def searchGoals(pattern):
   '''
   Search goals by subject
   :param pattern: Pattern for searching by subject
   '''
   results = query("SELECT Subject, [Description] FROM Goal WHERE Subject LIKE '%{0}%'".format(pattern))
   goals = []
   for i in range(0, len(results)):
      s = QtWidgets.QTableWidgetItem(results[i][0])
      d = QtWidgets.QTableWidgetItem(results[i][1])
      s.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
      d.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
      goals.append([s, d])
   
   return goals

def addSection(goalID, description):
   '''
   Add section to goal
   :param goalID: Goal ID
   :param description: Section Description
   :param steps: Steps to fulfill section
   '''
   sectionID = random.randint(1, 1000)
   sql = '''
   INSERT INTO Section
   VALUES ({0}, '{1}', {2})
   '''.format(sectionID, description, goalID)
   return query(sql)

def removeSection(sectionID):
   '''
   Remove section from goal
   :param sectionID: Section ID
   '''
   sql = '''
   DELETE FROM Section
   WHERE ID = {0}
   '''.format(sectionID)
   return query(sql)

def getSections(goalID):
   '''
   Get sections by goal ID
   :param goalID: Goal ID
   '''
   sql = "SELECT g.Subject, s.[Description] FROM Section s INNER JOIN Goal g ON s.Goal_ID=g.ID WHERE s.Goal_ID = {0}".format(goalID)
   return query(sql)

def searchSections(pattern):
   '''
   Search sections by description pattern
   :param pattern: Description Pattern
   '''
   return query("SELECT [Description] FROM Section WHERE [Description] LIKE '%{0}%'".format(pattern))

def addStep(sectionID, description, day):
   '''
   Add step to section
   :param sectionID: Section ID
   :param description: Section Description
   :param day: Day to fulfill step
   '''
   stepID = random.randint(1,10000)
   sql = '''
   INSERT INTO Step
   VALUES ({0}, '{1}', '{2}', {3})
   '''.format(stepID, description, day, sectionID)
   return query(sql)

def removeStep(stepID):
   '''
   Remove step from database
   :param stepID: Step ID
   '''
   sql = '''
   DELETE FROM Step
   WHERE ID = {0}
   '''.format(stepID)
   return query(sql)

def getSteps(day):
   '''
   Get all the steps with their section IDs and description
   :param day: Date in ####-##-## format
   '''
   sql = "SELECT s.[Description], st.[Description], st.Done FROM Step st INNER JOIN Section s ON st.Section_ID=s.ID WHERE st.Day = '{0}'".format(day)
   return query(sql)

def searchSteps(pattern):
   '''
   Search steps by description pattern
   :param pattern: Description Pattern
   '''
   return query("SELECT [Description] FROM Step WHERE [Description] LIKE '%{0}%'".format(pattern))