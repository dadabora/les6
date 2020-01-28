class Car:
    def __init__(self,  speed, color, name, is_police='гражданское авто'):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police


        print(f'Скрорость {self.speed} цвет {self.color} марка {self.name}, {self.is_police} ')

    def go(self):
        print(f'{self.name}  Машина поехала')

    def stop(self):
        print(f'{self.name} машина остановилась')

    def turn(self, direction):
        print(f'{self.name} машина повернула {"направо" if direction == 1 else "налево"}')

    def speed_bust(self):
        return f'{self.name} скорость {self.speed}'

class TownCar(Car):
    def speed_bust(self):
        return f'{self.name} движущаяся со скоростью {self.speed} ' \
               f'{("первысила скорость" if self.speed > 60 else "двигалась с нормальной скоростью")} '

class WorkCar(Car):
    def speed_bust(self):
        return f'{self.name} движущаяся со скоростью {self.speed} ' \
               f'{("первысила скорость" if self.speed > 40 else "двигалась с нормальной скоростью")} '

class SportCar(Car):
    def speed_bust(self):
        return f'{self.name} движущаяся со скоростью {self.speed} ' \
               f'{("Полицейские удивлись почему это у спортивной машины нет ограничения скорости и погнались за ней" if self.speed > 90 else "двигалась с нормальной скоростью")} '

class PoliceCar(Car):
    def __init__(self,  speed, color, name, is_police='ей законы не писаны является полицейской машиной'):
        super(). __init__(speed, color, name, is_police)

police_car = PoliceCar(200, 'Красный', 'Бобик')
police_car.go()
print(police_car.speed_bust())
police_car.turn(1)
police_car.turn(0)
police_car.stop()
print(' ')

work_car = WorkCar(39, 'Серебристый', 'Газель')
work_car.go()
print(work_car.speed_bust())
work_car.turn(1)
work_car.turn(0)
work_car.stop()
print(' ')

work_car = WorkCar(90, 'Серебристый', 'Газель')
work_car.go()
print(work_car.speed_bust())
work_car.turn(1)
work_car.turn(0)
work_car.stop()
print(' ')

sport_car = SportCar(200, 'Белый', 'Тюнингованная шестерка')
sport_car.go()
print(sport_car.speed_bust())
sport_car.turn(1)
sport_car.turn(0)
sport_car.stop()
print(' ')

town_car = TownCar(100, 'Серая', 'Приора')
town_car.go()
print(town_car.speed_bust())
town_car.turn(1)
town_car.turn(0)
town_car.stop()
print(' ')
