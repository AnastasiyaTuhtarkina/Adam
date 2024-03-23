import sqlite3

class ProductDB:
    def __init__(self, connect: sqlite3.Connection) -> None:
        self.__connect = connect
        self.__cursor = connect.cursor()

    def getAllProduct(self):
        sql = 'SELECT id, name, img FROM products'
        try:
            self.__cursor.execute(sql)    
            return self.__cursor.fetchall()
        except:    
            print('ошибка чтения из базы данных')
            return []    
        
    def getProduct(self, id):
        sql = 'SELECT * FROM products WHERE id = ?'
        self.__cursor.execute(sql, tuple([id]))
        return self.__cursor.fetchone()    