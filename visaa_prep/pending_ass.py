X,Y,Z = map(int,input().split())
total_time_needed= X * Y 
available_time = 2880
if total_time_needed <= available_time:
    print("YES")
else:
    print("No")
