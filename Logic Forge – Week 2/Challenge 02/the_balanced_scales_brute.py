def subsets(sub,i,arr,res):
    if i==len(arr):
        res.append(sub.copy())
        return
    subsets(sub,i+1,arr,res)
    sub.append(arr[i])
    subsets(sub,i+1,arr,res)
    sub.pop()
temp=[]
def func(arr):
    res=[]
    req_sum=sum(arr)
    if req_sum&1:
        return False
    req_sum//=2
    res=[]
    subsets(temp,0,arr,res)
    for i in range(0, len(res)):
        if sum(res[i])==req_sum:
            return True
    return False
arr=list(map(int,input().split()))
print(func(arr))