def maximize_freelance_profit(deadlines,profits):
    res=[]
    n=len(deadlines)
    for i in range(n):
        res.append([profits[i],deadlines[i]])
    res.sort(reverse=True)
    cur=0
    prof=0
    for profit,deadline in res:
        if deadline<=cur:
            continue
        else:
            prof+=profit
            cur+=1    
    return [cur,prof]
deadlines=list(map(int,input().split()))
profits=list(map(int,input().split()))
print(maximize_freelance_profit(deadlines,profits))