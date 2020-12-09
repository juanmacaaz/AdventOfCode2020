import time
import copy

ROM = open('input.txt')

RAM = []
pc = 0
ac = 0

for line in ROM.read().split('\n'):
    ins = line.split(' ')[0]
    val = line.split(' ')[1]
    RAM.append([ins,int(val)])

def nop(val):
    pass

def jmp(val):
    global pc
    pc += (val-1)

def acc(val):
    global ac
    ac += val

inst = dict()
inst['nop'] = nop
inst['jmp'] = jmp
inst['acc'] = acc

def decode(ins, val):
    inst[ins](val)

for i in range(len(RAM)):
    ac = 0
    pc = 0
    RAMCopy = copy.deepcopy(RAM)
    finish = False

    if RAM[i][0] == 'jmp':
        RAMCopy[i][0] = RAMCopy[i][0].replace('jmp', 'nop')
    elif RAM[i][0] == 'nop':
        RAMCopy[i][0] = RAMCopy[i][0].replace('nop', 'jmp')

    repited = []
    while not finish:
        if pc in repited:
            finish = True
        repited.append(pc)
        decode(RAMCopy[pc][0],RAMCopy[pc][1])
        pc += 1
        if pc == len(RAM):
            print(ac)
            exit()