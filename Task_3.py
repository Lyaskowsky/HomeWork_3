
def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    print(sum(z))

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))

my_func(a, b, c)
