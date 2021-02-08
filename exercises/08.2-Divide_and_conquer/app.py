list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]

#Your code here:

def merge_two_list(item):
    all_numbers = []
    odd_numbers = []
    even_numbers = []

    for i in list_of_numbers:
        if (i % 2) == 0:
            even_numbers.append(i)
        if (i % 2) != 0:
            odd_numbers.append(i)

    all_numbers=[odd_numbers]+[even_numbers]

    return all_numbers

print(merge_two_list(list_of_numbers))

