
## Linear Search in Array
## Best case - O(1)
## Worst case - O(n)
## Average case - O(n)

arr = [20, 45, 27, 47, 55, 67, 75, 88, 90]
x = 67

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

result = linear_search(arr, x)
print(x, "is present at index", result)

#----------------------------------------------------------------


