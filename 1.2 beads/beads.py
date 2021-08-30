"""
ID: angela.14
LANG: PYTHON3
TASK: beads
"""
with open('beads.in', 'r') as fin:
    N = int(fin.readline().strip())
    necklace = list(fin.readline().strip())

max = 0

def move_element(beads):
    beads.append(beads.pop(0))
    return beads

def one_side(necklace, score):
    color = necklace[0]
    copy = []
    if color == 'w':
        for i in range(len(necklace)):
            if necklace[i] != 'w':
                color = necklace[i]
                break
    for i in range(len(necklace)):
        if color == necklace[i]:
            score += 1
        elif necklace[i] == 'w':
            score += 1
            # necklace[i] = color
        else:
            copy = necklace[i:]
            break
    return copy, score

def find_max(necklace, max):
    #check if all beads are the same color
    ele = necklace[0]
    chk = True
    for item in necklace:
        if ele != item:
            chk = False
            break
    if chk == True:
        return N
    
    for i in range(N):
        score = 0
        result = one_side(necklace, score)
        result2 = one_side(result[0][::-1], result[1])

        move_element(necklace)
        if result2[1] > max:
            max = result2[1]

    return max
        
with open('beads.out', 'w') as fout:
    fout.write(f"{find_max(necklace, max)}\n")