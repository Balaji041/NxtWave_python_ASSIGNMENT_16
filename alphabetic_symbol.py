N=int(input())
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,N+1):
    name=""
    for j in range(i):
        name=name+string[j]+" "
    print(name)
  """
input:4
output:
A 
A B 
A B C 
A B C D 
"""
