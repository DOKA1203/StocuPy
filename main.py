n = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def canplaceInSq(y, x, su):
    y = y // 3
    x = x // 3
    y *= 3
    x *= 3
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if n[i][j] == su:
                return bool(0)
    return bool(1)


def canplace(y, x, su):
    for i in range(9):
        if n[y][i] == su:
            return bool(0)
    for i in range(9):
        if n[i][x] == su:
            return bool(0)
    return canplaceInSq(y, x, su)


def stD(y, x):
    if x == 9:
        y += 1
        x = 0
    if y == 9:
        for i in range(9):
            print(n[i])

        return bool(1)
    if n[y][x] == 0:
        for i in range(1, 10):
            if canplace(y, x, i) == bool(1):
                n[y][x] = i
                if stD(y, x + 1):
                    return bool(1)
                n[y][x] = 0
    else:
        return stD(y, x + 1)


stD(0, 0)
