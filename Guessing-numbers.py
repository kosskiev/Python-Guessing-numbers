import random

print('Добро пожаловать в игру')
print('Как тебя зовут ')
name = input()
def is_valid(n):
    if 1 <= int(n) <= 100:
        return True
    return False
counter = 1  # подсчитывать количество попыток
random_number = random.randint(1, 100) # получить случайное число от 0 до 100
while True:
    answer = int(input(name +', введите число от 1 до 100: \n' ))
    if is_valid(answer) == False:
        print('Введите число согласно условию')
        counter += 1
        continue
    if answer == random_number:
        print('Вы угадали, поздравляем!')
        print(f'Количество ваших попыток {counter}')
        break
    if 101 > answer > random_number:
        print('Слишком много, попробуйте еще раз')
        counter += 1
    if 0< answer < random_number:
        print('Слишком мало, попробуйте еще раз')
        counter +=1
    continue



