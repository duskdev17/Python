"""Shortest interval -- Greedy Algorithm"""
activity = [(12 , 15 ), (0 , 9 ), (0 , 11 ), (5 , 15 ), (9 , 13 ),( 0 , 14 ), ( 4 , 12 )]

n = len(activity)

sorted_acitivity = sorted(activity, key=lambda x: x[1] - x[0])
print("Sorted by Sortest Interval: ", sorted_acitivity)

selected = []
i = 0
selected.append(activity[i])

for j in range(1, n):
    if sorted_acitivity[j][0] >= sorted_acitivity[i][1]:
        selected.append(activity[j])
        i = j

print("Selected Activities: ", end = '  ')
for element in selected:
    print(element, end = '  ')
