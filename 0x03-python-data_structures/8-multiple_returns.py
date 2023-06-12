#!/usr/bin/python3
def multiple_returns(sentence):
    topul = ()
    if len(sentence) == 0:
        topul = (0, None)
        return topul
    topul = (len(sentence), sentence[0])
    return topul
