class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return None
        else:
            for i in range(1, new_floor+1):
                print(i)


h1 = House('ул. 5 Армии д 12', 14)
h2 = House('СНТ Солнышко д 59', 2)
h1.go_to(5)
h2.go_to(7)
