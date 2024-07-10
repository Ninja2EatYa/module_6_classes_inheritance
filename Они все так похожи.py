import math

class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides):
        self.__sides = list(__sides) if self.__is_valid_sides(*__sides) else [1] * self.sides_count
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
        return all(isinstance(side, int) and side > 0 for side in __sides) and len(__sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.__radius = self.__calculate__radius()

    def __calculate__radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
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
        super().__init__(__color, *__sides)
        if len(__sides) != 1:
            self._Figure__sides = [1] * self.sides_count
        else:
            self._Figure__sides = [__sides[0]] * self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) != 1:
            self.__sides = [super().get_sides()[0]] * self.sides_count
        else:
            self.__sides = new_sides

    def get_volume(self):
        return self.__sides[0] ** 2 * 6


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
