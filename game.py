import random

class Игра:
    def __init__(self):
        """
        Инициализирует объект игры, создавая игрока, список монстров, 
        список сокровищ и подземельные комнаты. Случайным образом 
        выбирается текущая комната, в которой начинается игра.

        Атрибуты:
            игрок (Игрок): Экземпляр игрока.
            монстры (list[Монстр]): Список монстров с их характеристиками.
            сокровища (list[Сокровище]): Список сокровищ с их стоимостью.
            комнаты_подземелья (list[Комната]): Список комнат подземелья.
            текущая_комната (Комната): Текущая комната, в которой находится игрок.
        """
        self.игрок = Игрок()
        self.монстры = [Монстр("Гоблин", 30, 5, "Огненный шар"), Монстр("Орк", 50, 10, "Рваная бомба"), Монстр("Дракон", 100, 20, "Дыхание огня")]
        self.сокровища = [Сокровище("Золотая монета", 10), Сокровище("Серебряное ожерелье", 25), Сокровище("Древний артефакт", 50)]
        self.комнаты_подземелья = [Комната(f"Комната {i}") for i in range(1, 6)]
        self.текущая_комната = random.choice(self.комнаты_подземелья)

    def начать(self):
        """
        Начинает игру, приветствуя игрока и позволяя ему исследовать подземелье.

        Метод выполняет следующие действия:
            1.  Приветствует игрока.
            2.  Пока игрок жив и есть доступные комнаты, 
                предлагает игроку войти в следующую комнату.
            3.  Если игрок был побежден, сообщает об этом.
            4.  Если игрок успешно исследовал подземелье, 
                поздравляет его с этим.

        """
        print("Добро пожаловать в Подземелье Искателя!")
        while self.игрок.жив() and self.текущая_комната:
            self.войти_в_комнату()

        if not self.игрок.жив():
            print("Игра окончена! Вы были побеждены.")
        else:
            print("Поздравляем! Вы успешно исследовали подземелье.")

    def войти_в_комнату(self):
        """
        Входит в текущую комнату, предлагая игроку 
        встретиться с монстром, собрать сокровище и 
        перейти в следующую комнату.

        """        
        print(f"\nВы вошли в {self.текущая_комната.имя}.")
        self.встретить_монстра()
        self.собрать_сокровище()
        self.перейти_в_следующую_комнату()

    def встретить_монстра(self):
        """
        Встречает монстра, если таковой есть, и предлагает игроку 
        атаковать, бежать, лечиться или использовать магию.

        """
        if random.choice([True, False]):  # Случайно решаем, появится ли монстр
            монстр = random.choice(self.монстры)
            print(f"Дикий {монстр.имя} появляется!")
            while монстр.жив() and self.игрок.жив():
                действие = input("Вы хотите (а)таковать, (б)ежать, (л)ечиться или (м)агия? ").lower()
                if действие == 'а':
                    self.игрок.атаковать(монстр)
                    if монстр.жив():
                        монстр.атаковать(self.игрок)
                elif действие == 'б':
                    print("Вы убежали!")
                    break
                elif действие == 'л':
                    self.игрок.лечиться()
                elif действие == 'м':
                    self.игрок.использовать_магии(монстр)

    def собрать_сокровище(self):
        """
        Случайно выбирает, будет ли в текущей комнате сокровище, 
        и если да, то добавляет его к списку собранных сокровищ игрока.
        """
        if random.choice([True, False]):
            сокровище = random.choice(self.сокровища)
            print(f"Вы нашли {сокровище.имя}, стоимостью {сокровище.стоимость} очков!")
            self.игрок.собрать_сокровище(сокровище)

    def перейти_в_следующую_комнату(self):
        """
        Переходит в случайно выбранную следующую комнату подземелья.
        """
        self.текущая_комната = random.choice(self.комнаты_подземелья)
        print("Переход в следующую комнату...")


