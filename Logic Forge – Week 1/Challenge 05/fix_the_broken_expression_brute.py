s=str(input())
res=[]
def subsets(sub,i,s):
    if i==len(s):
        res.append(sub.copy())
        return
    subsets(sub,i+1,s)
    sub.append(i)
    subsets(sub,i+1,s)
    sub.pop()
temp=[]
subsets(temp,0,s)
def valid(sub, s):
    stack=[]
    for i in sub:
        if s[i]=='(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return not len(stack)
mx=0
for sub in res:
    if valid(sub, s):
        mx=max(mx,len(sub))

ans=[]
for sub in res:
    if valid(sub, s) and len(sub) == mx:
        temp=""
        for idx in sub:
            temp+=s[idx]
        ans.append(temp)
st=set()
for i in ans:
    st.add(i)
print(st)

