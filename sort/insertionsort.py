import random

# implements insertion sort algorithm using python
def insertion_sort(array):
    for i in range(1,len(array)):
        cur_value = array[i]
        index = i
        while index > 0 and array[index-1] > cur_value:
            array[index-1], array[index] = array[index], array[index-1]
            index -= 1

# insertion sort test
array = [random.randrange(50) for i in range(10)]

print ("array before sorting")
print (array)

insertion_sort(array)

print ("array after sorting")
print (array)
