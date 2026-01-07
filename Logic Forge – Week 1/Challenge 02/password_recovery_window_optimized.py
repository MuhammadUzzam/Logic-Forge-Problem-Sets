log=str(input())
pattern=str(input())
hsh=dict()
for ch in pattern:
    if ch in hsh:
        hsh[ch]+=1
    else:
        hsh[ch]=1
need=len(hsh)
l=0
mn=1e18
ans=""
for r in range(len(log)):
    if log[r] in hsh:
        hsh[log[r]]-=1
        if hsh[log[r]]==0:
            need-=1
    while need==0:
        if r-l+1<mn:
            mn=r-l+1
            ans=log[l:r+1]
        if log[l] in hsh:
            hsh[log[l]]+=1
            if hsh[log[l]]==1:
                need+=1
        l+=1
print(ans)
