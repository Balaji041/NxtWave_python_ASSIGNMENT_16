N=int(input())
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for row in range(N):
    name=""
    space="  "*(N-row-1)
    for col in range(row+1):
        name+=string[col]+" "
    print(space+name)
"""
input:7
output:
            A 
          A B 
        A B C 
      A B C D 
    A B C D E 
  A B C D E F 
A B C D E F G 
"""
