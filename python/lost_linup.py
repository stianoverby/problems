import sys

n_people, *people = sys.stdin.read().split('\n')
n_people = int(n_people)
people = people[0].split()

Q = [1 for _ in range(n_people)]
for d, p in enumerate(people):
    Q[int(p) + 1] = d + 2

for i in range(len(Q)):
    if i == len(Q) - 1:
        print(Q[i])
        continue
    print(Q[i], end=" ")