class Book:
    def __init__(self,name, house):
        if not name:
            raise ValueError("Empty Input")
        self.name = name
        self.house = house

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if not house in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError("Invalid House")
        self._house = house

    def __str__(self):
        return (f"{self.name} is from {self.house}")


printer = Book("Ajinkya", "Gryffindor")
print(printer)
