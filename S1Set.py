johns_followers = {"jennie", "jack", "mark", "harry", "fionna", "jack"}
fionnas_followers = {"mark", "jennie", "ed", "george", "lee", "kia", "lee"}

print(johns_followers)
print(fionnas_followers)

# Nested Set
# my_data = {"John", (98, 78, 88), ("john@example.com", "john@abc.edu")}
numbers = [98, 78, 88, 97, 88, 78]
set_of_numbers = set(numbers)
print(set_of_numbers)

# Empty Set
# my_data = {} # empty dictionary
my_data = set() # empty set
my_data.add(20)
my_data.add(10)
my_data.add(20)

print(my_data)
# my_data.update({30, 40, 50, 10, 20})
my_data.update([90, 87, 55], {11, 33, 44})
print(my_data)

# my_data.discard(444) # no error genertion
# my_data.remove(444) # generates a key error if data not found
# print(my_data)

print(my_data.pop())
print(my_data)

# my_data.clear()
# print(my_data)

print(44 in my_data)
print(444 not in my_data)

for element in my_data:
    print(element)

# ERROR
# new_data = my_data + {-1, -2, -3}
# print(new_data)

# ERROR
# new_data = my_data * 3
# print(new_data)

johns_followers = {"jennie", "jack", "mark", "harry", "fionna", "jack"}
fionnas_followers = {"mark", "jennie", "ed", "george", "lee", "kia", "lee"}
mark_followers = {"jack", "fionna"}

print(johns_followers)
print(fionnas_followers)
print(mark_followers)

print(johns_followers.issuperset(mark_followers))
print(mark_followers.issubset(johns_followers))

# all_followers = johns_followers.union(fionnas_followers)
all_followers = johns_followers | fionnas_followers
print(all_followers)

# mutual_followers = johns_followers.intersection(fionnas_followers)
mutual_followers = johns_followers & fionnas_followers
print("mutual_followers:", mutual_followers)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# C = A-B
# C = A.difference(B)
# C = A ^ B
C = A.symmetric_difference(B)
print(C)

# Explore few more -> All, any etc..

# Frozen Sets -> IMMUTABLE :)
data = [1, 2, 3, 4, 5]
f_set = frozenset(data)
print("f_set is:", f_set, type(f_set))
# f_set.add(10)
