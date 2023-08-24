N=int(input())
for i in range(1,N+1):
    string=""
    for j in range(1,i+1):
        string+=str(j)
    for j in range(1,i):
        string+=str(i-j)
    print(string)
"""
input:4
output:
1
121
12321
1234321
"""
