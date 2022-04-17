n = 0
l = []
s = set(l)
dico = dict()
for i in range(int(input())):
    this = input()
    l.append(this)
    '''
    if n%60 == 0:
        s = set(l)
        for _ in s:
            if l.count(_) >= 40:
                print()
        l = []
    else :
        l.append(input())
    '''
for _ in range(0, len(l) - 50, 50):
    for el in range(50):
        pass


