x=int(input())
discount_p1 = x - (0.1 * x)
discount_p2 = x - 100
best_p = min(discount_p1 , discount_p2)
print(int(best_p))
