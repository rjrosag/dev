from cassandra import ConsistencyLevel

class TengraderInstall:
	def __init__(self, home=""):
		self.home = home 
		print(self.home )
	# Directory structure Add
	# DB Add 
	# Default value provision

# Main
if __name__ == "__main__":
	home = "/home/drosa/dev/db/tengrader"
	Installer = TengraderInstall(home)


