class Circle:
    all_circles = []
    pi = 3.14159
    def __init__(self, r=1):
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self):
        return self.__class__.pi * self.radius * self.radius
    @staticmethod
    def total_area():
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total