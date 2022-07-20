prevx = 0

for y in range(1, 11):
    sumx = prevx + y
    print("Current", y, "previous", prevx, "sum", sumx)
    prevx = y