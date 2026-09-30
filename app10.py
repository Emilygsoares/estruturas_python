# Conjuntos

import os
os.system('cls')

conj = {
    'casa',
    "peteca",
    122,
    True,
    1999.90,
    (10, 'mola'),
  122,122,122,122,122,122,122,122,122, #duas vezes e ele  ignora as duplicatas quando usamos len()
}

print(conj) # O conjunto se altera em cada execução do código (conjunto)
#print(conj[1]) # conjuntos não são ordenandos #ERRO!
print(len(conj))
