def longestCommonSubsequence(text1,text2):
    n=len(text1)
    m=len(text2)
    dp=[[-1 for i in range(n+1)]for j in range(m+1)]
    def func(n,m):
        if n==0 or m==0:  return 0
        if dp[n][m]!=-1:    return dp[n][m]
        if text1[n-1]==text2[m-1]:
            dp[n][m]=1+func(n-1,m-1)
        else:
            dp[n][m]=max(func(n-1,m),func(n,m-1))
        return dp[n][m]
    return func(n,m)
def longestPalindromeSubseq(s):
    a=s[::-1]
    return longestCommonSubsequence(s,a);   
text=str(input())
print(longestPalindromeSubseq(text))
