data = [(x[0], int(x[1:])) for x in open('input.txt').read().split('\n')]

# Parte 1
# Grados: 90, 180, 270 

BRUJULA = {0: 'N', 90: 'E', 180: 'S' , 270: 'W'}

def mover(pos, direccion, distancia):
    if direccion == 'N':
        pos[1] -= distancia
    if direccion == 'S':
        pos[1] += distancia
    if direccion == 'E':
        pos[0] += distancia
    if direccion == 'W':
        pos[0] -= distancia

d = 90
pos = [0,0] # X, Y

for x in data:
    if x[0] == 'F':
        mover(pos, BRUJULA[d], x[1])
    elif x[0] == 'R':
        d = (d + x[1]) % 360
    elif x[0] == 'L':
        d -= x[1]
        if d < 0:
            d = (d + 360)%360
    else:
        mover(pos, x[0], x[1])

print(abs(pos[0])+abs(pos[1]))

# Parte 2

pos = [0,0] # X, Y
mira = [10,1]

def toBrujula(pos):
    brujula = {}
    if pos[0] < 0:
        brujula['W'] = abs(pos[0])
        brujula['E'] = 0
    else:
        brujula['E'] = pos[0]
        brujula['W'] = 0
    if pos[1] < 0:
        brujula['N'] = abs(pos[1])
        brujula['S'] = 0
    else:
        brujula['N'] = 0
        brujula['S'] = pos[1]
    return brujula

def toCordenates(brujula):
    pos = [0,0]
    if brujula['W'] == 0:
        pos[0] = brujula['E']
    else:
        pos[0] = -brujula['W']
    
    if brujula['N'] == 0:
        pos[1] = brujula['S']
    else:
        pos[1] = -brujula['N']
    return pos

def cambiarPosBrujula(brujula, a, b):
    aux = brujula[a]
    brujula[a] = brujula[b]
    brujula[b] = aux

def girar90gradosDerecha(pos):
    brujula = toBrujula(pos)
    cambiarPosBrujula(brujula, 'N', 'W')
    cambiarPosBrujula(brujula, 'N', 'S')
    cambiarPosBrujula(brujula, 'N', 'E')
    return toCordenates(brujula)

def girar90gradosIzquierda(pos):
    brujula = toBrujula(pos)
    cambiarPosBrujula(brujula, 'N', 'E')
    cambiarPosBrujula(brujula, 'N', 'S')
    cambiarPosBrujula(brujula, 'N', 'W')
    return toCordenates(brujula)

def cambiarMira(mira, direccion, distancia):
    if direccion == 'N':
        mira[1] += distancia
    if direccion == 'S':
        mira[1] -= distancia
    if direccion == 'E':
        mira[0] += distancia
    if direccion == 'W':
        mira[0] -= distancia

def moverBarco(pos, mira, distancia):
    pos[0] += mira[0] * distancia
    pos[1] += mira[1] * distancia

for x in data:
    if x[0] == 'F':
        moverBarco(pos, mira, x[1])
    elif x[0] == 'R':
        for _ in range(int(x[1]/90)):
            mira = girar90gradosDerecha(mira)
    elif x[0] == 'L':
        for _ in range(int(x[1]/90)):
            mira = girar90gradosIzquierda(mira)
    else:
        cambiarMira(mira, x[0], x[1])

print(abs(pos[0])+abs(pos[1]))