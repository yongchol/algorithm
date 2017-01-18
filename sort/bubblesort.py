import random

# implements bubble sort algorithm using python
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


# bubble sort test
array = [random.randrange(20) for i in range(10)]

print ("array before sorting")
print (array)

bubble_sort(array)

print ("array after sorting")
print (array)
