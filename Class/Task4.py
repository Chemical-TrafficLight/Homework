class Bus():
    def __init__(self, speed, capacity, max_speed, emptyseats):
        self.speed = speed
        self.capacity = capacity
        self.max_s = max_speed
        self.empt = emptyseats

    def posadka(self,kol_vo):
        if self.empt >= kol_vo:
            self.empt -= kol_vo
            print('Посадили -',kol_vo)
            print('Осталось -', self.empt)
        else:
            print('Посадили -', self.empt)
            self.empt = 0

    def Razognatsya(self, speed):
        if speed + self.speed < self.max_s:
            print('Разогналсиь до -',self.speed + speed)
            self.speed += speed
        else:
            print('Едем в село с мах.скоростью -',self.max_s)
            self.speed = self.max_s

aftobys = Bus(40,80,200,40)
aftobys.posadka(65)
aftobys.posadka(5)
aftobys.Razognatsya(150)
aftobys.Razognatsya(50)