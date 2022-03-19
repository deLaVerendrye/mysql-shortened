from ast import Raise
from distutils.log import error
import mysql.connector

class Connection():

    def __init__(self, host='localhost', user='root', password='', db=''):
        if db != '':
            self.conn = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = db
            )
        else:
            self.conn = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
            )
        self.mycursor =  self.conn.cursor()
        self.syntaxError = 'You have an error in your SQL syntax'
    

    def CheckConnection(self):
        return self.conn


    def query(self, query):
        try:
            if query.find('INSERT') == 0:
                    self.mycursor.execute(query)
                    self.conn.commit()
                    return self.mycursor.rowcount, 'record inserted'
            elif query.find('CREATE') == 0:
                try:
                    self.mycursor.execute(query)
                    return 0
                except:
                    raise Exception(self.syntaxError)
            else:
                    result = []
                    self.mycursor.execute(query)
                    for i in self.mycursor:
                        result.append(i)
                    return result
        except:
            raise Exception(self.syntaxError)
        
        
    def queryMultiple(self, query, values):
        try:
            self.mycursor.executemany(query, values)
            self.conn.commit()
            return 0
        except:
            raise Exception(self.syntaxError)
