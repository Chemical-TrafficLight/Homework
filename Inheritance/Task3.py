"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""

class SpaceObject():
    def __init__(self,size):
        self.size = size

class Star(SpaceObject):
    def __init__(self,brightness):
        self.brightness = brightness
    def print_b(self):
        print('Данная звезда горит с яркостью -'+self.brightness)

class Planet(SpaceObject):
    def __init__(self,population,growth):
        self.population = population
        self.growth = growth
    def print_g(self):
        x = input()
        print(self.population*x)

