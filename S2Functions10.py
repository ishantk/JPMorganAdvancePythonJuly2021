restaurant1 = {
    "title": "McDonalds",
    "pricePerPerson": 150,
    "timeToDeliver": 20,
    "ratings": 4.5,
    "cuisines": "burger,fries,icecream"
}

restaurant2 = {
    "title": "Pizza Hut",
    "pricePerPerson": 350,
    "timeToDeliver": 25,
    "ratings": 4.7,
    "cuisines": "pizza,fries,sandwich"
}

restaurant3 = {
    "title": "Dominos",
    "pricePerPerson": 250,
    "timeToDeliver": 15,
    "ratings": 4.9,
    "cuisines": "pizza,fries,icecream,breads"
}

restaurant4 = {
    "title": "Table By Basant",
    "pricePerPerson": 200,
    "timeToDeliver": 30,
    "ratings": 4.2,
    "cuisines": "indian,veg,chinese,burger,icecream"
}

restaurant5 = {
    "title": "Johns Cafe",
    "pricePerPerson": 150,
    "timeToDeliver": 10,
    "ratings": 3.5,
    "cuisines": "coffe,tea,icecream"
}

# List of Restaurants -> Nested List
restaurants = [restaurant1, restaurant2, restaurant3, restaurant4, restaurant5]

# write a lambda

# filter restaurants whose delivery time is between 10 and 15
# filter restaurants with ratings > 4
get_filtered_restaurants = lambda restaurant: restaurant['timeToDeliver'] >= 10 and restaurant['timeToDeliver'] <= 15
result = list(filter(get_filtered_restaurants, restaurants))
print(result)

print("~~~~~~~~~~~")

get_filtered_restaurants = lambda restaurant: restaurant['ratings'] > 4
result = list(filter(get_filtered_restaurants, restaurants))
print(result)

def add(num1, num2):
    sum = num1 + num2
    print(sum)

add(10, 20)

import dis
print(dis.dis(add))
