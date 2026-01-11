def count_payment_combinations(coins, total_sum):
    n=len(coins)
    dp=[[0 for j in range(total_sum+1)] for i in range(n+1)]
    '''
        Target Sum: 4
        Vault Coins: [1, 2, 3]
            
            0 1 2 3 4
        0   1 0 0 0 0 
        1   1 
        2   1
        3   1
    '''
    for i in range(0,n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,total_sum+1):
            if j-coins[i-1]>=0:
                dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    # print(dp)
    return dp[n][total_sum]
coins=list(map(int,input().split()))
target_sum=int(input())
print(count_payment_combinations(coins,target_sum))