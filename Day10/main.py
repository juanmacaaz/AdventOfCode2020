import multiprocessing

data = open('input.txt')
data = data.read().split('\n')
data = [int(x) for x in data]
data.append(0)
data = sorted(data)
data.append(data[-1]+3)

diference = dict()
diference[1] = 0
diference[3] = 0

for i in range(len(data)-1):
    diff = data[i+1] - data[i]
    diference[diff] += 1 

print(diference[1]*diference[3])

print(diference)

groups = dict()

for i in range(len(data)-1):
    for x in range(1, 4):
        if (i+x) >= len(data): continue
        diff = data[i+x] - data[i]
        if diff <= 3:
            if data[i] not in groups.keys():
                groups[data[i]] = []
            groups[data[i]].append((data[i+x], data[i]))

combinations = 1

def claveEnPair(c, pairs):
    for x in pairs:
        if c == x[0]:
            return True
    return False

total = 0

dp = {}
def calcRec(index):
    s = 0
    if index in dp:
        return dp[index]
    if index not in groups.keys():
        return 1
    for x in groups[index]:
        s += calcRec(x[0])
    dp[index] = s
    return s

print(calcRec(0))

