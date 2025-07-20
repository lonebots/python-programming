"""
Trie (aka prefix tree)
  - tree like data structure
  - used for storing and retrieving string efficiently
"""


class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.__root = Node()

    def make(self, words: list) -> Node:
        for word in words:
            self.insert(word=word)

    def insert(self, word):
        temp_root = self.__root
        for letter in word:
            if letter not in temp_root.children:
                temp_root.children[letter] = Node()
            temp_root = temp_root.children[letter]
        temp_root.is_end = True

    def in_trie(self, word: str) -> bool:
        temp_root = self.__root

        if not temp_root.children:
            return False

        for letter in word:
            if letter not in temp_root.children:
                return False
            temp_root = temp_root.children[letter]

        return temp_root.is_end

    def __get_all(self, node: Node, key: str, key_list: list) -> list:
        if node.is_end:
            key_list.append(key)

        for letter in node.children.keys():
            self.__get_all(node.children[letter], key + letter, key_list)

    def search_prefix(self, key: str) -> list:
        key_list = []

        temp_root = self.__root
        for letter in key:
            if letter not in temp_root.children:
                return key_list
            temp_root = temp_root.children[letter]

        if not temp_root.children:
            return key_list

        self.__get_all(temp_root, key=key, key_list=key_list)
        return key_list


# run as independent file only
if __name__ == "__main__":
    word_list = ["KEY", "CAT", "BAT", "BALL", "CATTLE", "BALLOON"]

    trie = Trie()
    trie.make(words=word_list)

    SEARCH_KEY = "BAL"

    print(trie.search_prefix(SEARCH_KEY))

    print("in trie word BAL : ", trie.in_trie("BAL"))
