'''
import difflib

cases=[('afrykanerskojęzyczny', 'afrykanerskojęzycznym'),
       ('afrykanerskojęzyczni', 'nieafrykanerskojęzyczni'),
       ('afrykanerskojęzycznym', 'afrykanerskojęzyczny'),
       ('nieafrykanerskojęzyczni', 'afrykanerskojęzyczni'),
       ('nieafrynerskojęzyczni', 'afrykanerskojzyczni'),
       ('abcdefg','xac')] 
cases = [
            ('algorithme', 'rythme'),
            ('algorithme', 'logarithme')
        ]
for a,b in cases:     
    print('{} => {}'.format(a,b))
    cout = 0  
    for i,s in enumerate(difflib.ndiff(a, b)):
        print(i, s)
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
            cout += 2
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))  
            cout += 2
    print('cout : ',cout)
    print() 
'''
def cout(s1:list, s2:list):
    #c = cout
    global ct
    a, b = len(s1), len(s2)
    #s1, s2 = list(s1), list(s2)
    print('s1', s1)
    print('s2', s2)
    if s1 != s2:
        if a > b:
            print('lens(s1) > len(s2)')
            #div_position = [i for i in range(min(a, b)) if s1[i] != s2[i]]
            exces_elements = [_ for _ in range(a) if s1[_] not in s2]
            #map(lambda _ : s1.pop(_), exces_elements)
            i = 0
            for _ in exces_elements:
                print('deleted {} from {} at position {}'.format(s1[_-i], s1, _-i))
                tmp = s1.pop(_ - i)
                i += 1
                ct += 2
            cout(s1, s2)

        if a < b:
            print('lens(s1) < len(s2)')
            s2_exces_elements = [_ for _ in range(b) if s2[_] not in s1]
            for _ in s2_exces_elements: 
                print('inserting {} from {} at position {}'.format(s2[_], s1, _))
                s1.insert(_, s2[_]) 
                ct += 2
            cout(s1, s2)
        
        else:
            if ''.join(s1) == ''.join(s2):
                return ct
            diff_elements = [_ for _ in range(a) if s1[_]!=s2[_]]
            print('differents elements')
            [print(_, s1[_]) for _ in diff_elements]
            #if 0 in diff_elements:
            #    s1.pop(0)
            i = 0
            for _ in diff_elements:
                s1.pop(_-i)
                ct += 2
                if s1[_-i] != s2[_-i]:
                    s1.insert(_-i, s2[_-i])
                    ct += 1
                else : i += 1
                if s1 == s2: return ct
                cout(s1, s2)
            
            #for _ in range(1, a-1):
            #    if s1[_] == s2[_+1] and s2[_] == s1[_+1]:
            #        s1[_], s1[_+1] = s2[_+1], s2[_]
            
            #cout(s1, s2)

    
    return ct
''' before the else
        if a == b:
            print('they do not have same beginning elements')
            s1.pop(0)
            cout(s1, s2)
        '''


ct = 0
#print(cout(list('arbre'), list('arbore')))
#cout(list('algorithme'), list('logarithme'))
cout(list('algorithme'), list('rythme'))
print(ct)