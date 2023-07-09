def coin_change(coins,s):
    coins.sort()
    n=len(coins)
    dp = [0 for __ in range(s+1)]
    dp[0]=1
    for i in range(s+1):
        for j in range(n):
            if(i>=coins[j]):
                dp[i]+=dp[i-coins[j]]
            else:
                break
    return dp
print(coin_change([4,8],100))                