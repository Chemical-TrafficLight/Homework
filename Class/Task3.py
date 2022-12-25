class Animal():
    def __init__(self,vid_type,voice):
        self.type = vid_type
        self.voice = voice


    def print_t(self):
        print(self.voice)

egnyat = Animal('Барящик','Кушоц хочеца')
egnyat.print_t()
print(egnyat.type)
katilovka = Animal('Птичка','Курлык-курлык')
print(katilovka.type)
katilovka.print_t()