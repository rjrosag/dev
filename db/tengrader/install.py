import logging
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement

class TengraderInstall:
	def __init__(self, home=""):
		self.home = home 
		self.cluster = None
		self.session = None
		self.keyspace = None
		self.log = None

	def createsession(self):
		self.cluster = Cluster(['localhost'])
		self.session = self.cluster.connect(self.keyspace)

	def setlogger(self):
		log = logging.getLogger()
		log.setLevel('INFO')
		handler = logging.StreamHandler()
		handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(messages)s"))
		log.addHandler(handler)
		self.log = log

	def getsession(self):
		return (self.session)


	# Directory structure Add
	# DB Add 
	# Default value provision

# Main
if __name__ == "__main__":
	home = "/home/drosa/dev/db/tengrader"
	Installer = TengraderInstall(home)
	Installer.createsession()
	Installer.setlogger()
	'''
	References: 
	URL:
		https://techfossguru.com/apache-cassandra-python-step-step-guide-ubuntu-example/
	'''


