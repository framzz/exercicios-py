######## EXERCICIO 1 ---- RODOVIAS QUE PASSAM PELA PARAIBA #########
rodoviasPb = ['BR-101', 'BR-104', 'BR-110', 'BR-116',
'BR-361', 'BR-405', 'BR-408', 'BR-412', 'BR-426', 'BR-427',
'BR-434', 'BR-230']

print('EXERCICIO 1')
#transformando nomes em numeros apenas
rodoviasNum = []
for i in rodoviasPb:
    i = i[3:]
    i = int(i)
    rodoviasNum.append(i)

# LONGITUDINAIS
long = []
for i in rodoviasNum:
    if i >= 100 and i <= 199:
        long.append(i)
print(f'A quantidade de rodovias longitudinais na Paraíba é de: {len(long)}')

# TRANSVERSAIS
trans = []
for i in rodoviasNum:
    if i >= 200 and i <= 299:
        trans.append(i)
print(f'A quantidade de rodovias transversais na Paraíba é de: {len(trans)}')

# DIAGONAIS
dia = []
for i in rodoviasNum:
    if i >= 300 and i <= 399:
        dia.append(i)
print(f'A quantidade de rodovias diagonais na Paraíba é de: {len(dia)}')

# LIGAÇÃO
liga = []
for i in rodoviasNum:
    if i >= 400 and i <= 499:
        liga.append(i)
print(f'A quantidade de rodovias de ligação na Paraíba é de: {len(liga)}')
