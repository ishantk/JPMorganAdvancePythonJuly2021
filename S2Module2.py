import one
from one import mylogs

# import one.mylogs
# from one.mylogs import read_from_log_file
# import one.mylogs as log

print("[S2Module2] name of module is: ", __name__)
print("Hello")

# print(one.students)

# one.mylogs.read_from_log_file("logs.csv")

mylogs.read_from_log_file("logs.csv")