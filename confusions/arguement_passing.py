# passing arguments to functions 

'''
method 1 : normal arguments passing 

method 2 : keyword arguments passing

method 3 : default arguments

method 4 : arbitrary arguments passing
    4.2  : arbitrary positional arguments
    4.2  : arbitrary keyword arguments 

'''

# method 1 
def greeting(name):
    print (f"hello {name} !")

# method 2 
def say_hello(name,place) :
    print(f"hello {name}, welcome to {place} and nice to meet you!")

# method 3 
def say_age(name, age = 10) :
    print(f"My name is {name} and I am {age} years old")

# method 4.1
def calculate_sum(*args) :
    sum_ = 0
    for val in args :
        sum_ += val 
    print("sum :",sum_) 

# method 4.2
def concatenate_string(**kwargs) :
    result = ""
    
    for val in kwargs.values() :
        result += f" {val}"
    print(result)


# function calls 
greeting('Ram')

say_hello(place='India', name='Ram')

say_age(name="Ram")

calculate_sum(1,2,3,4,5)

concatenate_string(name="Ram", age = 10, place = "India")

