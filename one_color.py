string=input()
length=len(string)
count=0
c=0
for i in string:
    if i=="G":
        count+=1
    else:
        c+=1
if count>c:
    print(length-count)
else:
    print(length-c)
"""
input:GGGGGGR
output:1
"""
