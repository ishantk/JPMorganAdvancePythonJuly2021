import requests # we need to install it
import json     # built in module

# for Loop
# while Loop

product_prices = [1567, 4500, 2188, 6754, 9876]
# print(list(range(0, 11, 2)))

# Indexed Loop
for i in range(0, len(product_prices)):
    if product_prices[i] > 5000:
        product_prices[i] -= 0.5 * product_prices[i]
# else:
print(product_prices)


# Read Only Loop | For Each Loop
for price in product_prices:
    print(price)
else:
    print("Thank You")


students = {101: "John", 201: "Jennie", 301: "Fionna"}
roll_number = int(input("Enter Roll Number to be Searched: "))
for key in students:
    # print(key, students[key])
    if key == roll_number:
        print("STUDENT", students[key], "FOUND")
        break
else:
    print("No Such Student Found with", roll_number)

api_key = "31c21508fad64116acd229c10ac11e84"
url = "https://newsapi.org/v2/everything?q=tesla&from=2021-06-13&sortBy=publishedAt&apiKey="+api_key
response = requests.get(url)
print(response, type(response))
print(response.text, type(response.text))
data = json.loads(response.text)
print(data)
print(type(data))

print("TOTAL RESULTS", data['totalResults'])
articles = data['articles']

# for article in articles:
#     print(article['title'])
#     print(article['author'])
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# for i in range(len(articles)):
#     print(articles[i]['title'])
#     print(articles[i]['author'])
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
#     if i == 5:
#         break

idx = 0
while idx <= 5:
    print(articles[idx]['title'])
    print(articles[idx]['author'])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    idx += 1

# pass -> as a developed i may write the logic later| we will write the functionality sometime later :)
for i in range(1, 11):
    pass

for floor in range(1, 11):

    if floor < 5:
        continue

    print("Floor #", floor)

    if floor == 5:
        break