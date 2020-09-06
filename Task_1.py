def del_arg(x, y):
    z = x/y
    print('Результат деления =', z)

x = int(input('Введите делимое '))
y = int(input('Введите делитель '))
if y == 0:
    y = int(input('Делить на ноль нельзя! Введите делитель, неравный нулю '))
del_arg(x, y)