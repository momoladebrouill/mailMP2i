import random
def get_mails(path):
    f=open(path)
    f=f.read()
    f=f.split("\n")[:-1]
    l=[]
    for ligne in f:
        ind=ligne.index("<")
        mail=ligne[ind+1:]
        nom=ligne[:ind-1]
        if ">" in mail : mail=mail[:mail.index(">")]
        l.append((nom,mail))
    return l

if __name__=="__main__":
    eleves=get_mails("derniermail.txt")
    print(eleves[random.randint(0,48)])
    print(eleves[random.randint(0,48)])
