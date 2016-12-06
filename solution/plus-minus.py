num = int(input())
arr = list(input().strip().split())

pos, neg, zero = 0, 0, 0

for i in arr:
    if int(i) < 0:
        pos += 1
    if int(i) > 0:
        neg += 1
    else:
        zero += 1

print("%.6f" % (pos / num) + '\n' + "%.6f" % (neg / num) + '\n' + "%.6f" % (zero / num))