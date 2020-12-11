import copy

data = open('input.txt')
data = data.read().split('\n')
data = [list(x) for x in data]

dataCpt = copy.deepcopy(data)

def up(data, x, y):
    for i in range(1, x+1):
        if data[x-i][y] != '.':
            return (data[x-i][y] == '#')
    return False

def down(data, x, y):
    for i in range(1, len(data)-x):
        if data[x+i][y] != '.':
            return (data[x+i][y] == '#')
    return False

def rigth(data, x, y):
    for i in range(1, (len(data[0])-y)):
        if data[x][y+i] != '.':
            return (data[x][y+i] == '#')
    return False

def left(data, x, y):
    for i in range(1, y+1):
        if data[x][y-i] != '.':
            return (data[x][y-i] == '#')
    return False

def downRight(data, x, y):
    for i in range(1, 500):
        if x+i >= len(data):    continue
        if y+i >= len(data[0]): continue
        if data[x+i][y+i] != '.':
            return (data[x+i][y+i] == '#') 
    return False

def downLeft(data, x, y):
    for i in range(1, 500):
        if x+i >= len(data): continue
        if y-i < 0: continue
        if data[x+i][y-i] != '.':
            return (data[x+i][y-i] == '#')
    return False

def upRigth(data, x, y):
    for i in range(1, 500):
        if x-i < 0: continue
        if y+i >= len(data[0]): continue
        if data[x-i][y+i] != '.':
            return (data[x-i][y+i] == '#')
    return False

def upLeft(data, x, y):
    for i in range(1, 500):
        if x-i < 0: continue
        if y-i < 0: continue
        if data[x-i][y-i] != '.':
            return (data[x-i][y-i] == '#')
    return False

def cambio2(x, y, data):
    c = 0
    if up(data, x, y):    c+=1
    if down(data, x, y):  c+=1
    if left(data, x, y):  c+=1
    if rigth(data, x, y): c+=1
    if downRight(data, x, y): c+=1
    if downLeft(data, x, y): c+=1
    if upRigth(data, x, y): c+=1
    if upLeft(data, x, y): c+=1
    return c

def cambio(x, y, data):
    c = 0
    for i in range(-1, 2):
        for z in range(-1, 2):
            n_x = x+i
            n_y = y+z
            if i == 0 and z == 0:               continue
            if n_x < 0 or n_x >= len(data):     continue
            if n_y < 0 or n_y >= len(data[0]):  continue
            if data[n_x][n_y] == '#':
                c += 1
    return c

for _ in range(200):
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == '.': continue
            if data[x][y] == '#':
                if cambio2(x, y, data) >= 5:
                    dataCpt[x][y] = 'L'
            if data[x][y] == 'L':
                if cambio2(x, y, data) == 0:
                    dataCpt[x][y] = '#'
    data = copy.deepcopy(dataCpt)

count = 0

for x in data:
    print(x)

for x in data:
    for i in x:
        if i == '#':
            count += 1

print(count)