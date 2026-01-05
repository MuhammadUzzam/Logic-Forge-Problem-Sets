n=int(input())
contributions=list(map(int,input().split()))
impact=[]
for i in range(n):
    temp=1
    for j in range(n):
        if(i==j):   
            continue
        temp*=contributions[j]
    impact.append(temp)
for i in range(n):
    print(impact[i])