import random
import os
import re

class Loto_card:
    def __init__(self, name, name_2):
        self.name = name
        self.name_2 = name_2
    def Card(self):
        line_1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        line_2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        line_3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        all_spisok = []
        spisok = []

        i = 0
        while i != 15:
            a = random.randint(1, 90)
            if a not in spisok:
                spisok.append(a)
                i += 1

        ryad = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for el in spisok[0:5]:
            k = random.choice(ryad)
            line_1[k-1] = el
            ryad.remove(k)

        ryad = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for el in spisok[5:10]:
            k = random.choice(ryad)
            line_2[k-1] = el
            ryad.remove(k)


        ryad = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for el in spisok[10:15]:
            k = random.choice(ryad)
            line_3[k-1] = el
            ryad.remove(k)

        all_spisok.append(line_1)
        all_spisok.append(line_2)
        all_spisok.append(line_3)

        return all_spisok
        return self.name

class Start(Loto_card):

    def start(self, play_1, play_2):
        bocenki = list(range(1, 90))
        while True:
            print('-' * 10, f'{self.name}', '-' * 10, )
            for el in play_1:
                if el != ' ':
                    print(' '.join(map(str, el)))

            print('-' * 10, f'{self.name_2}', '-' * 10, )
            for el in play_2:
                if el != ' ':
                    print(' '.join(map(str, el)))

            boch = random.choice(bocenki)
            otvet = input(f'Новый боченок №:{boch} (осталось {len(bocenki)})\nВведите y/n: ')
            bocenki.remove(boch)
            if otvet == 'y':
                if boch in play_1[0]:
                    k = play_1[0].index(boch)
                    play_1[0][k] = '-'
                    os.system('cls')

                elif boch in play_1[1]:
                    k = play_1[1].index(boch)
                    play_1[1][k] = '-'
                    os.system('cls')

                elif boch in play_1[2]:
                    k = play_1[2].index(boch)
                    play_1[2][k] = '-'
                    os.system('cls')

                else:
                    print('Вы проиграли')
                    break

            if otvet == 'n':
                if boch in play_1[0]:
                    print('Вы проиграли')
                    break
                elif boch in play_1[1]:
                    print('Вы проиграли')
                    break
                elif boch in play_1[2]:
                    print('Вы проиграли')
                    break
                else:
                    os.system('cls')

            if boch in play_2[0]:
                c = play_2[0].index(boch)
                play_2[0][c] = '-'
                os.system('cls')

            elif boch in play_2[1]:
                c = play_2[1].index(boch)
                play_2[1][c] = '-'
                os.system('cls')

            elif boch in play_2[2]:
                c = play_2[2].index(boch)
                play_2[2][c] = '-'
                os.system('cls')

            g = play_1[0] + play_1[1] + play_1[2]
            h = ','.join(map(str, g))
            j = re.search('\d+', h) is not None

            if j == False:
                print('Поздравляю, вы победили!')
                break

            g = play_2[0] + play_2[1] + play_2[2]
            h = ','.join(map(str, g))
            j = re.search('\d+', h) is not None

            if j == False:
                print('Победил компьютер')
                break

game = Loto_card.Card('Игрок')
game_1 = Loto_card.Card('Компьютер')

k = Start('Игрок', 'Компьютер')
k.start(game, game_1)
