# Given a list of integers and a number K, return which contiguous elements of the list sum to K.

# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
import time


def contiguousElements(arr, k):
    subarr = []
    s = 0    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarr.append(arr[j])
            s += arr[j]
            if s == k:
                return subarr
            elif s > k:
                s = 0
                subarr = []
                break
    return None

def contiguousElements2(arr, k):
    subarr = []
    for i in arr:
        subarr.append(i)
        if sum(subarr) == k:
            return subarr
        elif sum(subarr) > k:
            while sum(subarr) > k: del subarr[0] 
            if sum(subarr) == k:
                return subarr
    return None

arr = [1, 2, 3, 4, 5]
k = 9

arr2 = [1, 2, 3, 4, 5, 100, 169, 27, 69]
k2 = 69

arr3 = [1, 16, 22, 44, 55, 125, 65, 645, 89, 2, 3, 4, 5]
k3 = 94



start_time = time.time()
print(contiguousElements(arr, k))
print(contiguousElements(arr2, k2))
print(contiguousElements(arr3, k3))
print("--- %s seconds ---" % (time.time() - start_time))

start_time2 = time.time()
print(contiguousElements2(arr, k))
print(contiguousElements2(arr2, k2))
print(contiguousElements2(arr3, k3))
print("--- %s seconds ---" % (time.time() - start_time2))