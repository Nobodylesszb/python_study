class  Solution(object):
     def uniqueMorseRepresentations(self, words):
         map_=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
         res = set()
         for word in words:
             val = ""
             for s in word:
                 val += map_[ord(s)-ord('a')]
             res.add(val) # 去除重复的
         return len(res)