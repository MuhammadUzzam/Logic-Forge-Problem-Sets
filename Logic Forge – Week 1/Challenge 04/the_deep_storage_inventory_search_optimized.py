matrix=[]
n=int(input())
for i in range(n):
    x=list(map(int,input().split()))
    matrix.append(x)
k=int(input())
low=matrix[0][0]
high=matrix[n-1][n-1]
def count_before(mid):
    cnt=0
    j=n-1
    for i in range(n):
        while j>=0 and matrix[i][j]>mid:
            j-=1
        cnt+=(j+1)
    return cnt

while low<high:
    mid=(low+high)//2
    if count_before(mid)<k:
        low=mid+1
    else:
        high=mid

print(low)