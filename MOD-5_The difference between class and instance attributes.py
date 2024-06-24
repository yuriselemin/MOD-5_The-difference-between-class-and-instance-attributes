
# Домашнее задание по уроку "Различие атрибутов класса и экземпляра"



'''
Этот код определяет класс Building и создает 40 экземпляров этого класса. Класс Building имеет атрибут total, который инициализируется значением 0 в конструкторе класса __init__(). 
При создании каждого нового экземпляра класса Building, значение атрибута total увеличивается на 1. Это позволяет отслеживать количество созданных экземпляров класса.
Вне класса определён цикл for, который создает 40 экземпляров класса Building и выводит информацию о каждом созданном объекте.
'''


class Building:  # Определение класса Building
    def __init__(self):  # Конструктор класса, который вызывается при создании нового экземпляра
        self.total = 0  # Атрибут total инициализируется значением 0
        self.total += 1  # Значение total увеличивается на 1 при создании каждого экземпляра

# Цикл for, который создает 40 экземпляров класса Building
for i in range(1, 41):
    building = Building()  # Создание нового экземпляра класса Building

    print(f"Объект {building.total} класса Building создан.")  # Вывод информации о созданном объекте

