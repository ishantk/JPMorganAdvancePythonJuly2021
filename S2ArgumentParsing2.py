import argparse

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

ap = argparse.ArgumentParser()

ap.add_argument("-o", "--operation", required=True, help="this is file operation read or write")
ap.add_argument("-f", "--filename", required=True, help="this is file name eg logs.csv")
args = vars(ap.parse_args())

print(args)

if args['operation'] == "read":
    read_from_log_file(args['filename'])
else:
    write_log_into_file(args['filename'])

# We can also work on various libraries to cread CLI Apps
# click is one of the famous -> https://pypi.org/project/click8/