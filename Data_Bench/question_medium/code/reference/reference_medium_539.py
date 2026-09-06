class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longest_word = ''
        for word in d:
            i , j =0 , 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            if i == len(word):
                if len(longest_word) < len(word):
                    longest_word = word
                elif len(word) == len(longest_word):
                    longest_word = min(longest_word , word)
        return longest_word

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ''
        for cand in d:
            if self.find(s, cand) and (len(cand) > len(res) or (len(cand) == len(res) and cand < res)):
                res = cand
        return res
    

    def find(self , s ,d):
        i , j = 0 , 0
        while i < len(s) and j < len(d):
            if s[i] == d[j]:
                i+=1
                j+=1
            else:
                i+=1
        return j == len(d)