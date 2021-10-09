# criação de funções
# indicação de remedios
# lista de remedios dada em aula 
def remedioIndicacao(dic):
    # usados os tres remedios na gratuidade
    hipertensao = 0
    asma = 0
    diabetes = 0
    lista = dic.items()
    for i in lista:
        if i[1] == 'hipertensão':
            hipertensao += 1
        elif i[1] == 'asma':
            asma += 1
        elif i[1] == 'diabetes':
            diabetes += 1
        
    return (hipertensao, asma, diabetes)

#remedios com C
def remediosComC(dic):
    c = 0
    for i in dic:
        if i[0] == 'C':
            c += 1
        else:
            pass

    return c

#gratuito ou copagamento
def remediosValor(dic):
    lista = dic.items()
    gratuito = 0
    copago = 0
    for i in lista:
        if i[1] == 'gratuidade':
            gratuito += 1
        elif i[1] == 'copagamento':
            copago += 1
    return (gratuito+1, copago)
    
dicRemediosIndicacao = { 'ATENOLOL': 'hipertensão', 'CAPTOPRIL': 'hipertensão', 'CLORIDATO DE PROPRANOLOL': 'hipertensão', 'HIDROCLOROTIAZIDA': 'hipertensão', 'LOSARTANA POTÁSSICA': 'hipertensão',
'MELEATO DE ENALAPRIL': 'hipertensão', 'GLIBENCLAMIDA': 'diabetes', 'CLORIDRATO DE METFORMINA': 'diabetes', 'CLORIDATO DE METFORMINA - AÇÃO PROLONGADA': 'diabetes', 'CLORIDRATO DE METFORMINA - 850MG': 'diabetes',
'INSULINA HUMANA': 'diabetes', 'INSULINA HUMANA REGULAR': 'diabetes', 'SULFATO DE SALBUTAMOL 5MG': 'asma', 'SULFATO DE SALBUTAMOL 100MCG': 'asma', 'DIPROPIONATO DE BECLOMETASONA 50MCG': 'asma', 'DIPROPIONATO DE BECLOMETASONA 200MCG/DOSE': 'asma',
'DIPROPIONATO DE BECLOMETASONA 200MCG/CÁPSULA': 'asma', 'DIPROPIONATO DE BECLOMETASONA 250MCG': 'asma', 'BROMETO DE IPRATRÓPIO 0,25MG/ML': 'asma', 'BROMETO DE IPRATRÓPIO 0,02MG/DOSE': 'asma', 'ACETATO DE MEDROXIPROGESTERONA': 'anticoncepção',
'ETINILESTRADIOL 0,03MG + LEVONORGESTREL 0,15MG': 'anticoncepção', 'NORETISTERONA': 'anticoncepção', 'VALERATO DE ESTRADIOL 5MG + ENANTATO DE NORETISTERONA 50MG': 'anticoncepção', 'SINVASTATINA 10MG': 'dislipidemia', 'SINVASTATINA 20MG': 'dislipidemia',
'SINVASTATINA 40MG': 'dislipidemia', 'BUDESONIDA 32MCG': 'rinite', 'BUDESONIDA 50MCG': 'rinite', 'DIPROPIONATO DE BECLOMETASONA 50MCG': 'rinite', 'CARBIDOPA 25MG + LEVODOPA 250MG': 'parkinson', 'CLORIDRATO DE BENSERAZIDA 25MG + LEVODOPA 100MG': 'parkinson',
'ALENDRONATO DE SÓDIO 70MG': 'osteoporose', 'MALEATO DE TIMOLOL 2,5MG': 'glaucoma', 'MALEATO DE TIMOLOL 5MG': 'glaucoma'}

resultado = remedioIndicacao(dicRemediosIndicacao)
print(resultado)
# Para que doença a maior quantidade de remédios na gratuidade é indicada? ASMA

dicRemediosValor = { 
'ATENOLOL': 'gratuidade', 
'CAPTOPRIL': 'gratuidade', 
'CLORIDATO DE PROPRANOLOL': 'gratuidade', 
'HIDROCLOROTIAZIDA': 'gratuidade', 
'LOSARTANA POTÁSSICA': 'gratuidade',
'MELEATO DE ENALAPRIL': 'gratuidade', 
'GLIBENCLAMIDA': 'gratuidade', 
'CLORIDRATO DE METFORMINA': 'gratuidade', 
'CLORIDATO DE METFORMINA AÇÃO PROLONGADA': 'gratuidade', 
'CLORIDRATO DE METFORMINA 850MG': 'gratuidade',
'INSULINA HUMANA': 'gratuidade', 
'INSULINA HUMANA REGULAR': 'gratuidade', 
'SULFATO DE SALBUTAMOL 5MG': 'gratuidade', 
'SULFATO DE SALBUTAMOL 100MCG': 'gratuidade', 
'DIPROPIONATO DE BECLOMETASONA 50MCG': 'gratuidade', 
'DIPROPIONATO DE BECLOMETASONA 200MCG/DOSE': 'gratuidade',
'DIPROPIONATO DE BECLOMETASONA 200MCG/CÁPSULA': 'gratuidade', 
'DIPROPIONATO DE BECLOMETASONA 250MCG': 'gratuidade', 
'BROMETO DE IPRATRÓPIO 0,25MG/ML': 'gratuidade', 
'BROMETO DE IPRATRÓPIO 0,02MG/DOSE': 'gratuidade',

'ACETATO DE MEDROXIPROGESTERONA': 'copagamento',
'ETINILESTRADIOL 0,03MG + LEVONORGESTREL 0,15MG': 'copagamento', 
'NORETISTERONA': 'copagamento', 
'VALERATO DE ESTRADIOL 5MG + ENANTATO DE NORETISTERONA 50MG': 'copagamento', 
'SINVASTATINA 10MG': 'copagamento', 
'SINVASTATINA 20MG': 'copagamento',
'SINVASTATINA 40MG': 'copagamento', 
'BUDESONIDA 32MCG': 'copagamento', 
'BUDESONIDA 50MCG': 'copagamento', 
'DIPROPIONATO DE BECLOMETASONA 50MCG': 'copagamento', 
'CARBIDOPA 25MG + LEVODOPA 250MG': 'copagamento', 
'CLORIDRATO DE BENSERAZIDA 25MG + LEVODOPA 100MG': 'copagamento',
'ALENDRONATO DE SÓDIO 70MG': 'copagamento', 
'MALEATO DE TIMOLOL 2,5MG': 'copagamento', 
'MALEATO DE TIMOLOL 5MG': 'copagamento'}

resultado = remediosComC(dicRemediosValor)
print(resultado)

# Quantos remédios têm a letra C como inicial de seu nome? 7

resultado = remediosValor(dicRemediosValor)
print(resultado)
# Qual é a quantidade de remédios nas classes gratuidade e copagamento? 20, 15