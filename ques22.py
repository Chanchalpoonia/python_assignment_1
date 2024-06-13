list1 = [2, 4, 1, 11, 9] 

max_value = list1[0] 

min_value = list1[0] 

for i in list1: 

    if i > max_value: 

        max_value = i 

    if i < min_value: 

        min_value = i 

print(max_value) 

print(min_value) 