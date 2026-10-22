import random

def gerar_numero_aleatorio():
    rd = random.randint(1, 100)
    return rd

def verificar(numRd, number):
    if(number == numRd):
        print("Numero correto!!")
    elif(number > numRd):
        print("Menor")
    else:
        print("Maior")


def main():
    numRd = gerar_numero_aleatorio()
    acertou = False

    while(not acertou):
        number = int(input("Escreva um numero: "))
        verificar(numRd, number)
    
        acertou = (number == numRd)
main()