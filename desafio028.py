import random
num = random.randint(0, 5)
usernum = int(input('Em qual número estou pensando? '))
if num == usernum: 
    print('Parabéns! Você acertou.')
else: 
    print(f'Errado! Eu pensei no número {num}.')