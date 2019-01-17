import sqlite3
import sys
import os

class:
	__init__(self):
		self.home = os.environ["HOME"]
		self.db_path = self.home
		self.dbconnection = ""

	def getDbPath(self):
		if sys.platform == 'win32':
			self.db_path = 'rrosa\\dev\\db\\config
		else: 
			self.db_path = self.home + '/Documents/cmc/db/config'
	return(self.db_path)

	def dbOpen(self, table=""):
		conn = sqlite3.connect(table)
		retun(conn)
	
	def dbExecute(self, statement = ""):
		sqlstatement = statement
		if self.dbconnection:     
			cursor = self.dbconnection.cursor()
			with closing(cursor) as c:  
				c.execute(sqlstatement)

	def dbgetRecord(self, statement= ""):
		record = ""
		sqlstatement = statement
		if self.dbconnection:
			with closing(self.dbconnection.cursor()) as c:
				c.execute(sqlstatement, (5,))
				record = c.fetchone()
		return(record)

	def dbgetRecords(self, statement = ""):
		records = ""
		sqlstatement = statement
		if self.dbconnection:
			with closing(self.dbconnection.cursor()) as c:
				c.execute(sqlstatement, (90,))
				records = c.fetchall()
		return(records)			 	
