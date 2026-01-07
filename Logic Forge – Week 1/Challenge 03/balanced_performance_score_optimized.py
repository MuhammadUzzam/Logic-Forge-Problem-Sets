scoresA=list(map(int, input().split()))
scoresB=list(map(int, input().split()))
scoresA.append(1e18)
scoresB.append(1e18)
n=len(scoresA)-1
m=len(scoresB)-1
i=0
j=0
med=(n+m)//2+1
cur=0
curnum=0
prevnum=0
while i<n or j<m:
    prevnum=curnum
    if scoresA[i]<scoresB[j]:
        curnum=scoresA[i]
        i+=1
    else:
        curnum=scoresB[j]
        j+=1
    cur+=1
    if(cur==med):
        break
if (n+m)&1:
    print(curnum)
else:
    print((prevnum+curnum)/2)
