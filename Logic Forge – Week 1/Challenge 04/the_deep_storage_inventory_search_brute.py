matrix=[]
n=int(input())
for i in range(n):
    x=list(map(int,input().split()))
    for j in x:
        matrix.append(j)
k=int(input())
matrix.sort()
print(matrix[k-1])
