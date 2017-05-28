import sqlite3
class Conexao:
    def __init__(self):
    	pass
    def Open(self, filename = 'banco.db'):
    	return sqlite3.connect(filename)