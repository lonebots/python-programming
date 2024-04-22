'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.

 

Constraints:

    1 <= deadends.length <= 500
    deadends[i].length == 4
    target.length == 4
    target will not be in the list deadends.
    target and deadends[i] consist of digits only.

'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # next slot map
        next_slot = {
            "0" : "1",
            "1" : "2",
            "2" : "3",
            "3" : "4",
            "4" : "5",
            "5" : "6",
            "6" : "7",
            "7" : "8",
            "8" : "9",
            "9" : "0"
        }

        # previous slot map
        prev_slot = {
            "0" : "9",
            "9" : "8",
            "8" : "7",
            "7" : "6",
            "6" : "5",
            "5" : "4",
            "4" : "3",
            "3" : "2",
            "2" : "1",
            "1" : "0"
        }


        # set to store visited and dead-ends
        visited_combinations = set(deadends)

        # queue for storing pending combinations
        pending_combinations = deque()

        # count number of wheel turns made
        turns = 0 

        # edge case, starting itself if locked or deadend state 
        if "0000" in visited_combinations : 
            return -1 

        # initialize pending combinations, it starts with "0000"
        pending_combinations.append("0000")
        visited_combinations.add("0000")


        while pending_combinations : 
            curr_level_nodes_count = len(pending_combinations) 

            for _ in range(curr_level_nodes_count) : 

                current_combination = pending_combinations.popleft()

                # check if target has reached 
                if current_combination == target : 
                    return turns 

                # explore possible combinations 
                for wheel in range(4) : 
                    # generate new combinations 
                    new_combination = list(current_combination) 
                    new_combination[wheel] = next_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)


                    # logic to add to visited 
                    if new_combination_str not in visited_combinations : 
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)

                    # generate new combinations from previous map
                    new_combination = list(current_combination)
                    new_combination[wheel] = prev_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)

                    if new_combination_str not in visited_combinations :
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)

            turns += 1 

        return -1