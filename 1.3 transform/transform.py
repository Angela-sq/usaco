"""
ID: angela.14
LANG: PYTHON3
TASK: transform
"""
import copy
old = []
new = []
trans = []
with open('transform.in', 'r') as fin:
    N = int(fin.readline().strip())

    for i in range(N):
        old.append(list(fin.readline().strip()))
    
    for i in range(N):
        new.append(list(fin.readline().strip()))

def rotation(square):
    temp = []
    for i in range(N):
        temp2 = []
        for j in range(N):
            temp2.append(square[N-j-1][i])
        temp.append(temp2)
    square = copy.deepcopy(temp)
    return square

def reflection(square):
    temp = []
    for i in range(N):
        temp.append(square[i][::-1])
    square = copy.deepcopy(temp)
    return square

# check transformations #1-#3
old1 = copy.deepcopy(old)
for i in range(3):
    old1 = rotation(old1)
    if old1 == new:
        trans.append(i+1)
        break

old2 = copy.deepcopy(old)
old2 = reflection(old2)
if old2 == new:
    trans.append(4)

for i in range(3):
    old2 = rotation(old2)
    if old2 == new:
        trans.append(5)
        break

if old == new:
    trans.append(6)

if not trans:
    trans.append(7)

with open('transform.out', 'w') as fout:
    fout.write(f"{min(trans)}\n")