arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
oddnumber = []

def sum_odd_numbers(item):
    
    for i in range(0,len(arr)):
        if (arr[i] % 2) != 0:
            oddnumber.append(arr[i])
    return sum(oddnumber)
    
print(sum_odd_numbers(arr))