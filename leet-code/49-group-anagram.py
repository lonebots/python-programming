class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = dict()
        answers = []

        for word in strs :
            nword = ''.join(sorted(list(word)))
            if nword in dict_ :
                dict_[nword].append(word)
            else :
                dict_[nword] = [word]

        # for key in dict_.keys() :
        #     answers.append(dict_[key])

        # return answers
        return dict_.values()