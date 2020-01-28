class Road:
    # атрибуты класса
    # методы класса
    def __init__(self, length, width):
        self.length = length
        self.width = width

        print("Масса  при толщине в 5 см будет = ", int(self.length*self.width*25*5/1000),"(тонн)")

length = int(input("Длинна полотна в метрах = "))
width = int(input("Ширина полотна в метрах = "))
road = Road(length, width)

