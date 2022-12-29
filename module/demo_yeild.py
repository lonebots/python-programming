def square(list1):
    # newList = list(("jishnu","jishnu1"))
    newList = list()
    for i in list1:
        newList.append(i * i)
    yield newList


input_list = [1, 2, 3, 4, 5, 6]
print("input list is:", input_list)
output = square(input_list)
print("Output from the generator is:", output)
print("Elements in the generator are:", next(output))
