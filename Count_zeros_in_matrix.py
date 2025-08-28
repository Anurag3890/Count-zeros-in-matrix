m,n=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(m)]
z=sum(row.count(0) for row in a)
print(z)
