s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]


n = len(s)
A = [0]
i=0

for m in range(1, n):
    if s[m] >= f[i]:
        A.append(m)

print("Selected Activities: ")

for element in A:
    print(element, end='    ')