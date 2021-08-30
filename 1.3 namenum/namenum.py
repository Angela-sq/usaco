"""
ID: angela.14
LANG: PYTHON3
TASK: namenum
"""

dict = {2:['A','B','C'], 3:['D','E','F'], 4:['G','H','I'], 5:['J','K','L'], 6:['M','N','O'], 7:['P','R','S'], 8:['T','U','V'], 9:['W','X','Y']}

with open('namenum.in', 'r') as fin:
    num = list(fin.readline().strip())

for i in range(len(num)):
    num[i] = int(num[i])

namesList = []
with open('dict.txt') as fin:
    for line in fin:
        namesList.append(line.strip())

names = set(namesList)

# a = []
# for i in range(len(num)):
#     a.append(dict[num[i]])
# cowname = list(itertools.product(*a))

cowname = []
nums = list(num)
def getNameStr(nameStr, start):
    if start == len(nums):
        cowname.append(nameStr)
        return
    for i in dict[nums[start]]:
        getNameStr(nameStr+i, start+1)

getNameStr("", 0)

acceptable = []
for i in range(len(cowname)):
    if cowname[i] in names:
        acceptable.append(cowname[i])

# for i in range(len(acceptable)):
#     acceptable[i] = ''.join(acceptable[i])
acceptable.sort()

with open('namenum.out', 'w') as fout:
    if len(acceptable) == 0:
        fout.write("NONE\n")
    else:
        for i in range(len(acceptable)):
            fout.write(f"{acceptable[i]}\n")