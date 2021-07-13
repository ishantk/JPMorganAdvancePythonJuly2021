# Argument Parsing
# Its a way how our python program will read the arguments supplied to it on command line
# 1. sys.argv
# 2. getopt
# 3. argparse

import sys

def write_log_into_file():
    log = {
        "time": "21:05",
        "date": "2021/7/12",
        "message": "device is blinking green"
    }

    log_to_write = "{time}, {date}, {message}\n".format_map(log)

    file = open("new-logs.csv", "a")
    file.write(log_to_write)
    print("Log Written")

def read_from_log_file():
    file = open("new-logs.csv", "r")
    contents = file.read()
    print(contents)

def main():

    print("Number of Arguments {}".format(len(sys.argv)))
    print("Arguments: {}".format(sys.argv))

    try:
        if sys.argv[1] == "write":
            write_log_into_file()
        elif sys.argv[1] == "read":
            read_from_log_file()
    except:
        print("Something Went Wrong. The kind of expecetd arguments did not found")


if __name__ == '__main__':
    main()