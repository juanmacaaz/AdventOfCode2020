from itertools import permutations  

LENGHT = 1000
PREAMBLE = 25

data = open('input.txt')
data = data.read().split('\n')

lista = []

for i in range(PREAMBLE,LENGHT-1):
    sums = [int(x[0])+int(x[1]) for x in list(permutations(data[i-PREAMBLE:i], 2))]
    if int(data[i]) not in sums:
        lista.append(data[i])

res = int(lista[0])
print(res)

data = list(map(int, data))

for i in range(LENGHT):
    for x in range(LENGHT):
        if i > x : continue
        if sum(data[i:x]) == res:
            print(max(data[i:x]) + min(data[i:x]))
            exit()