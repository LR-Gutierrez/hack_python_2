"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    new =[]
    if result == []:
        new.append("0")
    else:
        for index, value in enumerate(result):
            if index % 2 == 0:
                new.append(str(index + 1))
            else:
                new.append("-")
    return new
