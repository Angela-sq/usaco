"""
ID: angela.14
LANG: PYTHON3
TASK: milk
"""

farmers = []
money = 0

with open('milk.in', 'r') as fin:
    info = fin.readline().strip().split(" ")
    total, N = int(info[0]), int(info[1])
    for i in range(N):
        info = fin.readline().strip().split(" ")
        farmers.append((int(info[0]), int(info[1])))

farmers = sorted(farmers)
print(farmers)

j = 0
while total > 0:
    if total >= farmers[j][1]:
        total = total - farmers[j][1]
        money = money + farmers[j][0]*farmers[j][1]
        j += 1
    elif total < farmers[j][1]:
        money = money + total*farmers[j][0]
        total = 0

with open('milk.out', 'w') as fout:
    fout.write(f"{money}\n")