import os

os.system("cls")

fruits = ('maçã', 'pera', 'uva', 'morango', 'kiwi', 'pitanga',)
meats = ('Acém',) 
#eats = ('Acém' , 'Músculo' , 'Fígado' , 'Moela')

print('Minhas frutas favoritas:\n')

for fruit in fruits:
    print(f' • {fruit};')

for meat in meats:
    print(f'{meat} está cozinhando!')
    print('Vê se não deixa queimar!\n')    


print('\nAcabou')
