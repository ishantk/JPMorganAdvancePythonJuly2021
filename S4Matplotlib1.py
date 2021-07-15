import matplotlib.pyplot as plt
import numpy as np

# Y = np.random.rand(100, 100)
# print(Y)

# plt.hist(Y)

# Y = np.random.randn(1000)
# plt.hist(Y, 100)
# plt.show()

X = [1, 2, 3]
Y = [80, 90, 70]

# plt.bar(X, Y)
# plt.barh(X, Y)

data = {
    'cricketer1': 25,
    'cricketer2': 125,
    'cricketer3': 205,
    'cricketer4': 50,
    'cricketer5': 49,
}

# for i, key in enumerate(data):
#     # plt.bar(i, data[key])
#     plt.bar(key, data[key])

plt.figure(figsize=(5, 5))
job_labels = ['C++', 'Java', 'Python']
job_numbers = [100, 200, 300]

plt.pie(job_numbers, labels=job_labels)

plt.show()