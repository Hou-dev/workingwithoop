# With your knowledge of the concepts of aliasing, mutation, and cloning, fix this program so that the original list is not mutated. (Only modify the body of the functions).

a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
    
def remove_elem(data, target):
    data_new = data.copy()
    for item in data:
        if item == target:
            data_new.remove(target)
    return data_new
    
def get_product(data):
    total = 1
    for i in range(len(data)):
        total *= data.copy().pop()
    return total
    
remove_elem(c, 3)
print(get_product(b))
print(a)