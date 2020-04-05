import os, random, sys, sqlite3

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
   sql = "SELECT s.[Description], st.[Description] FROM Step st INNER JOIN Section s ON st.Section_ID=s.ID WHERE st.Day = '{0}'".format(day)
   return query(sql)