class Игрок:
    def __init__(self):
        """
        Инициализирует игрока, создавая атрибуты игрока:
            здоровье (int): Количество здоровья игрока.
            собранные_сокровища (list): Список сокровищ, которые нашел игрок.
            уровень (int): Уровень игрока.
            атака (int): Сила атаки игрока.
            магия (int): Количество магической энергии у игрока.
            броня (int): Количество брони, которое имеет игрок.
            лечения (int): Количество оставшихся лечений.
        """
        self.здоровье = 100
        self.собранные_сокровища = []
        self.уровень = 1
        self.атака = 10
        self.магия = 30  # Магическая энергия
        self.броня = 0    # Броня игрока
        self.лечения = 3   # Количество лечений за игру

    def атаковать(self, монстр):
        """
        Атакует монстра, нанося случайный урон в диапазоне от self.атака - 5 до self.атака + 5.
        
        :param монстр: Монстр, который будет атакован.
        :type монстр: Монстр
        """
        урон = random.randint(self.атака - 5, self.атака + 5)
        монстр.здоровье -= урон
        print(f"Вы нанесли {урон} урона {монстр.имя}. (Здоровье монстра: {монстр.здоровье})")

    def лечиться(self):
        """
        Лечит игрока, добавляя случайное количество здоровья от 10 до 20.
        Если у игрока больше нет лечений, то ничего не происходит.
        """
        if self.лечения > 0:
            лечение = random.randint(10, 20)
            self.здоровье += лечение
            self.лечения -= 1
            print(f"Вы исцелились на {лечение} здоровья. Осталось {self.лечения} лечений.")
        else:
            print("Вы исчерпали все лечащие действия.")

    def использовать_магии(self, монстр):
        """
        Использует магию против монстра, нанося случайный урон от 15 до 30.
        Если у игрока недостаточно магической энергии, то ничего не происходит.
        
        :param монстр: Монстр, который будет атакован магией.
        :type монстр: Монстр
        """
        if self.магия >= 10:
            self.магия -= 10
            урон = random.randint(15, 30)
            монстр.здоровье -= урон
            print(f"Вы использовали магию! {монстр.имя} получил {урон} урона от магического удара. (Здоровье монстра: {монстр.здоровье})")
        else:
            print("Недостаточно магической энергии для заклинания!")

    def собрать_сокровище(self, сокровище):
        """
        Добавляет сокровище к списку собранных сокровищ игрока и
        увеличивает уровень игрока, если количество собранных сокровищ
        стало кратно 3.
        """
        self.собранные_сокровища.append(сокровище)
        print(f"Теперь у вас: {self.получить_стоимость_сокровищ()} общих очков сокровищ.")
        if len(self.собранные_сокровища) % 3 == 0:
            self.уровень += 1
            self.атака += 5
            self.магия += 10
            print(f"Вы достигли уровня {self.уровень}! Ваша атака и магия увеличены.")

    def получить_стоимость_сокровищ(self):
        """
        Возвращает общую стоимость всех собранных сокровищ игрока.

        :return: Сумма стоимости всех сокровищ в списке `собранные_сокровища`.
        :rtype: int
        """
        return sum(с.стоимость for с in self.собранные_сокровища)

    def жив(self):
        """
        Проверяет, жив ли объект, исходя из его текущего уровня здоровья.

        :return: True, если здоровье больше нуля, иначе False.
        :rtype: bool
        """
        return self.здоровье > 0


class Монстр:
    def __init__(self, имя, здоровье, сила_атаки, способность):
        """
        Инициализирует монстра с именем, здоровьем, силой атаки и способностью.

        :param имя: Имя монстра
        :param здоровье: Здоровье монстра
        :param сила_атаки: Сила атаки монстра
        :param способность: Способность монстра
        """
        self.имя = имя
        self.здоровье = здоровье
        self.сила_атаки = сила_атаки
        self.способность = способность

    def атаковать(self, игрок):
        """
        Монстр атакует игрока, нанося случайный урон в пределах своей силы атаки.
        """
        урон = random.randint(1, self.сила_атаки)
        игрок.здоровье -= урон
        print(f"{self.имя} нанёс {урон} урона вам. (Ваше здоровье: {игрок.здоровье})")

    def жив(self):
        """
        Проверяет, жив ли объект, на основе его текущего уровня здоровья.

        :return: Возвращает True, если здоровье больше 0, иначе False.
        """
        return self.здоровье > 0


class Сокровище:
    def __init__(self, имя, стоимость):
        """
        Инициализирует сокровище с именем и стоимостью.

        :param имя: Имя сокровища
        :param стоимость: Стоимость сокровища
        """
        self.имя = имя
        self.стоимость = стоимость


class Комната:
    def __init__(self, имя):
        """
        Инициализирует комнату с именем.

        :param имя: Имя комнаты
        """
        self.имя = имя


if __name__ == "__main__":
    игра = Игра()
    игра.начать()