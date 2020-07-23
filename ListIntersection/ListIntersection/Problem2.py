def prod(input):
    output = []
    right = 1
    for number in reversed(input):
        output.insert(0, right)
        right *= number
    left = 1
    for i, number in enumerate(input):
        output[i] *= left
        left *= number
    return output


prod([1, 2, 3, 4, 5])
#, the expected output would be [120, 60, 40, 30, 24]
