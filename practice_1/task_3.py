# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""

# Ваш код
print("Эта программа рассчитывает индекс массы тела (body mass index – BMI) человека")

while True:
    try:
        print("Введите ниже свои вес (кг) и рост (см)")
        weight_input = str(input("Вес: "))
        height_input = str(input("Рост: "))

        weight = float(weight_input.replace(",", "."))
        height = float(height_input.replace(",", ".")) / 100

        if weight <= 0 or height <= 0:
            print("Проверьте корректность данных и введите их снова")
            continue
        else:
            bmi = round(weight / pow(height, 2), 1)
            print(f"Индекс массы тела (BMI) равен {bmi}")

    except Exception as e:
        print("Проверьте корректность данных и введите их снова")
        continue
