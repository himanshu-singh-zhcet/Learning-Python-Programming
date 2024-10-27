l = [2,3,4,5]
def test(l):
    l1= []
    for i in l:
        l1.append(i*i)
    return l1

l2 = test(l)
print(l2)

def sq(x):
    return x**2
l3 = map(sq,l)
l4 = list(map(sq,l))
l5 = list(map(lambda x:x**2,l))
print(l3)
print(l4)
print(l5)

l6=[1,2,3,4,5]
l7=[6,7,8,9,10]

l8= list(map(lambda x,y:x+y,l5,l6))
print(l8)

s= "pwskills"
s1 = list(map(lambda s:s.upper(),s))
print(s1)