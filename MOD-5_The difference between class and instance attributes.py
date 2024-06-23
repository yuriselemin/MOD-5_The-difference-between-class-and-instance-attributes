
# Домашнее задание по уроку "Различие атрибутов класса и экземпляра"



class Building:
    def __init__(self):
        self.total = 0
        self.total += 1

for i in range(1,41):
    building = Building()

    print(f"Объект {building.total} класса Building создан.")





