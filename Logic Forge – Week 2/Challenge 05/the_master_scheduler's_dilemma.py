def min_cancelled_bookings(intervals):
    intervals.sort(key=lambda x: x[1])
    end=float('-inf')
    res=0
    for inter in intervals:
        if inter[0]>=end:
            end=inter[1]
        else:
            res+=1
    return res
intervals=[]
n=int(input())
for i in range(0,n):
    temp=list(map(int,input().split()))
    intervals.append(temp)
print(min_cancelled_bookings(intervals))