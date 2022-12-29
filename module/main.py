# main function

from operator import ne
from yield_next import nextCube
from next_square import nextSquare
from count_custom import count_custom

limit = 100

if __name__ == "__main__":
    count = 0
    string = "jishnu is jishnu and he is good jishnu then he is bad jishnu"
    word = "jishnu"

    for item in count_custom(string=string, word=word):
        count += 1
    print("total number of  {} in {} is : {}".format(word, string, count))


#     print("cubes :")
#     for num in nextCube() :
#         if num > limit :
#             break
#         else :
#             print(num)


#     print("squares : ")
#     for num in nextSquare() :
#         if num > limit :
#             break
#         else :
#             print(num)
