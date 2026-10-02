# Iterando dicionário
import os
os.system('cls')

prods = {
    "cod": "123abc",
    "name": "Caixa de sapato vazia",
    "fabr": "Caixeiro Viajante",
    "preco": 120.99
}

print(prods)
print()

for prod in prods:
    #print(prods[prod])
    print(f' • {prod} - {prods[prod]}')

print()
print('------', prods.keys()) # Aqui eu converto uma tupla com lista nessa função 
for prod in prods.keys():
    print(prod)

print()
for prod in prods.values():
    print(prod)  

print()
# Para pegar um dicionário inteiro eu vou precisar criar duas variáveis 
print('------', prods.items())
for prod_key, prod_value in prods.items():
     print(f' • {prod_key.capitalize()} - {prod_value}')
    #print(prod_key, prod_value)

