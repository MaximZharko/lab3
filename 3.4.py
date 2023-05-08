import random

counter = 0
counter_mistakes = 0

while counter_mistakes != 3:
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    print(str(num1) + " + " + str(num2) + " = ")
    num = int(input())
    if num == num1 + num2:
        print("Правильно!")
        counter += 1
    else:
        print("Ответ неверный")
        counter_mistakes += 1

print("Игра окончена. Правильных ответов: " + str(counter_mistakes))