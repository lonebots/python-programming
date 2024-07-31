'''
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

    For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

 

Example 1:

Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.

Example 2:

Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4

 

Constraints:

    1 <= books.length <= 1000
    1 <= thicknessi <= shelfWidth <= 1000
    1 <= heighti <= 1000

'''


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # cache 
        memo = [[ 0 for _ in range(shelfWidth + 1)] for _ in range(len(books))]
        return self._dpHelper(books, shelfWidth, memo, 0, shelfWidth, 0)

    def _dpHelper(self, books: List[List[int]], shelf_width: int, memo: List[List[int]], i: int, remaining_shelf_width: int, max_height: int) -> int:
        current_book = books[i]

        # update max height 
        max_height_updated = max(max_height, current_book[1])

        # handle last book case (either current row or new row above)
        if i == len(books) - 1:
            # store in current shelf 
            if remaining_shelf_width >= current_book[0]:
                return max_height_updated
            
            # new row 
            return max_height + current_book[1]
        
        # return cached value
        if memo[i][remaining_shelf_width] != 0: 
            return memo[i][remaining_shelf_width]
        else:
            # calculate the minimum possible height 

            # case 1 : new row 
            option_1_height = max_height + self._dpHelper(books, shelf_width, memo, i + 1, shelf_width - current_book[0], current_book[1])

            # case 2 : same row
            if remaining_shelf_width >= current_book[0]:
                option_2_height = self._dpHelper(books, shelf_width, memo, i + 1, remaining_shelf_width - current_book[0], max_height_updated)

                # store in cache 
                memo[i][remaining_shelf_width] = min(option_1_height, option_2_height)

                return memo[i][remaining_shelf_width]
        
            memo[i][remaining_shelf_width] = option_1_height
            return memo[i][remaining_shelf_width]