N=int(input())
count=0
for i in range(N):
    digit=int(input())
    no_prime=False
    for j in range(2,digit):
        if digit%j==0:
            no_prime=True
            break
    if no_prime:
        count+=digit
print(count)
"""
input:5
8
11
96
49
25
output:178
"""
