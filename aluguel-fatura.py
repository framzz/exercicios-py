# aluguel e fatura de jonas já com o atraso 
aluguel = 6500.00
atrasoAluguel = 12

fatura = 7234.77
atrasoFatura = 6

# criação de função para calcular quanto jonas deve
def jurosJonas(a,aal,f,af):
    
    #aluguel
    principalAluguel = a
    diasAluguel = aal
    mora = 0.0625
    jurosSimples = 0.00025 * diasAluguel
    moraTaxa = principalAluguel * mora 
    jurosTaxa = principalAluguel * jurosSimples
    aluguelTaxa = moraTaxa + jurosTaxa
    print(f"O total de juros a ser pago é:{aluguelTaxa:.2f}")


    # fatura 
    principalFatura = f
    diasFatura = af  
    taxa = 0.0144  
    montanteFatura = principalFatura * pow((1 + taxa), diasFatura)
    jurosFatura = montanteFatura - principalFatura  
    print(f"O total de juros a ser pago é:{jurosFatura:.2f}")
    
    #juntando
    total = aluguelTaxa + jurosFatura + principalAluguel + principalFatura
    return total



print(f'O total que Jonas precisa pagar é de R${jurosJonas(aluguel, atrasoAluguel, fatura, atrasoFatura):.2f}')