class Stationery:
    def __init__(self,  title, dgraw = 'Нет эфекта'):
        self.title = title
        self.dgraw = dgraw
        print(f'Выбран {self.title} {self.dgraw}')

    def draw(self):
        print(f'{self.title} запуск отрисовки{self.dgraw}')

class Pen(Stationery):
    def __init__(self, title, dgraw = "тонкая  четкая линия"):
        super().__init__(title, dgraw)

class Pencil(Stationery):
    def __init__(self, title, dgraw = "тонкая блеклая линия"):
        super().__init__(title, dgraw)
class Handle(Stationery):
    def __init__(self, title, dgraw = "толстая яркая линия"):
        super().__init__(title, dgraw)

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
