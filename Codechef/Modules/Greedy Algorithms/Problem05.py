"""
EVacuate to Moon
Pesla needs to charge N cars before sending them to space. The car i has energy capacity of A[i] Watt-hours.
There are M power outlets. The power outlet j provides a power of B[j] Watt. If an outlet can charge at most one car, and a car can be charged by at most one outlet, find the maximum total energy (in Watt-hours) stored in all cars after H hours.

Input Format:
Primary Line: T   ; T-->no. of test-cases
1st line: N, M, H ; N-->no. of cars, M-->no. of outlets, H-->no. of hours
2nd line: <N space-separated integers | energy capacities of N cars>
3rd line: <M space-separated integers | power of M outlets >
"""

# cook your dish here
for t in range(int(input())):
    n,m,h = map(int,input().split())
    N = [int(x) for x in input().split()]
    M = [int(y)*h for y in input().split()]
    
    N.sort(reverse=True)
    M.sort(reverse=True)
    s=0
    
    for i in range(min(n,m)):
        s=s+min(N[i],M[i])

    print(s)
    
    
    
    