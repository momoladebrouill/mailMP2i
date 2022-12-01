import derniermail
import sender0
import shuffle

l=derniermail.get_mails("derniermail.txt")
pairs=shuffle.shuffle(l)
for a,b in zip(l,pairs):
    sender0.send([a[1]],"Secret Santa 🎄",
f"""Salut {a[0]}! c'est Bob le bonhomme de neige !⛄
Alors voilà, nos chers délégués, appuyés par une grande partie de la classe on décidé d'organiser un secret Santa. Le principe ?
Faire un cadeau à moins de 5€ comme si tu était le père Noël à une personne de la classe tirée aléatoirement. De cette manière, chacun reçoit un petit cadeau surprise juste avant noël ! 
Mais attention !! La personne à qui tu adresses ton cadeau ne doit pas savoir qui est son père noël secret !🎅
Tu recevras donc aussi un petit cadeau ce jour là, alors tiens toi prêt.e !
Ainsi, un algorithme très complexe a tranché, et toi tu devras offrir un cadeau à {b[0]} !!!
Tu as donc jusqu'au Jeudi 15 décembre à 17h pour trouver un petit cadeau pour {b[0]} !
Bon courage !☃
Avec pleins de bisous gelés,
Bob Paslabobine


PS : si tu ne souhaites pas participer, il te suffit de me répondre en m'indiquant cela, on s'arrangera pour les petits soucis de distributions, mais dis le moi avant vendredi soir ! uwu""")
