"""
ID: angela.14
LANG: PYTHON3
TASK: skidesign
"""
fin = open('skidesign.in','r')
N = int(fin.readline().strip())

hills= [int(l.strip()) for l in fin.readlines()]
hills.sort()

c=(hills[0]+hills[-1])//2
i=0
costMin=9999999
while i<=hills[-1]-17:    
    costs=[]
    for e in hills:
        if e<i:
            costs.append(i-e)
        elif e>i+17:
            costs.append(e-(i+17))
    
    total=0
    for c in costs:
        total+=c**2
    if total<costMin:
        costMin=total
    i+=1

with open('skidesign.out','w') as fout:
    fout.write(f"{costMin}\n")