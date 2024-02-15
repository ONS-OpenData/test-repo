import os

def my_function():
    print("I am 'my_function' from the app in the test repo")
    return 

def get_working_directory():
    return os.getcwd()


if __name__ == '__main__':
    print("Running my_function()")
    my_function()

    print("Running get_working_directory")
    wd = get_working_directory()
    print(wd)