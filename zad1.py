import time
class TrafficLight:
    # атрибуты класса
    # методы класса
    def __init__(self, __color):
        self.__color = __color

        print({self.__color})


color = ["Красный", "Желтый", "Зеленый", "Желтый"]
temp_tr = [7, 2, 5, 2]
for _ in temp_tr:
    a = 0
    for c in color:
        trafficLight_1 = TrafficLight(c)
        time.sleep(temp_tr[a])
        a += 1
