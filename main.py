list_ints = [100, 1, 10, 20]

print(list_ints[0])
print(list_ints[-4])

list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)
print(type(list_numbers))
list_numbers[0] = "hello"
print(list_numbers)

print(len(list_numbers))
list_numbers.append("another element")
print(list_numbers[len(list_numbers)-1])

empty_list = []
print(len(empty_list))

nested_list = [[0, 1], [2], [3], [4,5], []]
print(len(nested_list))
print(len(nested_list[0]))

candies = ["twix", "reeses", "oreos", "snickers"]
print(candies)

for candy in candies:
    print(candy)

i = 0
for i in range(len(candies)):
        print(i, candies)

print(candies)
candies += ["m&ms", "starburst"]
print(candies)
bag_o_candies = 5 * ["twix", "snickers"]
print(bag_o_candies)
print(candies[1:3])
copy_of_candies = candies[:]
copy_of_candies[0] = "twix"
print(copy_of_candies)
print(candies)
