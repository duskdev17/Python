"""Earliest Start Time --- Greedy Algorithm"""

activity = [(12 , 15 ), (0 , 9 ), (0 , 11 ), (5 , 15 ), (9 , 13 ),( 0 , 14 ), ( 4 , 12 )]

n = len(activity)
sorted_activities = sorted(activity)
print("Sorted by Earliest Start Time: ", sorted_activities)

selected = []
i = 0
selected.append(activity[i])

for j in range(1, n):
    if sorted_activities[j][0] >= sorted_activities[i][1]:
        selected.append(j)
        i = j

print("Selected Activities: ", end = '  ')
for element in selected:
    print(element, end = '  ')
