n=int(input()) 
dp=[-1]*(n+1) 
dp[0]=1 
''' n=5 dp=[-1 -1 -1 -1 -1] mein ith stair se (i-1)th stair p ja skta hon aur (i-2)th stair p ja skta hon. ''' 
def func(i): 
    if i<0: return 0     
    if i==0: return 1 
    if dp[i]!=-1: return dp[i] 
    dp[i]=func(i-1)+func(i-2) 
    return dp[i] 
func(n) 
print(dp[n])