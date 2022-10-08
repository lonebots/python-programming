# yeid function module for finding cube of a number 

from operator import truediv
from tkinter.tix import Tree


def nextCube() : 
    i = 1

    #infinite loop to generate cube 
    while True :
        yield i**3
        # to get next number 
        i += 1