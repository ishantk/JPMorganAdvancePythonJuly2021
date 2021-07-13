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