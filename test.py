#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Um programa simples feito a partir de um fluxograma simples.
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	print('Está chovendo lá fora?')
	resp = raw_input()
	if resp == 's':
		# Chovendo...
		print('Tem um casaco e um guarda-chuva?')
		resp = raw_input()
		if resp == 's':
			resp = 'go_covered'
		else:
			resp = 'no_cover'
		# "Loop lock"
		while resp != 'n':
			print('Então espera mais um pouco.')
			print('Está chovendo?')
			resp = raw_input()		
	if resp == 'go_covered':
		print('(Você saiu de guarda-chuva.)')
	else:
		print('~ Bro, faz sol! ~')
		print('(Você saiu.)')
# END of the "impossible code"

# Teste de loops n' stuff. Variável do input não é alterada no primeiro bloco.
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	print('Digite um número:')
	num = input()
	print('O dobro do número é: ' + str(num*2))
	for i in range(num):
	    print('i\'m outside. Hello SP! (' + str(i+1) + ')')

	print('')
	print('Soma de Gauss:')
	soma = 0
	for i in range(101):
	    soma += i
	print(str(soma))

	print('')
	import random
	print(str(random.randint(-10, 10)))

	print('')
	import sys
	txt = ''
	while True:
	    print('AAA!')
	    txt = raw_input()
	    if txt == 'sair':
		    sys.exit()
	    elif txt == 'vai':
		    continue
	    else:
		    break
	print('(end of the program)')
# END of the "impossible code"

# Programa de adivinhação "bem loko, empolgante".
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	import random
	lim = random.randint(50, 100)
	mind = random.randint(1, lim)
	tent = 0
	print('Estou pensando em um número entre 1 e ' + str(lim) + '...')
	print('E você vai ter que adivinhá-lo!')
	while True:
		tent += 1
		print('Qual é o número?')
		try:
			n = int(input())
			if n == mind:
				print('Muito bem, você acertou!')
				break
			elif n < mind:
				print('O número certo é maior que esse...')
			elif n > mind:
				print('O número certo é menor que esse...')
		except:
			print('Ah, mas pra acertar, você tem que digitar um NÚMERO!')
	print('Até acertar, você tentou ' + str(tent) + ' vezes.')
# END of the "impossible code"

# Teste de functions.
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	print('i\'m here \'cause i\'m happy')
	print('big', 'thunder', 'cats')
	def fatorial(x):
		if x > 0:
			return x * fatorial(x - 1)
		else:
			return 1
	num = 0
	print('Digite um número:')
	num = input()
	print('O fatorial é: ' + str(fatorial(num)))

	x = 22
	def tag():
		x = 50
		print(str(x) + ' (local)')
	print(str(x) + ' (global)')
	tag()

	def inverse(x):
		try:
			return 1 / float(x)
		except ZeroDivisionError:
			print('OH CARAMBA, NÃO SE DIVIDE POR ZERO NÃO!')
			return 'indefinido'
	print('Digite um número:')
	num = input()
	print('O inverso do número é: ' + str(inverse(num)))
# END of the "impossible code"

# Testes com lists.
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	print('~ Enchendo linguiça numa lista em Python, v0.1 ~')
	lista1 = []
	lista2 = []
	while True:
		print('Digite alguma coisa. (Enter para parar)')
		value = raw_input()
		if value != '':
			lista1 += value
			lista2 += [value]
		else:
			break
	print(str(lista1))
	print(str(lista2))
	for i in range(len(lista2)):
		print(lista2[i])
	print('')
	a, b = ' de nada!', '...nadica'
	a, b = b, a
	print(a + b)
	print('')
	array = ['item1', 'itemVasco', 225]
	print(array) # implicit conversion - str(array)
	array.append('quadra')
	print(array)
	array = array.append('Borracha quântica.')
	print(array)
# END of the "impossible code"

# Mexendo um pouco com dicionários...
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	dicio = {'grou': 130, 'leopardo': 70}
	for i, j in dicio.items():
	    print('Key: ' + i + ' Value: ' + str(j))
	print('A altura média do grou é: ' + str(dicio.get('grou', 0)))
	print('Novamente, é: ' + str(dicio['grou']))
	print('E a do menor inseto é: ' + str(dicio.get('inseto', 0)))
	print('')
	# Contagem de caracteres
	def contagem(frase):
		import pprint
		count = {}
		for char in frase:
		    count.setdefault(char, 0)
		    count[char] += 1
		pprint.pprint(count)
	contagem('Master of Puppets, I am pulling your strings')
	print('')
	contagem('Memórias Póstumas de Brás Cubas.')
