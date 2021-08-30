"""
ID: angela.14
LANG: PYTHON3
TASK: milk2
"""
times = []

with open('milk2.in', 'r') as fin:
    N = int(fin.readline().strip())

    for i in range(N):
        info = (fin.readline().strip()).split(" ")
        times.append((int(info[0]), int(info[1])))

sorted_times = sorted(times)

for i in range(N):
    sorted_times[i] = list(sorted_times[i])

marker = 0
for i in range(N):
    if marker + 1 >= len(sorted_times):
        break
    elif sorted_times[marker][1] >= sorted_times[marker+1][0] and sorted_times[marker][1] < sorted_times[marker+1][1]:
        sorted_times[marker][1] = sorted_times[marker+1][1]
        sorted_times.pop(marker+1)
    elif sorted_times[marker][1] >= sorted_times[marker+1][0] and sorted_times[marker][1] >= sorted_times[marker+1][1]:
        sorted_times.pop(marker+1)
    else:
        marker += 1

longest_continuous = 0
longest_idle = 0

for i in range(len(sorted_times)):
    if sorted_times[i][1] - sorted_times[i][0] > longest_continuous:
        longest_continuous = sorted_times[i][1] - sorted_times[i][0]

for i in range(len(sorted_times) - 1):
    if sorted_times[i+1][0]-sorted_times[i][1] > longest_idle:
        longest_idle = sorted_times[i+1][0]-sorted_times[i][1]

with open('milk2.out', 'w') as fout:
    fout.write(f"{longest_continuous} {longest_idle}\n")