"""
ID: angela.14
LANG: PYTHON3
TASK: barn1
"""

with open('barn1.in', 'r') as fin:
    info = fin.readline().strip().split(" ")
    maxboards, stalls, cows = int(info[0]), int(info[1]), int(info[2])
    barn = []
    for i in range(cows):
        barn.append(int(fin.readline().strip()))

gaps = []
allowablegaps = maxboards - 1
barn = sorted(barn)
for i in range(len(barn)):
    if i != len(barn) - 1:
        gap = barn[i+1] - barn[i] - 1
        if gap > 0:
            gaps.append(gap)

gaps = sorted(gaps)
gaps = gaps[::-1]
total = 0

j=0
while j < allowablegaps and j < len(gaps):
    total = total + gaps[j]
    j += 1

if barn[0] != 1:
    total = total + barn[0] - 1

if barn[len(barn) - 1] != stalls:
    total = total + stalls - barn[len(barn) - 1]

with open('barn1.out', 'w') as fout:
    fout.write(f"{stalls-total}\n")