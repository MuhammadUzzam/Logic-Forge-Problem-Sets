def func(idx,total_sum,coins):
    if(total_sum == 0): return 1
    if(idx < 0): return 0
    ways=0
    coin=0
    while( total_sum - coin >= 0 ):
        ways+=func(idx-1, total_sum - coin, coins)
        coin+=coins[idx]
    return ways
def count_payment_combinations(coins, total_sum):
    return func(len(coins)-1,total_sum,coins)
coins=list(map(int,input().split()))
target_sum=int(input())
print(count_payment_combinations(coins,target_sum))