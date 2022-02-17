import re


l, u, p, a = 0, 0, 0, 0

print("""Atencao! Sua senha preciso possui 
no mínimo 6 caracteres.
no mínimo 1 digito.
no mínimo 1 letra em minúsculo.
no mínimo 1 letra em maiúsculo.
no mínimo 1 caractere especial. 
Os caracteres especiais são: !@#$%^&*()-+
""")

nome = str(input("Digite seu usuario! "))
senha = str(input("Qual a sua senha? "))

if (len(senha) >= 6):
    for i in senha:
        if (i.islower()):
            l += 1
        if (i.isupper()):
            u += 1
        if (i.isdigit()):
            p += 1
        if (i == '@' or i == '$' or i == '-' or i == '!' or i == '#' or i == '%' or i == '()'
                or i == '*' or i == '+' or i == '^'):
            a += 1
if (l >= 1 and u >= 1 and p >= 1 and a >= 1 and l + u + p + a == len(senha)):
    print("Seja Bem vinda Débora")
else:
    print("Senha Fraca!")

