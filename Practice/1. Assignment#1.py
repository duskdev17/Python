"""Shortest interval -- Greedy Algorithm"""
activity = [(12 , 15 ), (0 , 9 ), (0 , 11 ), (5 , 15 ), (9 , 13 ),( 0 , 14 ), ( 4 , 12 )]

n = len(activity)

activity.sort(key=lambda x: x[1])

selected = []
i = 0
selected.append(activity[i])

for j in range(1, n):
    if activity[j][0] >= activity[i][1]:
        selected.append(activity[j])
        i = j

print("Selected Activities: ", end = '  ')
for element in selected:
    print(element, end = '  ')
