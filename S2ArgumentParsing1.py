import getopt
import sys
# Argument Parsing
# Its a way how our python program will read the arguments supplied to it on command line
# 1. sys.argv
# 2. getopt
# 3. argparse


def write_log_into_file(filename):
    log = {
        "time": "22:17",
        "date": "2021/7/12",
        "message": "device is running fine"
    }

    log_to_write = "{time}, {date}, {message}\n".format_map(log)

    file = open(filename, "a")
    file.write(log_to_write)
    print("Log Written")

def read_from_log_file(filename):
    file = open(filename, "r")
    contents = file.read()
    print(contents)

def main():

    argv = sys.argv[1:]

    print("Number of Arguments {}".format(len(sys.argv)))
    print("Arguments: {}".format(sys.argv))

    try:

        opts, args = getopt.getopt(argv, 'o:f:', ['operation=', 'filename='])

        print(opts)

        if len(opts) == 0 and len(opts) > 2:
            print("USAGE: S2ArgumentParsing1.py -o <operation> -f <filename>")
        else:
            idx = 0
            operation = ""
            filename = ""
            for opt in opts:
                if idx == 0:
                    operation = opt[1]
                else:
                    filename = opt[1]
                idx += 1

            print(operation, filename)

            if operation == "read":
                read_from_log_file(filename)
            else:
                write_log_into_file(filename)
    except:
        print("USAGE: S2ArgumentParsing1.py -o1 <operation> -o2 <filename>")
if __name__ == '__main__':
    main()