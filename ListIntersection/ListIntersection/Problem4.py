from typing import List

def find_lowest_missing_integer(arr: List[int]) -> int:
    def order_array(arr: List[int]) -> List[int]:
        index = 0
        while index < len(arr):
            value = arr[index]
            if 1 <= value <= len(arr):
                if value != arr[value-1]: # if it's not in its rightful place
                    arr[value-1], arr[index] = value, arr[value-1] # swap both elements
                    index=index-1 # but don't increment counter
            index=index+1
        return arr
    # Could equally use filter(...)[0] since we just want the first occurrence

    return next(index+1 for index, value in enumerate(order_array(arr)) if value != index+1)


assert find_lowest_missing_integer([3, 4, -1, 1]) == 2
assert find_lowest_missing_integer([1, 2, 0]) == 3