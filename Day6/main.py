data = open('input.txt')

info = data.read().split('\n\n')

total = 0
for x in info:
    total += len(set(x.replace('\n', '')))
print(total)


total = 0
for x in info:
    print(x.split('\n'))
    nPersonas = len(x.split('\n'))
    for y in set(x.replace('\n', '')):
        if x.count(y) == nPersonas:
            total += 1

print(total)
    
