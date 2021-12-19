n = int(input("How many activities? "))
print("Enter activities starting and ending time in separate line")
activities = []
for i in range(n):
      s , f = map(int, input("Activities %d: " % (i+1)).split())
      activities.append([s, f])
sorted_item = sorted(activities, key=lambda x: abs(x[1]-x[0]))
print(sorted_item)

A = [sorted_item[0]]
i = 0
for m in range(1, n):
    if sorted_item[m][0] >= sorted_item[i][1]:
        A.append(sorted_item[m])
        i = m
print("Selected activities for shortest interval: ", end=' ')

print(A)