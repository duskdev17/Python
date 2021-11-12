s = [12,0,0,5,9,0,4]
f = [15,9,11,15,13,14,12]


n = len(s)
A = [0]
i=0

for m in range(1, n):
    if s[m] >= f[i]:
        A.append(m)

print("Selected Activities: ")

for element in A:
    print(element, end='    ')