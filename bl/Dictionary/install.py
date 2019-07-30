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
                            tablename VARCHAR(20), 
                            name VARCHAR(30),
                            type VARCHAR(50),
                            length INT,
                            _decimal INT,
                            format VARCHAR(15), 
                            _index VARCHAR(50),
                            _foreignkey VARCHAR(70),
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
          elif 'INDEX' in record:
              sql_command = 'INSERT INTO attribute (sys,tablename,type, _index) VALUES (' + record + ');'
          elif 'FOREIGN' in record:
              sql_command = 'INSERT INTO attribute (sys,tablename,type, _foreignkey) VALUES (' + record + ');'
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
             '"scf", "catalog", "type", "CHAR", 20',
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
sql_table = {'"scf", "generallayer", "id", "INT NOT NULL PRIMARY KEY AUTO_INCREMENT", 10, 0',
              '"scf", "generallayer", "account",  "INT", 10, 0',
              '"scf", "generallayer", "_date", "DATE"',
              '"scf", "generallayer", "debit", "INT", 15, 2',
              '"scf", "generallayer", "credit", "INT", 15, 2',
              '"scf", "generallayer", "status", "CHAR", 10',
              '"scf", "generallayer", "INDEX", "INDEX scfgenerallayer_account_idx (account)"',
              '"scf", "generallayer", "FOREIGNKEY","FOREIGN KEY (account) REFERENCES scfcatalog(id) ON DELETE CASCADE"'
             }
dict.put(sql_table)
sql_table = {'"scf", "journal", "id", "INT NOT NULL PRIMARY KEY AUTO_INCREMENT", 10, 0',
              '"scf", "journal", "account",  "INT", 10, 0',
              '"scf", "journal", "_date", "DATE"',
              '"scf", "journal", "debit", "INT", 15, 2',
              '"scf", "journal", "credit", "INT", 15, 2',
              '"scf", "journal", "status", "CHAR", 10',
              '"scf", "journal", "INDEX", "INDEX scfjournal_account_idx (account)"',
              '"scf", "journal", "FOREIGNKEY","FOREIGN KEY (account) REFERENCES scfcatalog(id) ON DELETE CASCADE"'
             }
dict.put(sql_table)
sql_table = {'"scf", "finance", "id", "INT NOT NULL PRIMARY KEY AUTO_INCREMENT", 10, 0',
              '"scf", "finance", "account",  "INT", 10, 0',
              '"scf", "finance", "type", "CHAR", 20',
              '"scf", "finance", "state", "CHAR", 10',
              '"scf", "finance", "begindate", "DATE"',
              '"scf", "finance", "enddate", "DATE"',
              '"scf", "finance", "amount", "INT", 15,2',
              '"scf", "finance", "budgetamount", "INT", 15,2',
              '"scf", "finance", "INDEX", "INDEX scffinance_account_idx (account)"',
              '"scf", "finance", "FOREIGNKEY","FOREIGN KEY (account) REFERENCES scfcatalog(id) ON DELETE CASCADE"'
             }
dict.put(sql_table)

sql_table = {'"scf", "policy", "id", "INT NOT NULL PRIMARY KEY AUTO_INCREMENT", 10, 0',
              '"scf", "policy", "account",  "INT", 10, 0',
              '"scf", "policy", "posttype",  "CHAR", 20',
              '"scf", "policy", "name", "CHAR", 50',
              '"scf", "policy", "status", "CHAR", 10',
              '"scf", "policy", "INDEX", "INDEX scfpolicy_account_idx (account)"',
              '"scf", "policy", "FOREIGNKEY","FOREIGN KEY (account) REFERENCES scfcatalog(id) ON DELETE CASCADE"'
             }
dict.put(sql_table)

sql_table = {'"scf", "Organizationbox", "id", "INT NOT NULL PRIMARY KEY AUTO_INCREMENT", 10, 0',
              '"scf", "Organizationbox", "date", "DATE"',
              '"scf", "Organizationbox", "actionitemdescription",  "CHAR", 50',
              '"scf", "Organizationbox", "actionitemdate", "DATE"',
              '"scf", "Organizationbox", "actionitemreference", "CHAR", 20',
              '"scf", "Organizationbox", "actionitemstatus", "CHAR", 20',
              '"scf", "Organizationbox", "actionitemlog", "TEXT", 50',
              '"scf", "Organizationbox", "actionitemcmd", "TEXT", 50',
              '"scf", "Organizationbox", "actionitemsme", "TEXT", 50',
              '"scf", "Organizationbox", "actionitemnextfollowup", "DATE"',
              '"scf", "Organizationbox", "actionitemtag", "TEXT", 50',
              '"scf", "Organizationbox", "financeid", "INT", 10, 0',
              '"scf", "Organizationbox", "INDEX", "INDEX Organizationbox_financeid_idx (financeid)"',
              '"scf", "Organizationbox", "FOREIGNKEY","FOREIGN KEY (financeid) REFERENCES scffinance(id) ON DELETE CASCADE"'
             }
dict.put(sql_table)

