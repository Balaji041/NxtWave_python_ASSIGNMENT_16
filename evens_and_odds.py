M=int(input())
N=int(input())
even=0
odd=0
for i in range(M,N+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)
"""
input:-5
7
output:7
6
"""
