
activities = [(12, 15), (0, 9), (0, 11), (5, 15), (9, 13), (0, 14), (4, 12)]

k = 0
selected = set()

if len(activities):
  selected.add(0)

activities.sort(key=lambda x: x[1])

for i in range(1, len(activities)):
    if activities[i][0] >= activities[k][1]:
        selected.add(i)


print("Selected Activities: ", end = '  ')
for element in  selected:
    print(element, end = '  ')
