# module 2 -- for importing 
print("File two __name__ is set to : {}".format(__name__))

#function3
def function_3():
    print("function 3 is executed")

def function_4() :
    print("function 4 is executed")

if __name__  == "__main__" : 
    print("File two excuted when ran directly")
    function_3()
else :
    print("File two executed when imported")
    function_4() 