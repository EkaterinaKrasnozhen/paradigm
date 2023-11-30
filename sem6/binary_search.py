# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

def binary_search(arr: list[int], num: int) -> int:
    index = len(arr) // 2
    res = 0
    if num in arr:
        if num >= arr[index]:
            res = [i for i in range(index, len(arr)) if arr[i] == num]
        if num < arr[index]:
            res = [i for i in range(index) if arr[i] == num]
    else:
        res = -1
    return res
     
            
my_list = sorted([1,12,5,10,11])  
res = binary_search(my_list, 12)
print(res)