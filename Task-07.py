# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 4. Задание 7:
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
# значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться
# следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а
# в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24

# Создаю функцию, на основе которой будет создан генератор
def gen_fact(n):

    factorial = 1
    for i in range(1, n+1):
        yield i
        factorial *= i
        print(f'{i}! = {factorial}', end = '')


# Создаю генератор
fact = gen_fact(100)

# Прохожу в цикле по элементам, получаемым генератором
for el in fact:
    # Вот это место у меня вызвало наибольшее затруднение. Мы печатаем значение факториала из функции генератора
    # Что должно быть в этом месте?
    print('')

# Я не уверен, что до конца правильно понял задание, готов адекватно воспринять критику