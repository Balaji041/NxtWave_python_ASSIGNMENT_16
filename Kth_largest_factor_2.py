N=int(input())
K=int(input())
if K>N:
    print("1")
else:
    n=0
    count=0
    for i in range(N):
        if N%(N-i)==0:
            n=N-i
            count+=1
        if count==K:
            break
    print(n)
"""
input:
12
7
output:1
"""
            
