def MaxActivities(arr, n):
    selected = []

    # Sort jobs according to finish time
    Activity.sort(key=lambda x: x[1])

    # The first activity always gets selected
    i = 0
    selected.append(arr[i])

    for j in range(1, n):
        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
        return selected


# Driver code
Activity = [(4 , 12 ), ( 3 , 12 ), ( 0 , 1 ), ( 0 , 15 ), ( 12 , 14 ), ( 0 , 10 ), ( 0 , 2 )]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected)

# This cde is contributed by kshitijjainm
