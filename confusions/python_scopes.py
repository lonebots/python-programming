# def concatenate(*args,**kwargs):
#     for val in args :
#         print(f"print testing {val}")
#     for val in kwargs.values():
#         print(f'hi this is {val}')


# concatenate(1,3,5,jishnu="suresh", iss="is", good="good")


def check_scope():

    def do_local():
        # this defines local function scope
        test = "local_test"

    def do_non_local():
        # nonlocal keyword is used to access the variable just outside the function scope
        nonlocal test
        test = "non_local_test"

    def do_global():
        # global access the 'global' variable, which is outside of all the local functions 
        global test 
        test = "global_test"

    test = "default_test"

    do_local()
    print("test value after running do_local() : ", test) # test = default_test

    do_non_local()
    print("test value after running do_non_local() : ", test) # test = non_local_test

    do_global() # if you didnot run this then the `test` value after main() will not be accessible.
    print("test value after running do_global() : ", test) # test = non_local_test
 

check_scope()
print("test value after running main :", test) # test = global_test
 