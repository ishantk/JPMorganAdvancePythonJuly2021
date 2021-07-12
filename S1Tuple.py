# Tuple

# Empty Tuple -> No Use
my_data = ()

# Homo
# my_data = 10, 20, 30
my_data = (10, 20, 30)

# Hetro
my_data = (1, "John", 97)

# Nested
#            0          1                   2
#            -3         -2                  -1
my_data = ("John", (98, 78, 88), ("john@example.com", "john@abc.edu"))
print(my_data, type(my_data))

# Unpacking the Tuple
var1, var2, var3 = my_data
print(var1)
print(var2)
print(var3)


# Tuple Indexing
print(my_data[0])
print(my_data[2])
print(my_data[2][1])

# Negative Tuple Indexing
print(my_data[0])
print(my_data[-1]) # Last Element
print(my_data[-2]) # Second Last Element
print(my_data[-3]) # Third Last Element

# Slicing
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# start from 2nd index till 6th index
print(numbers[2:7])
print(numbers[:5])  # from 0 to 4
print(numbers[5:])  # from 5 till end
print(numbers[:])   # all
print(numbers[:-5]) # starting from 0 till -5(i.e. from the end)

# As tuple is IMMUTABLE we cannot perform any manipulation operation
# del numbers[1] # NOT OK
# numbers[1] = 777

more_numbers = (1, 2, 3, 4, 5)

# Concatenation
new_numbers = numbers + more_numbers
print(new_numbers)

# Repeat
repeated_numbers = more_numbers * 3
print(repeated_numbers)

# OK
# del more_numbers

# Functions on Tuple
numbers = (10, 20, 10, 40, 50, 10, 70, 80, 90, 100)
print(numbers.count(10))
print(numbers.index(50))

# Membership Testing
print(10 in numbers)
print(77 not in numbers)

print()

# Iterating
for element in numbers:
    print(element)

