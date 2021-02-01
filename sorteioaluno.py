import random
aluno0 = str(input('Primeiro aluno:'))
aluno1 = str(input('Segundo aluno:'))
aluno2= str(input('Terceiro aluno:'))
alunos = [aluno0, aluno1, aluno2]
print(f'O aluno sorteado foi {random.choice(alunos)}')
