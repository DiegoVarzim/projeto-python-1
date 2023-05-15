print(' \n Seja muito bem-vindo ao quiz do Diego Varzim!')
answer_user = input(' \n Quer começar? (S/N)')

if answer_user != 'S':
    quit()

score = 0

print(' \n Começando...')

print(' \n Questão 1: Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n')
answer_1 = input('Resposta: ')

if answer_1 == 'A':
    print('Correta! Rockstar Games!!')
    score = score + 1
else:
    print('Incorreta!')

print(' \n Questão 2: Qual o nome do protagonista do game Final Fantasy XVI (FFXVI)? \n \n (A) Cloud Strife \n (B) Squall Leonhart \n (C) Zidane Tribal \n (D) Clive Rosfield \n')
answer_2 = input('Resposta: ')

if answer_2 == 'D':
    print('Correta! Clive Rosfield!!')
    score = score + 1
else:
    print('Incorreta!')

print(' \n Questão 3: Em que ano foi lançado o jogo Demon`s Souls Remake para PS5? \n \n (A) 2019 \n (B) 2020 \n (C) 2021 \n (D) 2022 \n')
answer_3 = input('Resposta: ')

if answer_3 == 'B':
    print('Correta! 2020!!')
    score = score + 1
else: 
    print('Incorreta!')

print(f' \n Quiz acabou... Pontuação: {score}/3 \n')

