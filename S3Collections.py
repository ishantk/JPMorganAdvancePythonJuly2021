"""
    Collections Module in Python
"""

# Regular Tuple
numbers = (10, 20, 30, 40, 50, 10, 30, 70, 40)
print(numbers[0])
print(numbers[3])

# namedtuple
from collections import namedtuple

student = namedtuple('student', 'roll name age marks')

john = student(roll=101, name="John Watson", age=20, marks=80)
fionna = student(roll=201, name="Fionna Flynn", age=21, marks=88)

print(student)
print(john)
print(fionna)

print(john.roll, john.name)
print(fionna.roll, fionna.name)

# Counter
from collections import Counter
message = "this is a good day. this seems to be a rough day"
c = Counter(message)
print(c, type(c))

c = Counter(numbers)
print(c)

words = message.split()
c = Counter(words)
print(c)

# Default Dictionary
employees = {101: "John", 201: "Fionna"}
# print(employees[301])

from collections import defaultdict
employees = defaultdict(object)
print(employees[301])

# OrderedDict
dishes = {'noodles': 300, 'burger': 100, 'fries': 80, 'coke': 50}
print(dishes)


from collections import OrderedDict
# dictionary = OrderedDict(sorted(dishes.items(), key=lambda k: k[0]))  # 0 -> keys
# dictionary = OrderedDict(sorted(dishes.items(), key=lambda k: k[1]))    # 1 -> value
dictionary = OrderedDict(sorted(dishes.items(), key=lambda k: len(k[0])))# length of key
print(dictionary)

from collections import deque
deq = deque([10, 11, 12, 13, 14, 20, 16])
deq.append(100)
deq.appendleft(12)

print(deq)