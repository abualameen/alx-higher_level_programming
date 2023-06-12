#!/usr/bin/python3
def multiple_returns(sentence):
    topul = ()
    if sentence is None:
        return topul
    topul = (len(sentence), sentence[0])
    return topul
