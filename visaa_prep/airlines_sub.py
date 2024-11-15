x,n= map(int,input().split())
total_planes = (n+99)//100
new_planes = max(0,total_planes - x)
print(new_planes)
