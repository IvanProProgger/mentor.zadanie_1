class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index, state=0):
        self.index = index
        self._state = state

    def grow(self):
        if self._state != 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, count):
        self.tomatoes = [Tomato(i) for i in range(count)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def grow_particular(self, index):
        self.tomatoes[index].grow()

# def all_is_ripe(self):
#     for tomato in self.tomatoes:
#         if not tomato.is_ripe():
#             return False
#         return True

    def add_tomatoes(self, number):
        for i in range(number):
            self.tomatoes.append(Tomato(len(self.tomatoes)+1))

    def all_is_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_all(self):
        tmp = self.tomatoes
        self.tomatoes = []
        return tmp

    def give_harvest(self):
        # self.ripe_tomatoes = list(filter(lambda x: x._state == 3, self.tomatoes))
        # self.tomatoes = list(filter(lambda x: x._state != 3, self.tomatoes))
        tmp = []
        ripe_tomatoes = []
        for tomato in self.tomatoes:
            if tomato._state == 3:
                ripe_tomatoes.append(tomato)
            else:
                tmp.append(tomato)
        print(ripe_tomatoes)
        print(tmp)
        """Возвращает список спелых томатов, удаляя их из списка self.tomatoes"""
        self.tomatoes = tmp
        return ripe_tomatoes


class Gardener:
    def __init__(self, name: str, plant: TomatoBush):
        self.name = name
        self.plant = plant

    def work(self):
        self.plant.grow_all()

    def harvest_all(self):
        tmp = self.plant.tomatoes
        if self.plant.all_is_ripe():
            print('Все томаты собраны')
            self.plant.tomatoes = []
            return tmp
        else:
            print('Предупреждение: Не все томаты поспели!')
            return []
        """
        Проверяет, все ли томаты спелые. Если да, возвращает их. Если нет, возвращает пустой список + пишет предупреждение


            :return:
        """

    def harvest(self):
        self.plant.give_harvest()

        """Возвращает спелые томаты"""

kust_1 = TomatoBush(5)
kust_1.grow_all()
kust_1.grow_all()
kust_1.grow_all()
sadovnik_Ivan = Gardener('Иван', kust_1)
sadovnik_Ivan.harvest()

# Задача. Найти ключи по значениям.
