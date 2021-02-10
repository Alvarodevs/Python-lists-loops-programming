names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name
#Your code go here:
list_of_names = list(map(prepender, names))
print(list_of_names)