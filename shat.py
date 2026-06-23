import random


def merge(arr1, arr2):
    i , j = 0 , 0
    merged = []

    # arr1 = [1, 2, 3]
    # m = 3
    # arr2 = [1, 4, 5, 7, 8, 13]
    # n = 6

    # i = 0, 1, 2, 3
    # j = 0, 1, 
    #ans = [1, 1, 2, 3, ]


    m = len(arr1) # m = 3, i = 3
    n = len(arr2)

    while i < m and j < n: # 3
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    while i < len(arr1): # 0
        merged.append(arr1[i])
        i += 1
        
    while j < len(arr2): # 4
        merged.append(arr2[j])
        j += 1
    
    # TC = O(m + n)
    
    return merged



            
        


if __name__ == "__main__":
    arr1 = sorted([random.randrange(0, 101) for _ in range(random.randrange(0, 21))])
    arr2 = sorted([random.randrange(0, 101) for _ in range(random.randrange(0, 21))])
    
    
    
    print("arr1: ", arr1)
    print("arr2: ", arr2)
    ans = merge(arr1, arr2)

    print("merged arr: ", ans)
    
    print("size of arr1: ", len(arr1))
    print("Size of arr2: ", len(arr2))
    # print(sorted(arr1 + arr2))
   
    print("size of merged arr: ", len(ans))