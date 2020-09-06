def sum_el():
    el_sum = 0
    while True:
        numbers = input('Введите несколько чисел через пробел или + для завершения программы ').split()
        for i in numbers:
            if i != '+':
                el_sum += int(i)
            else:
                print(f'Сумма введенных чисел составляет: {el_sum}. Подсчет окончен')
                return
        print(f'Сумма введенных чисел составляет: {el_sum}')

sum_el()