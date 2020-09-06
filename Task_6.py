def int_func(user_str):
    text = user_str.title()
    return text

user_str = input('Введите слово либо строку, разделенную пробелами, из маленьких латинских букв ')
print(int_func(user_str))

