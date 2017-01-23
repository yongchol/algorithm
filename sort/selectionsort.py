import random

# implements selection sort algorithm using python
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]


# selection sort test
array = [random.randrange(50) for i in range(10)]

print ("array before sorting")
print (array)

selection_sort(array)

print ("array after sorting")
print (array)
