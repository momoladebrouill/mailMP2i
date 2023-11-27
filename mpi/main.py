import random
f = open("dummy.graph","r")
random.seed(0)
# arete : (x, poids, y)

class graph:
    def __init__(self):
        self.aretes = []
    def __repr__(self):
        return str(self.aretes)

names = f.readline().split(sep=" ")
g = graph()
countx = 0
for i in f.readlines():
    county = 0
    for j in i.split(sep=" ")[:-1]:
        g.aretes.append((countx, int(j), county))
        county += 1
    countx += 1
f.close()
g.aretes.sort(key=lambda x: -x[1])
cadeaux = []
'''
tant que la matrice ne contient pas que des -1 : 
  liste_max_arete = je recupere toutes les arretes de poid max
  je prends un elt random dans cette liste. (melanger les arretes qui ont les mêmes forces)
  je note ce lien de cadeau
  je supprime toutes les arretes sortantes de celui qui fait le cadeau 
  je supprime toutes les arretes entrantes de celui qui recoit le cadeau
je renvoie la liste des liens de cadeau
'''
while len(g.aretes)>0:
    print(g.aretes)
    liste_max_arete = [] # liste des aretes de poids max
    max_poids = g.aretes[0][1]
    for i in g.aretes:
        if i[1] == max_poids:
            liste_max_arete.append(i)
        else:
            break
    arete = liste_max_arete[random.randint(0,len(liste_max_arete)-1)]
    cadeaux.append(arete)
    g.aretes = [i for i in g.aretes if i[0] != arete[0] and i[2] != arete[2]]
    g.aretes.sort(key=lambda x: -x[1])
print(g)
print(cadeaux)
for arete in cadeaux:
    print("arete : ", names[arete[0]], arete[1], names[arete[2]])
