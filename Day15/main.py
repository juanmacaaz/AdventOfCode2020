import sys

LIMIT = 30000000
string = '6,4,12,1,20,0,16'.split(',') # Poner el input aqui!
data = { int(x) : i+1 for i, x in enumerate(string[:-1]) }

a = int(string[-1])
i = len(string)


while True:
    aux = 0
    if a in data:
        aux = i - data[a]
    data[a] = i
    a = aux
    i += 1
    if i == LIMIT:
        break

print(a)