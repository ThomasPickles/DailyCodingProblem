from math import inf

def smallest_interval(nums):
    # initialize pointers array
    pointers = [0] * len(nums)
    ans = -inf, inf

    while True:
        # initialize local variables and end conditions
        local_max = -inf
        local_min = inf
        local_min_index = -1
        reached_end = False

        # iterate over the pointers array
        for i in range(len(pointers)):

            # stop looking if we’ve reached the end of a list
            if pointers[i] >= len(nums[i]):
                reached_end = True
                break

            # calculate the maximum
            if nums[i][pointers[i]] > local_max:
                local_max = nums[i][pointers[i]]

            # calculate the minimum and index of the minimum.
            # index here means which list the minimum is in.
            if nums[i][pointers[i]] < local_min:
                local_min = nums[i][pointers[i]]
                local_min_index = i


        # if we reached the end of any list, we know we’ve already found the optimal interval.
        if reached_end:
            break

        # if the new interval is smaller, update ans
        if local_max - local_min < ans[1] - ans[0]:
            ans = local_min, local_max

        # increment the pointer of the minimum value
        pointers[local_min_index] = pointers[local_min_index] + 1

    return ans

data = [[0, 1, 4, 17, 20, 25, 31],
 [5, 6, 10],
 [0, 3, 7, 8, 12]]

assert smallest_interval(data) == (3, 5), "Should be (3,5)"