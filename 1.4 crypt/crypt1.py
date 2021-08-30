"""
ID: angela.14
LANG: PYTHON3
TASK: crypt1
"""
valids = 0

with open('crypt1.in', 'r') as fin:
    N = int(fin.readline().strip())
    nums = fin.readline().strip().split(" ")
    for i in range(N):
        nums[i] = int(nums[i])

factor1, factor2 = [], []
for i in range(N):
    for j in range(N):
        for k in range(N):
            factor1.append((nums[i], nums[j], nums[k]))

for i in range(N):
    for j in range(N):
        factor2.append((nums[i], nums[j]))

for i in range(len(factor1)):
    for j in range(len(factor2)):
        valid = True
        s = [str(n) for n in factor1[i]]
        number = int("".join(s))
        sum1 = number*factor2[j][0]
        sum2 = number*factor2[j][1]
        listsum1 = [int(x) for x in str(sum1)]
        listsum2 = [int(x) for x in str(sum2)]
        if not(len(listsum1) == 3 and len(listsum2) == 3):
            valid = False
        if not(set(listsum1).issubset(set(nums)) and set(listsum2).issubset(set(nums))):
            valid = False
        result = sum1*10 + sum2
        listresult = [int(x) for x in str(result)]
        if not(len(listresult) == 4 and set(listresult).issubset(set(nums))):
            valid = False
        if valid == True:
            valids += 1

with open('crypt1.out', 'w') as fout:
    fout.write(f"{valids}\n")