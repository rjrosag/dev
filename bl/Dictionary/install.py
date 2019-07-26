'''
Create the database for the app and demo data
'''
import mysql.connector
import os

class dictionarydb:
  def __init__(self):
    self.host = os.environ.get('DICTIONARY_DBHOST', "localhost")
    self.user = os.environ.get('DICTIONARY_DBUSER', 'admin')
    self.passwd = os.environ.get('DICTIONARY_DBPASSWORD', 'c0mcast!')


  def create(self, host, user, passwd):
    mydb = mysql.connector.connect(
        host=os.environ.get('DICTIONARY_DBHOST', "localhost"),
        user=os.environ.get('DICTIONARY_DBUSER', 'admin'),
        passwd=os.environ.get('DICTIONARY_DBPASSWORD', 'c0mcast!'))
    cursor = mydb.cursor(buffered=None)
    cursor.execute("CREATE DATABASE IF NOT EXISTS dictionary;")
    xcursor.close()
    mydb.commit()
    mydb.close()

host = os.environ.get('DICTIONARY_DBHOST', "localhost")
user = os.environ.get('DICTIONARY_DBUSER', 'admin')
passwd = os.environ.get('DICTIONARY_DBPASSWORD', 'c0mcast!')

sysdb = dictionarydb()
sysdb.create(host, user, passwd)