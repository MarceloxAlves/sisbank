import os
import time
import sqlite3

from Conta import Conta
from Conexao import Conexao

con = Conexao()
con = con.Open()
conta = Conta(con)
print("#################################################################################");
print("############################### BEM VINDO AO APP  ###############################");
print("#################################################################################\n\n");
rodando = True
while rodando:
	os.system('cls')
	print("#################################################################################");
	print("-----------------------------------SISBANK---------------------------------------")
	print("#################################################################################\n");
	l = input(" 1-Login\n 2-Cadastrar-se\n")
	if (not l):
		continue
	l = int(l)
	if(l==1):
		autenticado = conta.Autenticacao()
	if(l==2):
		nome =  input("NOME DO CLIENTE:\n")

		agencia =  input("AGENCIA:\n")
		agencia = int(agencia)

		numero =  input("NUMERO:\n")
		numero = int(numero)

		cadastra = conta.Insert(nome,agencia,numero)
		if(cadastra):
			print("\n Cadastro realizado com sucesso!\n")
			input('Pressione <ENTER> para Voltar')
		else:
			print("\n Erro ao cadastrar!\n")
			input('Pressione <ENTER> para Voltar')


	while autenticado:
		os.system('cls')
		print("#################################################################################");
		print("------------------------SISBANK---------- Logado como:",conta.getCliente())
		print("#################################################################################\n");
		op = input(" 1-Saldo\n 2-Sacar\n 3-Depositar\n 4-Logout\n ")
		if (not op):
			continue
		op = int(op)
		if(op==1):
			print("Seu saldo eh: ",conta.getSaldo())
		if(op==2):
			valor = input("Valor Solicitado: ")
			valor  = float(valor)
			if(conta.Sacar(valor)):
				print("Saque realizado com sucesso")
			else:
				print("Saldo Insuficiente")
		if(op==3):
			valor = input("Valor a Depositar: ")
			valor  = float(valor)
			if(conta.Depositar(valor)):
				print("Deposito realizado com sucesso")
			else:
				print("Erro ao Depositar")
		if(op==4):
			autenticado = False
			continue
		
		input('Pressione <ENTER> para continuar')
		

