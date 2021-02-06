v = float(input('Digite a velocidade do carro: '))
if v > 80:
    overpay = 7 * (v - 80)
    print(f'Multado! Sua multa é de R${overpay}')
else: 
    print('Não foi multado.')
    