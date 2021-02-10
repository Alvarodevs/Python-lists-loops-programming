my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
def average_result(item):
    num = 0
    for i in item:
        num = num + i
        result = num/len(item)
    return result 
print(average_result(my_list))