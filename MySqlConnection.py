import mysql.connector as mysql
from mysql.connector import Error
from config import config

class MySqlConnection:
    instance = None
    con = None
    cursor = None

    
    def __new__(cls):
        if MySqlConnection.instance is None:
            MySqlConnection.instance = object.__new__(cls)
        return MySqlConnection.instance

   
    def __init__(self):
        if MySqlConnection.con is None:
            try:
                __db_config = config['mysql']
                
                MySqlConnection.con = mysql.connect(host = __db_config['host'], database = __db_config['db'], user = __db_config['user'], password = __db_config['password'])
                self.cursor = MySqlConnection.con.cursor()
                print('connessione aperta')
            except Error as e:
                print('Error: ', e)
    
    
    def query(self, query):
            self.cursor.execute(query)
            return self.cursor
    
    
    def __del__(self):
        try:
            if MySqlConnection.con is not None:
                MySqlConnection.con.close()
                print('connessione conclusa')
        except Error as e:
            print('Error: ', e)