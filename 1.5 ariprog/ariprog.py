"""
ID: angela.14
LANG: PYTHON3
TASK: ariprog
"""
import math


with open('ariprog.in', 'r') as fin:
    N = int(fin.readline().strip())
    M = int(fin.readline().strip())

bisquares = set()
last_element = 0

for p in range(M+1):
    for q in range(M+1):
        bisquares.add(p*p+q*q)
        if p == M and q == M:
            last_element = p*p+q*q
# print(bisquares)

def check_if_progression(start, difference):
    number_of_terms = 1
    curr = start
    while number_of_terms < N:
        if curr + difference in bisquares:
            curr += difference
            number_of_terms += 1
        else:
            return False
    return True


ari_prog_sequences = []

for val in bisquares:
    for j in range(1, math.floor(last_element / (N-1))+1):
        if check_if_progression(val, j) == True:
            ari_prog_sequences.append((j, val))

ari_prog_sequences = sorted(ari_prog_sequences)

with open('ariprog.out', 'w') as fout:
    length = len(ari_prog_sequences)
    if length ==  0:
        fout.write(f"NONE\n")
    else:
        for i in range(length):
            fout.write(f"{ari_prog_sequences[i][1]} {ari_prog_sequences[i][0]}\n")