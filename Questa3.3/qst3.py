#Desafio

def anagrama(palavra1,palavra2):
    lista1 = list(palavra1)
    lista2 = list(palavra2)

    lista1.sort()
    lista2.sort()

    posicao = 0
    iguais = True

    while posicao < len(palavra1) and iguais:
        if lista1[posicao]==lista2[posicao]:
            posicao = posicao + 1
        else:
            iguais = False

    return iguais

print(anagrama('ovo','voo'))


