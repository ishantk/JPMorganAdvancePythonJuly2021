import getpass

print("Register Yourself")
name = input("Enter Name: ")
email = input("Enter Email: ")
# password = input("Enter Password: ")
password = getpass.getpass("Enter Password: ")

print("Details are: {}, {}, {}".format(name, email, password))
