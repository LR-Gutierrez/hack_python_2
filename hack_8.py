"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    new = []
    for index, value in reversed(list(enumerate(result))):
        if len(result) == 4 or len(result) == 2:
            new.append(str(index + 1))
        else:
            new.append(value + "-" + str(index + 1))
    return new