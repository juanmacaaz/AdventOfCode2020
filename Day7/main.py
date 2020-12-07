data = open('input.txt')

bags = dict()

for line in data.read().split('\n'):
    insideBags = []
    bagName = line.split('bags')[0].replace(' ', '')
    for bag in line[:-1].split('contain')[1].split(','):
        bagAux = bag[1:]
        if bagAux[0] == 'n':
            quantity = 0
        else:
            quantity = int(bagAux[0])
        insideBags.append((quantity, bagAux[2:].split(' ')[0]+bagAux[2:].split(' ')[1]))
    bags[bagName] = insideBags

# A

temp = []
def insideBag(key):
    aux = False
    if key != 'other':
        for bag in bags[key]:
            insideBag(bag[1])
            if bag[1] == 'shinygold':
                aux = True
    temp.append(aux)

count = 0

for key in bags.keys():
    temp = []
    insideBag(key)
    if any(temp):
        count +=1

print(count)

# A

b = 0

def insideBag2(key, count):
    global b
    if key == 'other': return 1
    for bag in bags[key]:
        for _ in range(bag[0]):
            insideBag2(bag[1], count)
            b += 1

insideBag2('shinygold', count)

print(b)