#!/udr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = list(map(lambda x: x[0], my_list))
    res1 = list(map(lambda x: x[1], my_list))
    sum1 = sum(map(lambda x, y: x * y, res, res1))
    sum2 = sum(res1)
    return sum1/sum2
