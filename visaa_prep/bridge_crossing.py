x,y,z = map(int,input().split())
if y >= z:
    print(0)
else:
    max_mangoes = (z - y) // x
    print(max_mangoes)
