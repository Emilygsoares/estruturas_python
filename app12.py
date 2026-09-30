import os
os.system('cls')

'''pessoas = (
    { 'nome': 'Maria', 'idade': 45, 'conceito': 'A' },
    { 'idade': 54, 'nome': 'Joca',  'conceito': 'I'},
    { 'nome': 'Mariana', 'idade': 27, 'conceito': 'A'}
)'''

pessoas = {
    'p1': { 'nome': 'Maria', 'idade': 45, 'conceito': 'A' },
    'p2': { 'idade': 54, 'nome': 'Joca',  'conceito': 'I'},
    'p3': { 'nome': 'Mariana', 'idade': 27, 'conceito': 'A'}
}

contador = 1

for pessoa in pessoas:
    print(
        f'''
{contador}) {pessoa['nome']}:
\t • Idade: {pessoa['idade']}
\t • Conceito: {pessoa['conceito']}
        ''' 
    )
    contador = contador + 1
