def quick_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[0]
    
    less = []
    equal = []
    greater = []


    for i in num_list:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)

    sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)

    
    sorted_list = sorted_less + equal + sorted_greater 
    return sorted_list


print(quick_sort([14,23,15,86,32,18,6,3,5]))