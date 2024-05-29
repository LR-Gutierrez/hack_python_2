"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    new = []
    index = 0
    if not result:
        new.append("0")
    else:
        while index < len(result):
            if len(result) < 4:
                if result[index] == 0:
                    new.append(result[0])
            else:
                if index % 2 == 0:
                    new.append(str(index + 1))
                else:
                    new.append((index + 1))
            index += 1
    return new