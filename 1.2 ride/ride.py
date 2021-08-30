"""
ID: angela.14
LANG: PYTHON3
TASK: ride
"""
with open('ride.in', 'r') as fin:
    line1 = fin.readline().strip()
    line2 = fin.readline().strip()

def convertint(line):
    product = 1
    for i in line:
        product = product * (ord(i)-ord('A')+1)
    return product % 47

rst = 'GO\n' if convertint(line1) == convertint(line2) else 'STAY\n'
# if convertint(line1) == convertint(line2):
#     print("GO")
# else:
#     print("STAY")

with open('ride.out', 'w') as fout:
    fout.write(rst)