class Stationery:
    def __init__(self,  title, dgraw = ''):
        self.title = title
        self.dgraw = dgraw
        print(f'Выбран {self.title} {self.dgraw}')

    def draw(self):
        print(f'{self.title} запуск отрисовки{self.dgraw}')

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} запуск отрисовки{self.dgraw} тонкая  четкая линия')



class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} запуск отрисовки{self.dgraw} тонкая блеклая линия')

class Handle(Stationery):
    
    def draw(self):
        print(f'{self.title} запуск отрисовки{self.dgraw} толстая яркая линия')

pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карандаш")
pencil.draw()
handle = Handle("Маркер")
handle.draw()
