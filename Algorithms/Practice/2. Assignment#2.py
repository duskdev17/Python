"""Earliest Starting Time --- Greedy Algorithm"""
activities = [(12 , 15 ), (0 , 9 ), (0 , 11 ), (5 , 15 ), (9 , 13 ),( 0 , 14 ), ( 4 , 12 )]

n = len(activities)

print("Activities : ", activities)
print("Number of activities : ", n)

sorted_items = sorted(activities)

print("Sorted Activities by Earliest Start Time : \n",sorted_items)

a = [0]
i = 0

for r in range(1, n):
    if sorted_items[r][0] >= sorted_items[i][1]:
        a.append(r)
        i = r

print("Selected Activities For Earliest Start Time: ",end=" ")
for element in a:
    print(sorted_items[element], end=' ')
print("\nSelected Index For Earliest Start Time:", a)