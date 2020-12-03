file = open("input.txt", "r")
rivit = file.readlines()
file.close()
numerot = [int(i) for i in rivit]
numerot.sort()
p1 = 0
p2 = numerot.__len__() - 1
while p1 <= p2:
    summa = numerot[p1] + numerot[p2]
    if summa == 2020:
        print(numerot[p1] * numerot[p2])
        break
    if summa < 2020:
        p1 = p1 + 1
    else:
        p2 = p2 - 1

p1 = 1
p2 = numerot.__len__() - 1
p3 = 0
while p1 <= p2:
    summa = numerot[p1] + numerot[p2] + numerot[p3]
    if summa == 2020:
        print(numerot[p1] * numerot[p2] * numerot[p3])
        break
    if p2 - p1 == 1:
        p3 = p3 + 1
        p2 = numerot.__len__() - 1
        p1 = p3 + 1
    else:
        if summa < 2020:
            p1 = p1 + 1
        else:
            p2 = p2 - 1
