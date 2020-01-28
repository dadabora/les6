
class Worker:
    def __init__(self, name, surname, position, _income1, _income2):
        self.name = name
        self.surname = surname
        self.position = position
        self._income1 = _income1
        self._income2 = _income2
        self._incom = {"wage": self._income1, "bonus": self._income2}
        print(self.name, self.surname, self.position, self._income1, self._income2, self._incom)




class Position(Worker):
    def __init__(self, name, surname, position, _income1, _income2):
        super().__init__(name, surname, position, _income1, _income2)
    def full_incom(self):
        #incom_full = int(self._income["wage"])+int(self._income["bonus"])
        print(f'{self.name}, {self.surname}, {int(self._incom["wage"])+int(self._incom["bonus"])}')

pos1 = Position('Борис', 'Владиславович', 'Подручный подручного', 10000, 2000)
pos1.full_incom()