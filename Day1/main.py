'''
--- Día 1: Informe de reparación ---
Después de salvar la Navidad cinco años seguidos , ha decidido tomarse unas vacaciones en un bonito resort en una isla tropical. Seguro que la Navidad seguirá sin ti.
La isla tropical tiene su propia moneda y solo se paga en efectivo. Las monedas de oro que se utilizan allí tienen una pequeña imagen de una estrella de mar;
los lugareños simplemente los llaman estrellas . Ninguno de los intercambios de divisas parece haber oído hablar de ellos, pero de alguna manera,
debera encontrar cincuenta de estas monedas para cuando llegue para poder pagar el depósito en su habitación.
Para guardar sus vacaciones, debe obtener las cincuenta estrellas antes del 25 de diciembre.
Recoge estrellas resolviendo acertijos. Dos rompecabezas estarán disponibles cada día en el calendario de Adviento; el segundo rompecabezas se desbloquea al completar el primero. Cada rompecabezas otorga una estrella . ¡Buena suerte!
Antes de que te vayas, los Elfos en contabilidad solo necesitan que arregles tu informe de gastos (tu entrada de rompecabezas); aparentemente, algo no cuadra.
Específicamente, necesitan que encuentres las dos entradas que suman2020 y luego multipliques esos dos números.
Por ejemplo, suponga que su informe de gastos contiene lo siguiente:

1721
979
366
299
675
1456

En esta lista, las dos entradas que suman 2020son 1721y 299. Multiplicarlos juntos produce 1721 * 299 = 514579, por lo que la respuesta correcta es 514579.
Por supuesto, su informe de gastos es mucho más amplio. Encuentre las dos entradas que sumen 2020; ¿Qué obtienes si los multiplicas?
'''

dataFile = open('data.txt')
dataList = []

for line in dataFile.readlines():
    dataList.append(int(line))

size = len(dataList)
cartesian = []

for i in range(size):
    for x in range(i, size):
        if dataList[i] + dataList[x] == 2020:
                print('A: ',dataList[i]*dataList[x])
        for y in range(x, size):
            if dataList[i] + dataList[x] + dataList[y] == 2020:
                print('B: ',dataList[i]*dataList[x]*dataList[y])

