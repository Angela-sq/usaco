"""
ID: angela.14
LANG: PYTHON3
TASK: palsquare
"""

palindromes = []

with open('palsquare.in', 'r') as fin:
    base = int(fin.readline().strip())

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        num = int(n % b)
        if num >=10:
            digits.append(chr(65 + num - 10))
        else:
            digits.append(num)
        n //= b
    return digits[::-1]

for i in range(1,301):
    num = numberToBase(i, base)
    num = "".join(map(str, num))
    pal = numberToBase(i*i, base)
    yes = True
    length = len(pal)
    for i in range(length // 2):
        if pal[i] != pal[length - i - 1]:
            yes = False
    if yes == True:
        palindromes.append((num, "".join(map(str, pal))))

with open('palsquare.out', 'w') as fout:
    for i in range(len(palindromes)):
        fout.write(f"{palindromes[i][0]} {palindromes[i][1]}\n")