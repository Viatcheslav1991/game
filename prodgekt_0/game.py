"""Угадай число"""
import numpy as np
number=np.random.randint(1,101)

count=0

while True:
    count+=1
    predict_number=int(input("Введите число"))
    if predict_number<number:
        print("Искомое число больше")
    elif predict_number>number:
        print("Искомое число меньше")
    else:
        print(f"Победа, вы справились за {count} попыток")
        break

    