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

print("WELCOME TO FOODIE APP")
print("----------------------")
print("WE HAVE {} RESTAURANTS".format(len(restaurants)))
print("----------------------")
print("Listing All....")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~")
#               0, 5
for i in range(len(restaurants)):
    print(restaurants[i]["title"])
    print("time:", restaurants[i]["timeToDeliver"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~")


while True:
    print("^^^^^^^^^^^^^^^^^^")
    print("1. To Apply Filters")
    print("2. To Search a Restaurant")
    print("3. To Sort on the basis of time to deliver")
    print("^^^^^^^^^^^^^^^^^^")

    option = int(input("Enter a Choice: "))
    print("option is:", option)

    if option == 1:
        # print("Apply Filter")
        filter = input("Enter the Filter from {}: ".format(list(restaurant1.keys())))
        if filter == "cuisines":
            cuisine = input("Which cuisine are you looking for? ")
            for restaurant in restaurants:
                cuisines = restaurant['cuisines'].split(",")
                if cuisine in cuisines:
                    print(restaurant['title'], " | ", restaurant[filter])
        else:
            for restaurant in restaurants:
                print(restaurant['title'], " | ", restaurant[filter])

    elif option == 2:
       search = input("Enter Restaurant to search: ")
       for restaurant in restaurants:
           if restaurant['title'] == search:
                print(restaurant)

    elif option == 3:
        # print("Apply Sort")

        filter = input("Enter the Filter from [pricePerPerson, timeToDeliver, ratings]: ")
        n = len(restaurants)

        for i in range(0, n): # 0, 1, 2, 3, 4
            for j in range(0, n-i-1):
                if restaurants[j][filter] > restaurants[j+1][filter]:
                    restaurants[j], restaurants[j+1] = restaurants[j+1], restaurants[j]

        for restaurant in restaurants:
            print(restaurant['title'], restaurant['cuisines'], restaurant[filter])

    else:
        print("Option Invalid")

    choice = input("Do you wish to continue(yes/no): ")
    if choice == "no":
        break
