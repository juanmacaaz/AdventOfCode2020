data = open('input.txt')

F_MAX = 128
C_MAX = 8

VALOR = 0

def calcularValor(val):
    RS = F_MAX
    RI = 0
    CS = C_MAX
    CI = 0

    for x in val[0:8]:
        if x == 'B':
            RI = RI+((RS-RI)/2)
        if x == 'F':
            RS = RS-((RS-RI)/2)

    for x in val[7:]:
        if x == 'L':
            CS = CS-((CS-CI)/2)
        if x == 'R':
            CI = CI+((CS-CI)/2)
    return int(RI), int(CI)

asientos = []

for x in data.read().split("\n"):
    fila, columna = calcularValor(x)
    identificador = fila*C_MAX+columna
    asientos.append(identificador)
    if identificador > VALOR:
        VALOR = identificador

print(VALOR)

for x in sorted(asientos):
    if x+1 not in asientos:
        print(x+1)
        exit()


