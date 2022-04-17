def position(s1, s2):
    return [_ for _ in range(max(len(s1), len(s2))) if s1[_] != s2[_]]


def cout(string1 : str, string2 : str):
    a,b,c = len(string1), len(string2), 0
    s1, s2 = string1, string2
    if a > b :
        s = supprimer(string1, string2)
        c += s[0]
        s1 = ''.join(s[1::])
    elif a < b :
        s = ajout(s1, s2)
        c += s[0]
        s1 = ''.join(s[1::])
    else :
        if s1 == string2: return c
        print('same lenght')
        s = remplacement(s1, s2)
        c += s[0]
        s1 = ''.join(s[1::])
        
        if s1 == string2: return c

        s = echange(s1, s2)
        c += s[0]
        s1 = ''.join(s[1::])

    return c
    """
    if a == b:
        position = []
        ## replace with
        '''
        position = position(string1, string2)
        '''
        for _ in range(b):
            if string1[_] != string2[_]:
                position.append(_)
        return 3*len(position)
    else:
        if a > b:
            for _ in range(a):
                if string1[_] not in string2:
                    string1.replace(string1[_], '')
            cout(string1, string2)
        else:
            for _ in range(b):
                if string2[_] not in string1:
                    string2.replace(string2[_], '')
            cout(string1, string2)
    """

# retourne un dico qui contient un seul element dont l'index est le cout et et la valeur la chaine initiale
def supprimer(s1:str, s2:str):
    cout = 0
    ret = list(s1)
    ret.insert(0, 0)
    for _ in range(len(s1)):
        if s1[_] not in s2:
            ret.pop(_+1)
            ret[0] += 2
            print("suppression")
    return ret

# retourn une liste dont le premier element est le cout de l'ajout et les autres sont les caracteres de la nouvelle chaine
# obtenue apres l'ajout
def ajout(s1:str, s2:str):
    ret = list(s1)
    ret.insert(0, 0)
    for _ in range(len(s2)):
        if s2[_] not in s1:
            ret.insert(_+1, s2[_])
            ret[0] += 2
            print("ajout")
        '''
        if s1[_] != s2[_]:
            ret.insert(_, s2[_])
            ret[0] += 2
        '''

    return ret


def echange(s1:str, s2:str):
    if s1 == s2:
        ret = list(s1)
        ret.insert(0, 0)
        return ret
    ret = list(s1)
    ret.insert(0, 0)
    for _ in range(0, len(s1) - 1, 1):
        if s1[_] == s2[_+1] and s2[_] == s1[_+1]:
            ret.pop(_+1)
            ret.pop(_+2)
            ret.insert(_+2, s1[_+1])
            ret.insert(_+1, s1[_+2])
            ret[0] += 3
            print('echange')
        #print(ret)
    return ret

# retourne
def remplacement(s1:str, s2:str):
    if s1 == s2:
        ret = list(s1)
        ret.insert(0, 0)
        return ret
    ret = list(s1)
    ret.insert(0, 0)
    for _ in range(0, len(s1) - 1):
        #if s1[_] == s2[_ + 1] and s2[_] == s1[_ + 1]:
        if s1[_] != s2[_]:
            ret.pop(_ + 1)
            ret.insert(_ + 1, s2[_])
            ret[0] += 3
            print('remplacement')

    return ret

print(cout('algorithme', 'logarithme'))
