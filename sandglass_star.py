N=int(input())
for i in range(N):
    print(" "*i+"* "*(N-i))
for i in range(2,N+1):
    print(" "*(N-i)+"* "*i)
"""
input:5
output:
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
