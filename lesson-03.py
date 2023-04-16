"""
Lesson: Python Functions (Methods) and Packages
Author: Olouge E.E
"""


def square(number):
    result = number**2  # result and number are local variables
    return result


# result = square(10)  # this result is a global variable

# print(result)


def cube(num):
    return num**3


def say_hello(name):
    return "Hello "+name


def calculate_bmi(h, w):
    '''This function calculates the BMI of an individual and return the results given the height and weight'''

    bmi = w/(h**2)
    return bmi


height = 1.7
weight = 75

my_bmi = calculate_bmi(height, weight)

#print(my_bmi)

# ?calculate_bmi()


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def do_it_again(item_list):
    for item in item_list:
        print(item**2)


# do_it_again(items)


def example_a():
    print('example_a is running')
    print('returning value "a"')
    return 'a'


# r = example_a()


# print(r)

def example_b():
    print('example_b is running')
    print('exiting without returning a value')

    r = example_a()

    print(r)


example_b()



