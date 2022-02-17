
print("Algoritimo escada: ")
quantidade = int(input("Digite a quantidade de desgraus da escada: "))
degraus = '*'

for num in range(1, quantidade):
  print(f'{" " + num * degraus + " "}')