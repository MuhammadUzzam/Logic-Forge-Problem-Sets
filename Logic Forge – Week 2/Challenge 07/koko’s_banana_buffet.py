piles=list(map(int,input().split()))
k=int(input())
lo=1
hi=max(piles)
res=hi

def func(x):
    res=0
    for pile in piles:
        res+=(pile+x-1)//x
    return res<=k

while lo<=hi:
    mid=(lo+hi)//2
    if(func(mid)):
        hi=mid-1
        res=mid
    else:
        lo=mid+1
print(res)