#Good morning! Here's your coding interview problem for today.
#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?


def has_pair(data, k):
    complements = []
    for value in data:
        if value in complements:
            return True
        complements.append(k - value)
    return False

assert has_pair([10, 15, 3, 7], 17) == True, "Should contain pair"
assert has_pair([10, 15, 3, 7], 19) == False, "Should not contain pair"
assert has_pair([], 17) == False, "Should not contain pair"


