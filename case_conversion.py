string=Name[0]
strn=""
l=len(Name)
for i in range(1,l):
    if Name[i].isupper():
        strn+="_"+Name[i]
    else:
        strn+=Name[i]
print((string+strn).lower())
"""
input:PythonLearning
output:python_learning
"""
