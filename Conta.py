import os
import time
class Conta:
	Conn = None
	Id,Saldo,Agencia,Numero,Cliente_id = None,None,None,None,None
	Cliente = None
  
	def __init__(self,con):
		self.Conn = con

	def setAtributos(self,tupla):
		self.Id,self.Saldo,self.Agencia,self.Numero,self.Cliente_id = tupla[0],tupla[1],tupla[2],tupla[3],tupla[4]
	
	def Autenticacao(self):
		print("------------ LOGIN -------------")
		agencia = input("Agencia:")
		nconta = input("Conta:")
		cursor = self.Conn.cursor()
		cursor.execute('SELECT * FROM Conta WHERE Agencia=? AND Numero=?', (agencia,nconta))
		c = cursor.fetchone()
		if(c==None):
			os.system('cls')
			print("Usuário Inválido!")
			time.sleep(1)
			return False
		else:
			self.setAtributos(c)
			os.system('cls')
			cursor = self.Conn.cursor()
			cursor.execute('SELECT * FROM Cliente WHERE Id=?', [c[4]])
			# retorna uma tupla
			cliente = cursor.fetchone()
		    # limpa a tela
			os.system('cls')
			print("Bem vindo ao sistema ",cliente[1])
			# seta o cliente na variavel da class Conta
			self.Cliente = cliente[1]
			print("Carregando... Aguarde")
			#aguarda 3 segundos para passar para a proxima operação
			time.sleep(3)
			return True

	def Depositar(self,valor):
		if(valor >= 0):
			self.Saldo  = self.Saldo + valor
			return self.Update()
		else:
			return False

	def Sacar(self,valor):
		if(self.Saldo - valor >= 0):
			self.Saldo  = self.Saldo - valor
			return self.Update()
		else:
			return False

	def getSaldo(self):
		self.Busca()
		return self.Saldo

		#retorna o cliente setado
	def getCliente(self):
		return self.Cliente 
		
		# Inserir registro no banco de dados
	def Insert(self,nome,agencia,numero):
		try:
			cursor = self.Conn.cursor()
			cursor.execute('INSERT INTO Cliente (Nome) VALUES (?)', [nome])
			self.Conn.commit()
			id_cliente  = cursor.lastrowid
			cursor.execute('INSERT INTO Conta (Agencia,Numero,Cliente_id) VALUES (?,?,?)', [agencia,numero,id_cliente])
			self.Conn.commit()
			return True
		except Exception as e:
			self.Conn.rollback()
			raise
			return False
		
		#Atualizar registro no banco de dados
	def Update(self):
		try:
			cursor = self.Conn.cursor()
			cursor.execute("""
				UPDATE Conta SET Saldo=? , Agencia=? , Numero=?, Cliente_id=? WHERE Id=?
				""", (self.Saldo,self.Agencia,self.Numero, self.Cliente_id, self.Id))
			self.Conn.commit()
			return True
		except Exception as e:
			self.Conn.rollback()
			raise
			return False

		# Busca um registro
	def Busca(self):
		cursor = self.Conn.cursor()
		cursor.execute('SELECT * FROM Conta WHERE Id=?', [self.Id])
		c = cursor.fetchone()
		self.setAtributos(c)
		
		

		
