# Dictionary

# empty dictionary
my_data = {}

my_data = {101: "John", 201: "Jennie", 301: "Fionna"}

my_data = {101: "John", 201: "Jennie", 301: "Fionna", 401: [10, 20, 30]}
my_data = {101: "John", 201: "Jennie", 301: "Fionna", "marks": [10, 20, 30]}

my_data = dict({101: "John", 201: "Jennie", 301: "Fionna", "marks": [10, 20, 30]})

my_data = dict([(101, "John"), (201, "Fionna")])
print(my_data)

print(my_data[101])
# print(my_data[301]) # Key Error

print(my_data.get(301))

# Update the value for the key 101
my_data[101] = "John Watson"

my_data[456] = "George"

print(my_data)

# remove
# my_data.pop(201)
# del my_data[201]

pair = my_data.popitem()
print(pair)
print(my_data)

# my_data.clear()
# del my_data

# More of Dictionary Methods
covid_cases = {}.fromkeys(["active", "total", "recovered"], 0)
print(covid_cases, type(covid_cases))

# Iterate
for item in covid_cases.items():
    # print(item, type(item))
    print(item[0], item[1])

keys = sorted(list(covid_cases.keys()))
print(keys)

# Dictionary Comprehensions
# data = {x: x**2 for x in range(1, 6)}
data = {x: x**2 for x in range(1, 21) if x%2==0}
print(data)

# Membership Testing | Only for keys
print(2 in data)
print(3 not in data)

print(all(data))
print(len(data))
print(any(data))
print(sorted(data))