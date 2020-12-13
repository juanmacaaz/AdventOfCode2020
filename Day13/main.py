import operator

data = open('input.txt').read().split('\n')

# Parte 1

INIT = int(data[0])
IDS = [int(i) for i in data[1].split(',') if i != 'x']
IDS = {x:0 for x in IDS}

for key in IDS.keys():
    index = 0
    encontrado = False
    while not encontrado:
        if index >= INIT:
            IDS[key] = (index - INIT)
            encontrado = True
        index += key

print([IDS[x]*x for x in IDS.keys() if IDS[x] == min(IDS.values())][0])


# Parte 2 (Problema del resto chino con fuerza bruta)

data2 = data[1].replace('x', '0').split(',')
data = data[1].split(',')

bus = {int(x):i for i, x in enumerate(data) if x.isdigit()}

value = max(data2)
index = data2.index(value)
value = int(value)

print(index,value)

i = 600691418731505- 30000

def mp(i):
    cumple = True
    for x in bus.keys():
        if ((i)+bus[x])%x != 0: cumple = False
    if cumple:
        print(i)
        exit(0)

while True:
    mp(i)
    i+=1