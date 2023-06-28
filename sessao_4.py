# Declarações condicionais
# if, elif, else

# dataNasc = 2045
# anoAtual = 2020
# idade = anoAtual - dataNasc

# a = 10
# b = 10

# if (idade <= 10):
#     print("És uma criança")
# elif (idade >= 10 and idade <= 12):
#     print("És uma coisa moderna que no meu tempo não existia")
# elif (idade > 12 and idade <= 19):
#     print ("És um adolescente")
# elif (idade > 19):    
#     print ("És um adulto")
# else:
#     print("Deves ser um extraterrestre")

# Cilo for
# Contador com ciclo for até 10

# myList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# for val in myList:
#     print(val, end = ",")

# print ("\n")

# for x in range(26):
#     print(myList[x], end=",")

# myDict ={"nome":"João", "apelido":"Silva", "idade":20}
# for key in myDict:
#     print (key, ":", myDict[])

# Fibronacci

# numero_de_termos = 100

# n1 = 0
# n2 = 1
# conta = 0

# while conta < numero_de_termos:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     conta += 1

# Ciclo for Numa Lista

# l1 = [1,2,3,4,5,6,7,8,9,10]
# k = 9

# for v in l1:
#     if v == k:
#         print("Encontrei")
#     else:
#         print("Não Encontrei")

# um programa que encontra numeros divisivel por 5 ou 7 entre 1500 e 2700

# inicio = 1500
# final = 2700

# # % é o resto da divissão

# for numero in range(inicio, final):
    
#     if numero % 5 == 0:
#         print( numero, "é divisivel por 5" )
#     if numero % 7 == 0:
#         print( numero, "é divisivel por 7" )

# para saber os numeres impares dor pares

# listA = range(1465,1672,3)
# par = 0
# impar = 0
# for x in listA:
#     if x % 2 == 0:
#         par +=1
#         print(par, "par")
#     else:
#         impar +=1
#         print(impar, "impar")