import getpass
import telnetlib

HOST = "https://localhost:8080/"
user = input("Enter User Name: ")
# password = getpass.getpass()
password = input("Enter Password: ")

tn = telnetlib.Telnet(HOST)

tn.read_until("Logging in..")
tn.write(user+"\n")

tn.read_until("Applying Password..")
tn.write(password+"\n")

tn.write("ls\n")
print(tn.read_all())

tn.write("ls-l\n")
print(tn.read_all())


