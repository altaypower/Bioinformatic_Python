"""ишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

class Teams:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.draws = 0
        self.loses = 0
        self.scores = 0

    def add_win(self):
        self.wins += 1
        self.scores += 3

    def add_lose(self):
        self.loses += 1

    def add_draw(self):
        self.draws += 1
        self.scores += 1


table = {}
for i in range(int(input())):
    com1, sc1, com2, sc2 = input().split(';')
    for command in (com1, com2):
        if command not in table:
            table.update({command: Teams(command)})
    if sc1 > sc2:
        table[com1].add_win()
        table[com2].add_lose()
    elif sc2 > sc1:
        table[com2].add_win()
        table[com1].add_lose()
    else:
        table[com1].add_draw()
        table[com2].add_draw()

for com in table.values():
    print(f'{com.name}:', com.wins + com.draws + com.loses, com.wins, com.draws, com.loses, com.scores)