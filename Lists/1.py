list = []
while True:
    Game=input('введите название игры -')
    if Game != '0':
        if Game not in list:
            list.append(Game)
            list.sort()
            print('игра добавлена')
        else:
            print('игра уже существует ')
    else:
        print('Спасибо за игру')
    break
