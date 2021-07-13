# __name__ -> gives the name of python module i.e. the name of file
# BUT, if we are executing a module so name becomes main -> i.e. it is the main file which we are executing
# import S2Functions1 -> for this name will be S2Functions1
print("__name__ in S2Functions2.py is:", __name__) # for this name will be __main__

# def main():
#     print("Do all your jobs here")
#     print("All of the Jobs are in Execution")
#
# if __name__ == '__main__':
#     main()

def any_name_for_main():
    print("Do all your jobs here")
    print("All of the Jobs are in Execution")

if __name__ == '__main__':
    any_name_for_main()