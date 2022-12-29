# python module 1


#importing a particular function from file 2
from file_two import function_4


print("File one __name__ is set to : {}".format(__name__))

#function1
def function_1():
    print("function 1 is executed")

#function2
def function_2():
    print("function 2 is executed")

if __name__ == "__main__" :
    print("File one executed when ran directly")
    function_2()

    #excuted function from imported file
    #file_two.function_3()
    # function_4()
else :
    print("File one executed when imported")