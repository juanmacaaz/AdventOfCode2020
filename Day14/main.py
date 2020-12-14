import copy as cp

data = open('input.txt').read().split('\n')

BITS_TOTALES = 36

mask = ''

# Parte 1

def toBit(number):
    return list(bin(int(number)).split('b')[1])

def emask(mask, number):
    numberBit = ((BITS_TOTALES-len(toBit(number)))*list('0')+toBit(number))[::-1]
    mask2 = mask[::-1]
    for i, _ in enumerate(numberBit):
        if mask2[i] == '0':
            numberBit[i] = '0'
        if mask2[i] == '1':
            numberBit[i] = '1'
    return ''.join((numberBit[::-1]))

total = 0

MEM = {}

for line in data:
    action, val = line.replace(' ', '').split('=')
    if action == 'mask':
        mask = val
    else:
        MEM[action.split('[')[1].split(']')[0]] = int(emask(mask,val), 2)

print(sum(MEM.values()))

# Parte 2

def emask2(mask, number):
    numberBit = ((BITS_TOTALES-len(toBit(number)))*list('0')+toBit(number))[::-1]
    mask2 = mask[::-1]
    for i in range(len(numberBit)):
        if mask2[i] == '0': continue
        if mask2[i] == '1':
            numberBit[i] = '1'
        elif mask2[i] == 'X':
            numberBit[i] = 'X'
    return numberBit

alter = []

def generate(index, value):
    if index < len(value):
        if value[index] == 'X':
            copy = cp.deepcopy(value)
            copy[index] = '1'
            alter.append(copy)
            generate(index+1, copy)
            copy = cp.deepcopy(value)
            copy[index] = '0'
            alter.append(copy)
            generate(index+1, copy)
        else:
            generate(index+1, value)

MEM = {}

for line in data:
    action, val = line.replace(' ', '').split('=')
    if action == 'mask':
        mask = val
    else:
        mascara = emask2(mask,action.split('[')[1].split(']')[0])
        alter = []
        generate(0, mascara)
        alter = [''.join(x[::-1]) for x in alter]
        alter = [int(x, 2) for x in alter if 'X' not in x]
        for x in alter:
            MEM[x] = int(val)

print(sum(MEM.values()))