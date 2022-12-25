"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""

class Hero():
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def print_info(self):
        print('Уровень здоровья:',self.health)
        print('Класс брони:',self.armor)

class Magician(Hero):
    def hello(self):
        print('-> Поприветствуем нового героя! Прошу, вашему вниманию -',self.name)
    def atack(self,enemy):
        print('Ехе! Видно между героями произошла перепалка!',self.name,'наносит удар',enemy.name)
        enemy.armor -= 10
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print('Какая жалооость! Какой удар обрушился на противника! \nТеперь его броня:'+str(enemy.armor)+', а здоровья:'+str(enemy.health))

knight = Hero('Ричард', 50, 25)
mag = Magician('Берти',40,30)
knight.print_info()
mag.print_info()