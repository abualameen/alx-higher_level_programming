#!/udr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = list(map(lambda x: x[0], my_list))
    weight = list(map(lambda x: x[1], my_list))
    score_sum = sum(map(lambda x, y: x * y, score, weight))
    weight_sum = sum(weight)
    return score_sum/weight_sum
