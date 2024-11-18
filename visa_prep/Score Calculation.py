n=int(input())
for i in range(0,n):
    u,v=map(int, input().split())
    print(v*(u//10))
