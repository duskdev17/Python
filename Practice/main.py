s = [10, 12, 20]
f = [20, 25, 30]


n = len(s)
A = [0]
i=0

for m in range(1, n):
    if s[m] >= f[i]:
        A.append(m)

print("Selected Activities: ")

for element in A:
    print(element, end='    ')