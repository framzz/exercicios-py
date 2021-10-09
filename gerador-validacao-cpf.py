print('EXERCICIO 3')
# gerando cpfs
import random 
def random_cpf(n):
    random.seed(38)
    cpf = []    
    for _ in range(n):              
        n = random.randrange(10000000000,99999999999)
        cpf.append(n)
    return cpf

cpf = random_cpf(20) 

# soma dos numeros dos cpfs
def somaCPF(n):
    soma = 0
    while (n > 0):
        restante = n % 10
        n = (n - restante)/10
        soma = soma + restante
    return soma

# validadando cpf
digitosCPF = (11, 22, 33, 44, 55, 66, 77, 88, 99)
cpfValido = []
print('VALIDANDO CPFS................')
for i in cpf:
    print(somaCPF(i))
    if somaCPF(i) not in digitosCPF:
        print('cpf não é valido')
    else:
        print('cpf válido')
        cpfValido.append(i)
print(cpfValido)
print(f'Existem {len(cpfValido)} cpfs válidos cadastrados')

#sabendo quantos cpfs são de SP
lista = []
for i in cpfValido:
    i = str(i)
    i = i[8]
    lista.append(i)
sp = 0
for i in lista:
    if i == '8':
        sp += 1

print(f'Sendo {sp} cpfs de São Paulo')