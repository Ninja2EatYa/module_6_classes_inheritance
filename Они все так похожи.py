import math


class Figure:
    sides_count = 0

    def __init__(self, __color, __sides):
        if self.__is_valid_sides(*__sides):
            if isinstance(self, Cube):
                self.__sides = list(__sides) * self.sides_count
            else:
                self.__sides = list(__sides)
        else:
            self.__sides = [1] * self.sides_count
        self.__color = list(__color) if self.__is_valid_color(*__color) else [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *__sides):
        cond1 = all(isinstance(side, int) and side > 0 for side in __sides)
        if isinstance(self, Cube):
            cond2 = len(__sides) == 1
        else:
            cond2 = len(__sides) == self.sides_count  #  или сравнить с len(self.__sides) вместо self.sides_count
        return cond1 and cond2

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides) * self.sides_count
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__radius = self.__calculate__radius()

    def __calculate__radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__height = self.__calculate__height()

    def __calculate__height(self):
        p = sum(self.get_sides()) / 2
        return ((2 * math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))) /
                self.get_sides()[0])

    def get_square(self):
        return (self.__calculate__height() * self.get_sides()[0]) / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)

    def get_volume(self):
        return super().get_sides()[0] ** 2 * 6


print('Из задания:')
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# круг
print('\n\n\nКруг:')
circle1 = Circle((200, 200, 100), 10)
print('стороны:', circle1.get_sides())
print('прощадь:', circle1.get_square())
print('радиус:', circle1.get_radius())
print('цвета:', circle1.get_color())
circle1.set_color(1, 2, 3)
print('цвета:', circle1.get_color())
circle1.set_color(-1, 200, 3)
print('цвета:', circle1.get_color())
circle1.set_color(1, 2, 300.0)
print('цвета:', circle1.get_color())
circle1.set_sides(15)
print('стороны:', circle1.get_sides())
print('прощадь:', circle1.get_square())  # не меняет площадь
print('радиус:', circle1.get_radius())  # не меняет радиус
circle1.set_sides(10, 8)
print('стороны:', circle1.get_sides())

# треугольник
print('\n\n\nТреугольник:')
fig = Triangle((200, 200, 100), 10)
print('стороны:', fig.get_sides())
print('прощадь:', fig.get_square())  # + получение высоты треугольника
print('цвета:', fig.get_color())

fig = Triangle((200, 200, 100), 10, 7, 9)
print('стороны:', fig.get_sides())
fig.set_sides(1)
print('стороны:', fig.get_sides())
fig.set_sides(1, 2, 3)
print('стороны:', fig.get_sides())
fig.set_sides(1, 2, -3)
print('стороны:', fig.get_sides())

# куб
print('\n\n\nКуб:')
fig = Cube((200, 200, 100), 10, 12)
print('стороны:', fig.get_sides())
print('прощадь:', fig.get_volume())
print('цвета:', fig.get_color())

fig = Cube((200, 200, 100), 10)
print('стороны:', fig.get_sides())
fig.set_sides(50)
print('стороны:', fig.get_sides())
fig.set_sides(-100)
print('стороны:', fig.get_sides())
fig.set_sides(1, 2, 3)
print('стороны:', fig.get_sides())
fig.set_sides(1, 2, -3)
print('стороны:', fig.get_sides())
