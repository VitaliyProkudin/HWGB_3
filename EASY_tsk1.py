# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


import argparse

parser = argparse.ArgumentParser(description='Process some integer for number cyrcle print Text.')
parser.add_argument('Input_float', type=float  , help='Float')
parser.add_argument('Input_int_round', type=int, help='Number of character')
round_a = int(parser.parse_args().Input_float * (10**parser.parse_args().Input_int_round) + 0.41)
End = round_a / 10**parser.parse_args().Input_int_round
print(End)




