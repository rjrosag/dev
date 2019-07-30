'''
Create the database for the app and demo data
'''
import mysql.connector
import os

class dictionarydb:
  def __init__(self):
    pass


  def create(self):
    sql_command = ""
    mydb = mysql.connector.connect(
        host=os.environ.get('DICTIONARY_DBHOST', "localhost"),
        user=os.environ.get('DICTIONARY_DBUSER', 'admin'),
        passwd=os.environ.get('DICTIONARY_DBPASSWORD', 'c0mcast!'))
    cursor = mydb.cursor(buffered=None)
    cursor.execute("CREATE DATABASE IF NOT EXISTS dictionary;")
    cursor.execute("USE dictionary;")
    cursor.execute("DROP TABLE IF EXISTS attribute;")
    sql_command = '''CREATE TABLE IF NOT EXISTS attribute (
                            attributeid INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                            sys VARCHAR(3),
                            tablename VARCHAR(10), 
                            name VARCHAR(30),
                            type VARCHAR(50),
                            length INT,
                            _decimal INT,
                            format VARCHAR(15), 
                            INDEX NAME (sys, tablename)                            
                            );
    '''
    cursor.execute(sql_command)
    cursor.close()
    mydb.commit()
    mydb.close()

  def put(self, table = {}):
      mydb = mysql.connector.connect(
          host=os.environ.get('DICTIONARY_DBHOST', "localhost"),
          user=os.environ.get('DICTIONARY_DBUSER', 'admin'),
          passwd=os.environ.get('DICTIONARY_DBPASSWORD', 'c0mcast!'))
      cursor = mydb.cursor(buffered=None)
      cursor.execute("USE dictionary;")
      for record in table:
          if 'INT' in record:
              sql_command = 'INSERT INTO attribute (sys,tablename,name,type,length,_decimal) VALUES ('+ record +');'
          elif 'DATE' in record:
              sql_command = 'INSERT INTO attribute (sys,tablename,name,type) VALUES (' + record + ');'
          else:
              sql_command = 'INSERT INTO attribute (sys,tablename,name,type,length) VALUES ('+ record +');'
          cursor.execute(sql_command)
      cursor.close()
      mydb.commit()
      mydb.close()





dict = dictionarydb()
dict.create()
sql_table = {'"scf", "catalog", "id", "INT NOT NULL PRIMARY KEY AUTO_INCREMENT", 10, 0',
              '"scf", "catalog", "name", "CHAR", 30',
              '"scf", "catalog", "control", "INT", 15, 0',
              '"scf", "catalog", "debit", "INT",  15, 2',
              '"scf", "catalog", "credit", "INT", 15, 2',
              '"scf", "catalog", "status", "CHAR", 10'}
dict.put(sql_table)

sql_table = {'"scf", "cycle", "id", "INT NOT NULL PRIMARY KEY AUTO_INCREMENT", 10, 0',
              '"scf", "cycle", "name", "CHAR", 30',
              '"scf", "cycle", "begindate", "DATE"',
              '"scf", "cycle", "enddate", "DATE"',
              '"scf", "cycle", "type", "CHAR", 15' ,
              '"scf", "cycle", "recurrency", "CHAR", 10',
              '"scf", "cycle", "priority", "INT", 3, 0',
              '"scf", "cycle", "status", "CHAR", 10'
             }
dict.put(sql_table)

