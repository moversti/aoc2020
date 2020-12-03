file = open("input.txt", "r")
rivit = file.readlines()


class Policy:
    def __init__(self, _min, _max, char: str):
        self.min = int(_min)
        self.max = int(_max)
        self.char = char

    def test_pass(self, pw: str):
        c = pw.count(self.char)
        return self.max >= c >= self.min


class RealPolicy:
    def __init__(self, _i1, _i2, char: str):
        self.i1 = int(_i1) - 1
        self.i2 = int(_i2) - 1
        self.char = char

    def test_pass(self, pw: str):
        return False


n = 0
for rivi in rivit:
    p = Policy(rivi.partition('-')[0], rivi.partition('-')[2].partition(' ')[0],
               rivi.partition(':')[0].partition(' ')[2])
    if p.test_pass(rivi.partition(':')[2][1:]):
        n = n + 1
print(n)

n = 0
for rivi in rivit:
    p = RealPolicy(rivi.partition('-')[0], rivi.partition('-')[2].partition(' ')[0],
               rivi.partition(':')[0].partition(' ')[2])
    if p.test_pass(rivi.partition(':')[2][1:]):
        n = n + 1
print(n)