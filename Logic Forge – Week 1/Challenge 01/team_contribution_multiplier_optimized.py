n=int(input())
contributions=list(map(int,input().split()))
pref=[1]*n
suff=[1]*n
for i in range(1,n):
    pref[i]=pref[i-1]*contributions[i-1]
for i in range(n-2,-1,-1):
    suff[i]=suff[i+1]*contributions[i+1]
for i in range(n):
    print(pref[i]*suff[i])
