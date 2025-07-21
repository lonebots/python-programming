"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the
    Rs come first,
    the Gs come second,
    and the Bs come last.

You can only swap elements of the array.

Do this in linear time and in-place.

['G', 'B', 'R', 'R', 'B', 'R', 'G']

to

['R', 'R', 'R', 'G', 'G', 'B', 'B'].

"""


class RGBHandler:
    rgb_index = [
        "R",
        "G",
        "B",
    ]  # bad approach since this look up take O(n) time - linear search if we use .index()

    order = {"R": 1, "G": 2, "B": 3}

    def __init__(self, rgb_array):
        self.__rgb_array = rgb_array

    @staticmethod
    def swap(array: list, index1: int, index2: int) -> None:
        array[index1], array[index2] = array[index2], array[index1]

    def reorder(self):
        rgb_array = self.__rgb_array

        # for index1, val1 in enumerate(rgb_array):
        #     for index2, val2 in enumerate(rgb_array[index1 + 1 :]):
        #         if self.order[val2] < self.order[val1]:
        #             self.swap(rgb_array, index1=index1, index2=index2)
        
        # o(n^2) solution
        for index1 in range(len(rgb_array)):
            for index2 in range(index1, len(rgb_array)):
                if self.order[rgb_array[index2]] < self.order[rgb_array[index1]]:
                    self.swap(rgb_array, index1, index2)

        return rgb_array
    
    @staticmethod
    def dutch_national_flag_sort(rgb_array: list) -> list:
        low = 0
        mid = 0
        high = len(rgb_array) - 1
        
        while mid <= high:
            if rgb_array[mid] == "R": # swap it with low
                RGBHandler.swap(rgb_array, mid, low)
                mid += 1
                low += 1
            elif rgb_array[mid] == "G":
                mid += 1
            else: # case `B`, swap with high
                RGBHandler.swap(rgb_array, mid, high)
                high -= 1
        
        return rgb_array

if __name__ == "__main__":

    rgb_array = ["G", "B", "R", "R", "B", "R", "G"]
    rgb_handler = RGBHandler(rgb_array=rgb_array)

    print(rgb_handler.reorder())
    
    print(rgb_handler.dutch_national_flag_sort(rgb_array= rgb_array))
