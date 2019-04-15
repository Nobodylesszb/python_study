    # @return a string

def find_substr(str):
    res = []
    if len(str) < 1:
        return str
    else:
        for i in range(1,len(str)):
            for j in range(len(str)-i):
                substr = str[j:j+i]
                if str.count(substr) >=2:
                    res.append(substr)
        return res

s = 'banana'
print(find_substr(s))