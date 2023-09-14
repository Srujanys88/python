def insertion_sort(arr):
    for i in range(len(arr)):
        j=i
        while j>0:
            if arr[j]<arr[j-1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
            j=j-1


arr = [11,43,12,67,23,15,98,65]
print("before insertion sort : ", arr)
insertion_sort(arr)
print("after sorting : ",arr)








