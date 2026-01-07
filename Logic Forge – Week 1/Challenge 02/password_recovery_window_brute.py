log=str(input())
pattern=str(input())
hsh=dict()
for ch in pattern:
    if ch in hsh:
        hsh[ch]+=1
    else:
        hsh[ch]=1 
mn=1e18
ans=""
for i in range(len(log)):
    start=i
    temp=hsh.copy()
    temp_str=""
    for j in range(start,len(log)):
        temp_str+=log[j]
        if log[j] in temp:
            temp[log[j]]-=1
            if temp[log[j]]==0:
                del temp[log[j]]
            if len(temp)==0:
                if(j-i+1<mn):
                    mn=j-i+1
                    ans=temp_str
print(ans)
    