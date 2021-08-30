"""
ID: angela.14
LANG: PYTHON3
TASK: combo
"""

with open('combo.in', 'r') as fin:
    N = int(fin.readline().strip())
    j1, j2, j3 = map(int, fin.readline().strip().split(" "))
    m1, m2, m3 = map(int, fin.readline().strip().split(" "))

def close(a, b):
    if abs(a-b) <= 2: return True;
    if abs(a-b) >= N-2: return True;
    return False

total = 0
for c1 in range(1, N+1):
    for c2 in range(1, N+1):
        for c3 in range(1, N+1):
            if (close(j1, c1) and close(j2, c2) and close(j3, c3)) or (close(m1, c1) and close(m2, c2) and close(m3, c3)):
                total +=1

with open('combo.out', 'w') as fout:
    fout.write(f"{total}\n")