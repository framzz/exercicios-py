def transforma_cpf(cpf: str) -> list:
   return [int(i) for i in cpf]

def primeira_checagem(num_cpf: list) -> float:
  x =  (num_cpf[0]*10 + num_cpf[1]*9 + num_cpf[2]*8 + num_cpf[3]*7\
        + num_cpf[4]*6 + num_cpf[5]*5 + num_cpf[6]*4 + num_cpf[7]*3\
        + num_cpf[8]*2)
   
  return x * 10 % 11

def segunda_checagem(primeiro_check: float, num_cpf: list, cpf: str) -> float:
    if primeiro_check == num_cpf[9]:
      x =  (num_cpf[0]*11 + num_cpf[1]*10 + num_cpf[2]*9 + num_cpf[3]*8\
        + num_cpf[4]*7 + num_cpf[5]*6 + num_cpf[6]*5 + num_cpf[7]*4\
        + num_cpf[8]*3 + num_cpf[9]*2)
    else:
      return f'O CPF de número {cpf} não é válido'
    return x * 10 % 11

def validacao_cpf(segundo_check: float, num_cpf: list, cpf: str) -> str:
    if segundo_check == num_cpf[10]:
      return f'O CPF de número {cpf} é válido'
    else:
      return f'O CPF de número {cpf} não é válido'

def main():
  cpf = input('Digite o CPF: ')
  cpf_list = transforma_cpf(cpf)

  check = segunda_checagem(primeira_checagem(cpf_list), cpf_list)
  return validacao_cpf(check, cpf_list, cpf)


main()
