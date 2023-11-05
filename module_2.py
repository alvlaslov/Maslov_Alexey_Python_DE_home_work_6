import random


def rotation_queens(positions):
    x = []
    y = []
    for i in positions:
        if i[0] != i[1] and i[0] not in x:
            x.append(i[0])
        else:
            return False
        if i[1] not in y:
            y.append(i[1])
        else:
            return False
    return True


def generate_position():
    count = 0
    while count < 4:
        pos = [(((random.randint(1, 8), random.randint(1, 8)))) for i in range(8)]
        if rotation_queens(pos) == True:
            print(pos)
            count += 1


if __name__ == '__main__':
    positions = [(1, 2), (2, 7), (3, 5), (4, 8), (5, 1), (6, 4), (7, 6), (8, 3)]
    # print(rotation_queens(positions))
    generate_position()
