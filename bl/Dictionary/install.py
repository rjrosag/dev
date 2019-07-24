'''
Create the database for the app and demo data
'''
import mysql.connector
import os


class DictionaryDB(mysql):
    def __init__(self, host="localhost", user = "", password=""):
        self.host = host
        self.user = user
        self.password = password
        self.systemdb = ""

    @property
    def serverConnect(self):

        self.systemdb = mysql.connector.connection(
            self.host,
            self.user,
            self.password)
        return(self.systemdb)
    #
    # def run(self, sqlstatement = ""):
    #     cursor = self.systemdb.cursor(buffered=None)
    #
    #     # Creating dabase system
    #     cursor.execute(sqlstatement)
    #     cursor.close()
    #
    # def save(self):
    #     self.systemdb.commit()
    #     self.systemdb.close()


host = os.environ.get('DICTIONARY_DBHOST', "localhost")
user = os.environ.get('DICTIONARY_DBUSER', 'admin')
password = os.environ.get('DICTIONARY_DBPASSWORD', 'c0mcast!')

dict = DictionaryDB(host, user, password)
#conn = dict.serverConnect()
pass
#     dict.run("CREATE DATABASE IF NOT EXISTS dictionary;")
#     dict.run("USE dictionary;")
#     dict.run("CREATE TABLE IF NOT EXISTS attribute (attribute_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, system_id CHAR(3) NOT NULL, table_name CHAR(7) NOT NULL, attribute_name CHAR(10), attribute_type CHAR(10)  NOT NULL, attribute_size CHAR(10));")
#     dict.save()




# cursor.execute("CREATE DATABASE IF NOT EXISTS dictionary;")
# cursor.execute("USE dictionary;")
# cursor.execute("CREATE TABLE IF NOT EXISTS attribute (attribute_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, system_id CHAR(3) NOT NULL, table_name CHAR(7) NOT NULL, attribute_name CHAR(10), attribute_type CHAR(10)  NOT NULL, attribute_size CHAR(10));")



# rollback
# cursor.execute("USE dictionary;")
# cursor.execute("DROP TABLE IF EXISTS port;")
# cursor.execute("DROP DATABASE dictionary;")

# cursor.close()
# systemdb.commit()
# systemdb.close()

