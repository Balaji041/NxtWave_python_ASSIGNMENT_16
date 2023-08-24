N=int(input())
for i in range(N):
    Num=int(input())
    if Num>1: #Num is greater
        is_prime=True
        for j in range(2,Num):
            if Num%j==0:
                is_prime=False
                break
        if is_prime:
            print(Num)
            break
"""
input:5
1
10
4
3
output:3
"""
