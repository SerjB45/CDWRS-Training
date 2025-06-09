# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
def move_zeros(lst: list):
    zero = lst.count(0)
    if zero > 0:
        lst = [i for i in lst if i != 0]
        lst += [0] * zero 
    return lst

def move_zeros_2(lst: list):
    base_len = len(lst)
    lst = [i for i in lst if i != 0]
    return lst + [0] * (base_len - len(lst))
    