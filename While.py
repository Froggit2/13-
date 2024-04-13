while 1 > 0 or True:
    number = int(input('Введи число: '))
    if number % 2 == 0:
        print(number, 'Четное число')
        if number % 5 == 0:
            print('Конец')
            break
    if number % 2 != 0:
        print(number, 'НЕ четное')