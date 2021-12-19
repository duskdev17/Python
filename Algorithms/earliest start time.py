n = int(input("How many activities?"))
print("Enter activities starting and ending time in separate line")
activities = []
for i in range(n):
    s, f = map(int, input("Activities %d: "%(i+1)).split())
    activities.append([s, f])
sorted_items = sorted(activities, key=lambda x:x[0])
print(sorted_items)

A=[sorted_items[0]]
i=0

for m in range(1, n):
    if sorted_items[m][0] >= sorted_items[i][1]:
        A.append(sorted_items[m])
        i=m
print("Selected activities earliest start time: ")
print(A)