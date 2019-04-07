class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set('aeiouAEIOU')
        res = S.split()
        r = []
        for index, word in enumerate(res,1):
            if word[0] not in vowel:
                word = word[1:] + word[0] + 'ma' + 'a' * index
                r.append(word)
            else:
                word = word + 'ma' + 'a' * index
                r.append(word)
        return ' '.join(r)

            