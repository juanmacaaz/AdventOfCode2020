data = open('input.txt')

conditions = [(1,1),
              (3,1),
              (5,1),
              (7,1),
              (1,2)]

mapa  = []

hSize = 0
vSize = 0

vPos = 0
hPos = 0

arboles = 0
nada    = 0

for line in data.read().split('\n')[:-1]:
    print(len(line))
    hSize = len(line)
    mapa.append(line)
    vSize += 1

print('Ancho de: ', hSize, 'Altura de: ', vSize)

arbolesTotales = 1
for condition in conditions:
    vPos = 0
    hPos = 0
    arboles = 0
    while vPos != vSize-1:
        vPos += condition[1]
        hPos = (hPos+condition[0])%hSize
        if mapa[vPos][hPos] == '#':
            arboles += 1
    arbolesTotales *= arboles

print('Arboles: ', arbolesTotales)