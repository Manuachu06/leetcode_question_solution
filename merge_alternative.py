##https://leetcode.com/problems/merge-strings-alternately/description/

def mergeAlternately(self, word1: str, word2: str) -> str:

        A , B = len(word1) , len(word2)

        left , right = 0 , 0

        res = []

        word = 1
        while left < A and right < B :

            if word == 1:
                res.append(word1[left])
                left += 1
                word = 2
            else:
                res.append(word2[right])
                right += 1
                word = 1
            
        while left < A:
            res.append(word1[left])
            left += 1
        
        while right < B:
            res.append(word2[right])
            right += 1

        return ''.join(res)
