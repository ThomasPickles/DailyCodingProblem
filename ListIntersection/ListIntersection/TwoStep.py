#There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

#For example, if N is 4, then there are 5 unique ways:

#1, 1, 1, 1
#2, 1, 1
#1, 2, 1
#1, 1, 2
#2, 2
#What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

# Want to use a set (add only if unique), but can't add list items to a set


[[1, 1, 1, 1],
[2, 1, 1],
[1, 2, 1],
[1, 1, 2],
[2, 2]]

def calculate_steps(N, memo = {1: [[1]], 2: [[1,1],[2]]}):
    assert N > 0, "Can't climb a staircase with no steps"       
    if N not in memo:
        two_steps = [[*step,2] for step in calculate_steps(N-2)]
        one_step = [[*step,1] for step in calculate_steps(N-1)]
        memo[N] = [*one_step, *two_steps]
    return memo[N]


assert calculate_steps(1) == [[1]], "Only one way"
assert calculate_steps(2) == [[1,1],[2]], "Two ways"
assert calculate_steps(3) == [[1,1,1],[2,1],[1,2]], "Three ways"
assert calculate_steps(4) == [[1,1,1,1],[2,1,1],[1,2,1],[1,1,2],[2,2]], "Four ways"

print(calculate_steps(7))

# TODO: needs some memoisation