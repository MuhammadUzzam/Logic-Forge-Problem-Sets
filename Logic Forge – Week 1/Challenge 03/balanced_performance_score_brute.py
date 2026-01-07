scoresA=list(map(int,input().split()))
scoresB=list(map(int,input().split()))
arr=scoresA+scoresB
arr.sort()
n=len(arr)
if n%2==1:
    print(arr[n//2])
else:
    print((arr[n//2 - 1] + arr[n//2]) / 2)
