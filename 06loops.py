print("Loops--------------------------------------------------")
print("")
print("Loop para imprimir o valor de X num laço de 10 repetiçoes (FOR)")
for x in range (0, 10): print("Valor de X é :", x)
print("Loop para imprimir a lestras de uma string como BRASIL")
nome= 'BRASIL'
for letra in nome: print(letra)
print("Loop com While")
numero=10
while(numero>0):
    print(numero)
    numero= numero-1

numero=20
while True :
    numero = numero - 1
    if(numero == 4):
        continue
    else:
        print("TESTE", numero)
    if(numero == 2):
        break