class Student:
    def __init__(self,name, house):
        if not name:
            raise ValueError("Empty Input")
        self.name = name
        self.house = house
    def __str__(self):
        return (f"{self.name} is from {self.house}")

printer = Student("Ajinkya", "Masurkar")
print(printer)