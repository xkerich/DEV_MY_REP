'''
Цикл в котором у пользователя спрашивают имя и с ним здороваются.
'''
while True:
    print('Здравствуйте. Как вас зовут?')
    name = input('Введите ваше имя: ')
    if name:
        print(f'Привет, {name}!')
    else:
        break