string=input()
Vowels="A,E,I,O,U,a,e,i,o,u"
count=0
c=0
for char in string:
    if char in Vowels:
        count+=1
    else:
        if char==" ":
            pass
        else:
            c+=1
print(count)
print(c)
"""
input:Good Morning
output:
4
7
"""
