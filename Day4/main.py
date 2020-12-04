import re
data = open('input.txt')

def validaCampos(a,b):
    for x in b:
        if x not in a: return False
    return True

def validaValores(campos, valores):
    for i in range(len(campos)):
        if campos[i] == 'byr':
            if int(valores[i]) < 1920 or int(valores[i]) > 2002: return False
        if campos[i] == 'iyr':
            if int(valores[i]) < 2010 or int(valores[i]) > 2020: return False
        if campos[i] == 'eyr':
            if int(valores[i]) < 2020 or int(valores[i]) > 2030: return False
        if campos[i] == 'hgt':
            if not(valores[i][-2:] == 'cm' or valores[i][-2:] == 'in'): return False
            if valores[i][-2:] == 'cm':
                if len(valores[i]) != 5: return False
                if int(valores[i][:3]) < 150 or int(valores[i][:3]) > 193: return False
            elif valores[i][-2:] == 'in':
                if len(valores[i]) != 4: return False
                if int(valores[i][:2]) < 59 or int(valores[i][:2]) > 76: return False
        if campos[i] == 'hcl':
            if len(valores[i]) != 7: return False
            if not(re.match(r"#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]", valores[i])): return False
        if campos[i] == 'ecl':
            if valores[i] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False
        if campos[i] == 'pid':
            if len(valores[i]) != 9: return False
            if not(re.match(r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", valores[i])): return False
    return True

validos = 0

camposNecesarios = sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid'])

campos = []
valores = []

for linea in data.read().split('\n'):
    if linea == "":
        if validaCampos(sorted(campos), camposNecesarios):
            if validaValores(campos,valores):
                validos += 1
        campos = []
        valores = []
    else:
        for campo in linea.split(' '):
            subampo = campo.split(':')[0]
            valor = campo.split(':')[1]
            campos.append(subampo)
            valores.append(valor)

print('Campos validos: ', validos)