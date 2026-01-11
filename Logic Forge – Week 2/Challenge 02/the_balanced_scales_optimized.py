def func(arr):
    sum_arr=sum(arr)
    if sum_arr&1:
        return False
    sum_arr//=2
    n=len(arr)
    # [1 5 11 5]
    '''
        0 1 2 3 4 5 6 7 8 9
    0   T F F F F F F F F F 
    1   T 
    2   T
    3   T
    4   T
    5   T
    '''
    dp=[[False for _ in range(sum_arr+1)] for _ in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,sum_arr+1):
            if j == 0:
                dp[i][j]=True
            elif i == 0:
                dp[i][j]=False
    for i in range(1,n+1):
        for j in range(1,sum_arr+1):
            if j-arr[i-1]>=0:
                dp[i][j]=(dp[i-1][j] or dp[i-1][j-arr[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][sum_arr]

arr=list(map(int,input().split()))
print(func(arr))