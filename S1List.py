# List

# Empty List
my_data = []

# Homo
my_data = [10, 20, 30]

# Hetro
my_data = [1, "John", 97]

# Nested
#            0          1                   2
#            -3         -2                  -1
my_data = ["John", [98, 78, 88], ["john@example.com", "john@abc.edu"]]

print(my_data, type(my_data))

# List Indexing
print(my_data[0])
print(my_data[2])
print(my_data[2][1])

# Negative List Indexing
print(my_data[0])
print(my_data[-1]) # Last Element
print(my_data[-2]) # Second Last Element
print(my_data[-3]) # Third Last Element

# Slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# start from 2nd index till 6th index
print(numbers[2:7])
print(numbers[:5])  # from 0 to 4
print(numbers[5:])  # from 5 till end
print(numbers[:])   # all
print(numbers[:-5]) # starting from 0 till -5(i.e. from the end)

# Manipulate data in list
numbers[1] = 111
print(numbers)

numbers[2:5] = [300, 400, 500]
print(numbers)

numbers.append(77)
print(numbers)

more_numbers = [-10, -20, -30, -40, -50]
numbers.extend(more_numbers)
print(numbers)
print(more_numbers)

new_numbers = numbers + [99, 88, 55]
print(numbers, hex(id(numbers)))
print(new_numbers, hex(id(new_numbers)))

prices = [1000, 3000, 5000, 7000]
# Repeatition
new_prices = prices * 3
print(new_prices)

prices.insert(1, 7000)
print(prices)

# del prices[2]
# del prices[1:3]
prices.remove(7000)
print(prices)

stack = ['a', 'e', 'i', 'o', 'u']
print(stack)
# print(stack.pop(1))
print(stack.pop())
print(stack)

stack.clear()
print("STACK now:", stack)


numbers = [10, 110, 20, 70, 40, 50, 60, 70, 80, 70, 100]
print(numbers.index(70))
print(numbers.count(70))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

# List Comprehension Introduction
# data = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         data.append(i)

# numbers = [x for x in range(1, 11) if x%2==0]
numbers = [x**2 for x in range(1, 11) if x%2==0]
print(numbers)

team1 = ['john', 'jennie']
team2 = ['fionna', 'mark']
team = [ team1_member + team2_member for team1_member in team1 for team2_member in team2]
print(team)

# Membership Testing
print("fionna" in team1)
print("fionna" not in team1)

# Iterate in the List
for member in team1:
    print(member)
