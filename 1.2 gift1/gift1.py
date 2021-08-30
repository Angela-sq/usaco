"""
ID: angela.14
LANG: PYTHON3
TASK: gift1
"""

people = {}

with open('gift1.in', 'r') as fin:
    numppl = int(fin.readline().strip())

    for i in range(numppl):
        people[fin.readline().strip()] = 0
    
    def updateaccount():
        giver = fin.readline().strip()
        info = (fin.readline().strip()).split(" ")
        balance = int(info[0])
        receivers = int(info[1])

        if receivers == 0:
            people[giver] += balance
        else:
            leftovers = balance % receivers
            people[giver] -= (balance - leftovers)
            for i in range(receivers):
                people[fin.readline().strip()] += ((balance - leftovers) / receivers)

    for i in range(numppl):
        updateaccount()
    
with open('gift1.out', 'w') as fout:
    for i in range(numppl):
        person = list(people)[i]
        fout.write(f"{person} {int(people.get(person))}\n")