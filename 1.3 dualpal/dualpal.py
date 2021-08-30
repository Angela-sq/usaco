"""
ID: angela.14
LANG: PYTHON3
TASK: dualpal
"""

pals = []

with open('dualpal.in', 'r') as fin:
    info = (fin.readline().strip()).split(" ")
    N = int(info[0])
    S = int(info[1])

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

j = 1
while len(pals) < N:
    number = 0
    for i in range(2,11):
        yes = "true"
        palindrome = numberToBase(S+j, i)
        length = len(palindrome)
        for i in range(length // 2):
            if palindrome[i] != palindrome[length - i - 1]:
                yes = "false"
        if yes == "true":
            number += 1
    if number >= 2:
        pals.append(S+j)
    j += 1

with open('dualpal.out', 'w') as fout:
    for i in range(len(pals)):
        fout.write(f"{pals[i]}\n")