# END of the "impossible code"

# Um incrível e excelente jogo da velha!
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	board = {'0': ' ', '1': ' ', '2': ' ',
			'3': ' ', '4': ' ', '5': ' ',
			'6': ' ', '7': ' ', '8': ' '}
	num = 0

	# Mostra a situação da partida
	def print_board(dc):
		for i in range(3):
			print(' ' + dc[str(i*3)] + ' | ' + dc[str(i*3+1)] + ' | ' + dc[str(i*3+2)])

	# O adversário necessário
	def cpu_play(dc):
		import random
		n = random.randint(0, 8)
		if dc[str(n)] == ' ':
			dc[str(n)] = 'O'        
		else:
			cpu_play(dc)

	# Checar se há um vencedor
	def verifica_win(dc):
		# Linhas
		for i in range(3):
			if dc[str(i*3)] == dc[str(i*3+1)] and dc[str(i*3+1)] == dc[str(i*3+2)]:
				if dc[str(i*3)] != ' ':
					return 1
		# Colunas
		for i in range(3):
			if dc[str(i)] == dc[str(i+3)] and dc[str(i+3)] == dc[str(i+6)]:
				if dc[str(i)] != ' ':
					return 1
		# Diagonais
		if dc['0'] == dc['4'] and dc['4'] == dc['8']:
			if dc['0'] != ' ':
				return 1
		if dc['2'] == dc['4'] and dc['4'] == dc['6']:
			if dc['2'] != ' ':
				return 1

	# Apresentações, entradas e loop principal do jogo
	for i in range(3):
		print(' ' + str(i*3+1) + ' | ' + str(i*3+2) + ' | ' + str(i*3+3))
	while num != -1:
		print('Escolha um número entre 1 e 9:')
		try:
			num = input()
		except NameError:
			continue
		if num < 1 or num > 9:
			continue
		if board[str(num-1)] == ' ':
			# Vez do jogador
			board[str(num-1)] = 'X'
			print_board(board)
			if not verifica_win(board):
				print('(Vez da CPU.)')
				cpu_play(board)
				print_board(board)
			else:
				print_board(board)
				continue
			if verifica_win(board):
				print('~ Ao vencedor, as batatas! ~')
				break
# END of the "impossible code"

# Um "dicionário de dicionários", e recuperação de dados.
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
				'Bob': {'sandwiches': 3, 'apples': 2},
				'Carol': {'cups': 3, 'a_pies': 1}}

	def totalBrought(guests, item):
		numBrought = 0
		for k, v in guests.items():
			numBrought = numBrought + v.get(item, 0)
		return numBrought

	print('Number of things being brought:')
	print(' - Apples:     ' + str(totalBrought(allGuests, 'apples')))
	print(' - Cups:       ' + str(totalBrought(allGuests, 'cups')))
	print(' - Cakes:      ' + str(totalBrought(allGuests, 'cakes')))
	print(' - Sandwiches: ' + str(totalBrought(allGuests, 'sandwiches')))
	print(' - Apple pies: ' + str(totalBrought(allGuests, 'a_pies')))
# END of the "impossible code"

# Modificando o inventário de um jogo estilo RPG!
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	def addToInventory(inventory, addedItems):
		for k in addedItems:
			if k in inventory.keys():
				inventory[k] += 1
			else:
				inventory.setdefault(k, 1)
		return inventory

	inv = {'gold coin': 42, 'rope': 1}
	displayInventory(inv)

	dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
	inv = addToInventory(inv, dragonLoot)

	displayInventory(inv)
# END of the "impossible code"

# Exemplo de impressão de uma tabela.
# (P.S.: "if 0 > 1:" & indent is just some multiline commenting...)
if 0 > 1:
	tableData = [['apples', 'oranges', 'cherries', 'banana'],
				['Alice', 'Bob', 'Carol', 'David'],
				['dogs', 'cats', 'moose', 'goose']]
	siz = []
	txt = ''

	# Loops para encontrar as strings mais longas
	for i in range(3):
		tam = 0
		for j in range(4):
			if len(tableData[i][j]) > tam:
				tam = len(tableData[i][j])
			siz += [tam]

	# Composição do texto
	for j in range(4):
		for i in range(3):
			txt += tableData[i][j].rjust(siz[i]) + ' '
		txt += '\n'

	print(txt)
# END of the "impossible code"

print('and that, my friend, is totally out of bounds.')
