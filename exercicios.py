#Exercicio número 1
#If the variable a is equal to 10, print the string "Hello World".

# temperatura = 15

# if (temperatura == 10):
#     print("Hello World")
# else:
#     print ("Não é igual a 10")

# List1 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
# List2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# for val in List1:
#     print(val, end =",")
    
# print ("\n")
    
# for x in range(26):
#     print(List2[x], end=",")

# Numero = 10

# if (Numero == 10):
#     print("O numero é par")
# else:
#     print ("O numero é impar")

# a = True

# while(a):
#     for x in range(100):
#         if x%2 == 0:
#             print(x,"é par", a)
#         else:
#             print(x,"é impar", a)
#     a = False

info = []

while (True):
    print("Nome", end=": ")
    nome:str = input()
    print("Morada", end=": ")
    morada:str = input()
    info.append({"nome":nome, "morada":morada})
    
    print("Presione 0 para sair", end=": ")
    if input() == "0":
        break
        
print(info)
print(info[0]["nome"])
print(info[0]["morada"])
