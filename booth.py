#Thiago Chim Silvera - 110668
#Trabalho de Arquitetura - Implementacao do algortimo de Booth

def decimal_binario(x):
	result = []
	test_negative = x
	if (x<0):                #Testa se x e negativo
		x = -x
	while (x>=2):              #Faz a divisao por 2 e usa o resto para formar o binario
		result.append(x%2)
		x = int(x/2)
	if (x!=0):
		result.append(1)
	if (len(result)<5):
		cont = 5-len(result)
		while (cont>0):
			result.append(0)
			cont = cont - 1
	result.reverse()
	if ((test_negative)<0):         #Se x for negativo inverte e adicona +1
		for cont in range(5):
			if (result[cont]==0):
				result[cont] = 1
			else:
				result[cont] = 0
		result = soma_binarios(result, [0,0,0,0,1])
	return result

def binario_decimal(x): 	
	cont = 0 
	n = 0
	x.reverse()
	while (cont<10):                 #Faz o somatorio para formar o decimal
		n = n + x[cont]*2**cont
		cont += 1
	if (x[9])==1:                    #Arruma o decimal caso seja um binario negativo
		n = n - 512*2
	return n

def soma_binarios(a,b):
	result = []
	if len(a)>len(b):                 #Cria uma lista do tamanho do maior binario
		n = len(a) - 1
		while (n>-1):		
			result.append(0)
			n -= 1
		n = len(a) - 1
	else:
		n = len(b) - 1
		while (n>-1):
			result.append(0)
			n -= 1
		n = len(b) - 1
	carry = 0
	while (n>-1):                                 #Faz a conta de soma de binarios
		if (a[n]==0 and b[n]==0 and carry==0):
			result[n] = 0
			carry = 0
		elif (a[n]==0 and b[n]==0 and carry==1):
			result[n] = 1
			carry = 0
		elif (a[n]!=b[n] and carry == 0):
			result[n] = 1
			carry = 0
		elif (a[n]!=b[n] and carry == 1):
			result[n] = 0
			carry = 1
		elif (a[n]==1 and b[n]==1 and carry==0):
			result[n] = 0
			carry = 1
		elif (a[n]==1 and b[n]==1 and carry==1):
			result[n] = 1
			carry = 1
		n -= 1
	return result


def booth(a,b):
	x = 5
	y = 5
	adi = [0,0,0,0,0,0,0,0,0,0,0]
	sub = [0,0,0,0,0,0,0,0,0,0,0]
	pro = [0,0,0,0,0,0,0,0,0,0,0]
	comp = [0,0,0,0,0]
	print(adi)
	print(sub)
	print(pro, "\n")
	n = 0 
	while (n!=x):               #Preenche lista de adicao com multiplicando
		adi[n] = a[n]
		n += 1
	for cont in range(x):		#Inverte o multiplicando
		if (a[cont]==0):
			comp[cont] = 1
		else:
			comp[cont] = 0
	comp = soma_binarios(comp, [0,0,0,0,1])   #Soma 1 ao inverso do multiplicando
	n = 0
	while (n!=y):
		sub[n] = comp[n]      #Preenche lista subtracao com o inverso do multiplicando
		n += 1
	n = 5
	while (n!= 10):          #Preenche a segunda parte da lista do produto com o multiplicador
		pro[n] = b[n-5]
		n += 1
	#raw_input("***Pressione enter para continuar***\n")
	print(adi)
	print(sub)
	print(pro, "\n")
	n = 1
	while (n!=y+1):                                     #Faz as operacoes do algortimo de Booth
		print(pro, "\n")
		if (((pro[9])==0) and ((pro[10])==1)):
			print("01 Produto = Produto + Adicao\n")
			pro= soma_binarios(pro, adi)
		elif (((pro[9])==1) and ((pro[10])==0)):
			print("01 Produto = Produto + Subtracao\n")
			pro= soma_binarios(pro, sub)
		elif ((pro[9])==(pro[10])):
			print("00 ou 11, Nao faz nada\n")
		comp = [0,0,0,0,0,0,0,0,0,0,0]
		comp[0] = pro[0]
		c = 0
		while (c!=10):
			comp[c+1] = pro[c]
			c += 1
		c = 0
		while (c!=11):
			pro[c] = comp[c]
			c += 1
		n += 1
		#raw_input("***Pressione enter para continuar***\n")
	pro.pop()
	return pro
		

def main():
	x = decimal_binario(eval(input("Primeiro Numero: ")))
	print("Em complemento de 2, com 5 bits: ", x, "\n")
	y = decimal_binario(eval(input("Segundo Numero: ")))
	print("Em complemento de 2, com 5 bits: ", y, "\n")
	#raw_input("Pressione enter para comecar a multiplicao\n")
	result = booth(x,y)
	print("O Resultado da multiplicacao em binario e: ", result, "\n")
	result_2 = binario_decimal(result)
	print("O Resultado da multiplicacao em decimal e: ", result_2, "\n")

main()
