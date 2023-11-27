import random
f = open("noms.txt","r")

class cycle:
    def __init__(self):
        self.l = []
        self.n = 0
    def ingurgite(self, valeur):
        self.l.append(valeur)
        self.n += 1
    def digere(self):
        random.shuffle(self.l)
    def next(self, gars):
        i = self.l.index(gars)
        return self.l[(i+1)%self.n]
    def __str__(self):
        s = ""
        for i in range(self.n):
            s+=str(self.l[i]) + ' donne un kdo a ' + str(self.l[(i+1)%self.n]) + "\n"
        return s

cycle = cycle()
for line in f:
    line = line.strip()
    cycle.ingurgite(line)
cycle.digere()
print(cycle)
