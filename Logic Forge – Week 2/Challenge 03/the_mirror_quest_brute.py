def longestCommonSubsequence(text1,text2):
    n=len(text1)
    m=len(text2)
    def func(n,m):
        if n==0 or m==0:  return 0
        ans=-1
        if text1[n-1]==text2[m-1]:
            ans=1+func(n-1,m-1)
        else:
            ans=max(func(n-1,m),func(n,m-1))
        return ans
    return func(n,m)
def longestPalindromeSubseq(s):
    a=s[::-1]
    return longestCommonSubsequence(s,a);   
text=str(input())
print(longestPalindromeSubseq(text))
