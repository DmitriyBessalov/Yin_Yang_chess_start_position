import itertools

unique = []
unique2 = []
unique3 = []
unique4 = []
unique5 = []
unique6 = []
unique7 = []

for s in itertools.permutations('PKqrrnnbb'):
    poz = (''.join(s))
    # if True:
    #     poz = 'rrqnPKnbb'
    if poz[8] == 'n' or poz[8] == 'b':  # последняя фигура конь или слон
        for y in range(8):
            if poz[y] == 'K' and ((y < 9 and poz[y + 1] == 'P') or (y != 0 and poz[y - 1] == 'P')):  # Король и пешка стоят вместе
                if poz[y] == 'K' and ((y < 9 and poz[y + 1] != 'q' and poz[y + 1] != 'r') and (
                        y != 0 and poz[y - 1] != 'q' and poz[y - 1] != 'r')):  # Король не может стоять рядом с ладьёй или ферзём
                    if poz not in unique:  # опсекаем повторяющиеся позиции
                        unique.append(poz)

for poz in unique:
    if (poz[0] == 'r' or poz[2] == 'r' or poz[4] == 'r' or poz[6] == 'r') and (
            poz[1] == 'r' or poz[3] == 'r' or poz[5] == 'r' or poz[7] == 'r'):  # Ладьи разнопольные
        if (
                (  # Кони или слоны на 1 линии разнопольные
                        poz[8] == 'n'
                ) and (
                        poz[0] == 'b' or poz[2] == 'b' or poz[4] == 'b' or poz[6] == 'b'
                ) and (
                        poz[1] == 'b' or poz[3] == 'b' or poz[5] == 'b' or poz[7] == 'b'
                )
        ) or (
                (
                        poz[8] == 'b'
                ) and (
                        poz[0] == 'n' or poz[2] == 'n' or poz[4] == 'n' or poz[6] == 'n'
                ) and (
                        poz[1] == 'n' or poz[3] == 'n' or poz[5] == 'n' or poz[7] == 'n'
                )
        ):
            unique4.append(poz)

for poz in unique4:  # проверка позиции ферзя
    for y in range(8):
        if poz[8] == 'n':
            if poz[1] == 'q' or poz[3] == 'q' or poz[5] == 'q' or poz[7] == 'q':
                if poz not in unique6:
                    unique6.append(poz)
        else:
            if poz[0] == 'q' or poz[2] == 'q' or poz[4] == 'q' or poz[6] == 'q':
                if poz not in unique6:
                    unique6.append(poz)

for poz in unique6:
    for y in range(8):
        if poz[8] == 'n':  # Проверка разнопольности фигур на 1 и 2 линиях
            if poz[0] == 'P' or poz[2] == 'P' or poz[4] == 'P' or poz[6] == 'P':
                if poz[0] == 'n' or poz[2] == 'n' or poz[4] == 'n' or poz[6] == 'n':
                    if poz not in unique5:
                        unique5.append(poz)
            else:
                if poz[1] == 'n' or poz[3] == 'n' or poz[5] == 'n' or poz[7] == 'n':
                    if poz not in unique5:
                        unique5.append(poz)
        else:
            if poz[1] == 'P' or poz[3] == 'P' or poz[5] == 'P' or poz[7] == 'P':
                if poz[0] == 'b' or poz[2] == 'b' or poz[4] == 'b' or poz[6] == 'b':
                    if poz not in unique5:
                        unique5.append(poz)
            else:
                if poz[1] == 'b' or poz[3] == 'b' or poz[5] == 'b' or poz[7] == 'b':
                    if poz not in unique5:
                        unique5.append(poz)

for poz in unique5:  # перевод в формат FEN
    for y in range(8):
        if poz[y] == 'P':
            if poz[8] == 'b':
                p = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
                if y != 0:
                    p[y - 1] = 'b'
                    unique2.append(poz[:-1] + '/' + ''.join(p) + '/8/8/8/8/' + (''.join(p)).swapcase() + '/' + poz[:-1].swapcase())

                p = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
                if y != 7:
                    p[y + 1] = 'b'
                    unique2.append(poz[:-1] + '/' + ''.join(p) + '/8/8/8/8/' + (''.join(p)).swapcase() + '/' + poz[:-1].swapcase())

            if poz[8] == 'n':
                p = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
                if y != 0 and y != 1:
                    p[y - 2] = 'n'
                    unique2.append(poz[:-1] + '/' + ''.join(p) + '/8/8/8/8/' + (''.join(p)).swapcase() + '/' + poz[:-1].swapcase())

                p = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
                if y != 7 and y != 6:
                    p[y + 2] = 'n'
                    unique2.append(poz[:-1] + '/' + ''.join(p) + '/8/8/8/8/' + (''.join(p)).swapcase() + '/' + poz[:-1].swapcase())

for poz in unique2:  # проверку на защиту второй линии от короля
    cell = ['-', '-', '-', '-', '-', '-', '-', '-']
    for y in range(8):
        if poz[y] == 'q' or poz[y] == 'b':
            if y != 0:
                cell[y - 1] = 'b'
            if y != 7:
                cell[y + 1] = 'B'
        if poz[y] == 'n':
            if 2 <= y <= 7:
                cell[y - 2] = 'n'
            if 0 <= y <= 5:
                cell[y + 2] = 'N'

    for y in range(8):
        if poz[y] == 'K':
            if y == 0:
                if '-' not in str(cell[y] + cell[y + 1]):
                    if poz not in unique3:
                        unique3.append(poz)
            if 0 < y < 7:
                if '-' not in str(cell[y - 1] + cell[y] + cell[y + 1]):
                    if poz not in unique3:
                        unique3.append(poz)
            if y == 7:
                if '-' not in str(cell[y - 1] + cell[y]):
                    if poz not in unique3:
                        unique3.append(poz)

i = 0
for poz in unique3:
    f = ''
    w = 10
    for y in range(8):
        if poz[y] == 'K':
            if y != 7 and poz[y + 1] == 'P':
                f = y - 1
                w = y - 2
            if y != 0 and poz[y - 1] == 'P':
                f = y + 1
                w = y + 2

    if f != '':
        if poz[7] == 'K' and poz[6] == 'P':
            unique7.append(poz)
        if poz[0] == 'K' and poz[1] == 'P':
            unique7.append(poz)
        for y in range(8):
            if poz[y] == 'K' and poz[y + 9] == 'b':
                if poz not in unique7:
                    unique7.append(poz)
        if 0 <= w <= 7:
            if poz[w] == 'q' or poz[w] == 'r':
                if poz not in unique7:
                    unique7.append(poz)

for poz in unique7:
    # print(str(i) + ' ' + poz)
    print(poz)
    i = i + 1
