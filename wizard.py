class Wizard:
    def __init__(self, name):
        self.name = name

class House(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

w = House("Ajinkya", "Masurkar")
print(w.name, w.house)
        