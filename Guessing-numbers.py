import random

counter = 0

print('Привет как тебя зовут ')
name = input()

for i in range(1):
    num = random.randint(1, 100)

def guessing_numbers():
    while num > 0:
        a = int(input(name +', введите число от 1 до 100: \n' ))
        if a == num:
            print('Вы угадали, поздравляем!')
            break
        if a > num:
            print('Слишком много, попробуйте еще раз')
        if a < num:
            print('Слишком мало, попробуйте еще раз')
            continue

#print(num)
print(guessing_numbers())



