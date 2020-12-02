PATH = 'input.txt'

count = 0
data = open(PATH)

def countLeter(password, leter):
    return password.count(leter)

def minMaxLeter(condicion):
    return int(condicion.split("-")[0]), int(condicion.split(" ")[0].split("-")[1]), condicion[-1]

for line in data:
    password = line.split(":")[1][1:-1]
    minimo, maximo, leter = minMaxLeter(line.split(":")[0])
    if (password[minimo-1] == leter) ^ (password[maximo-1] == leter): # Case 1: countLeter(password, leter) in range(minimo, maximo+1)
        count += 1

print(count)