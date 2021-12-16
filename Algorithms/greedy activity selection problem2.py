n = int(input("Number of activities: "))
print("Enter start and finish time for %d activities: " %n)

activities = []

for i in range(n):
    s, f = map(int, input("Activity %d: " %(i+1)).split())
    activities.append([s, f])

s_a = sorted(activities, key = lambda x:x[1])
print(s_a)

A = [0]
i = 0

for m in range(1, n):
    if s_a[m][0] >= s_a[i][1]:
        A.append(m)
        i = m

print(A)