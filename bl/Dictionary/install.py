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
    cursor.execute("DROP TABLE IF EXISTS Attribute;")
    sql_command = '''CREATE TABLE IF NOT EXISTS Attribute (
                            id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, 
                            name VARCHAR(30),
                            type VARCHAR(10),
                            length INT,
                            format VARCHAR(15)                            
                            );
    '''
    cursor.execute(sql_command)
    cursor.close()
    mydb.commit()
    mydb.close()



sysdb = dictionarydb()
sysdb.create()