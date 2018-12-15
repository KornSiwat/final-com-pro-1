def permuted_str(n):
    """Return a string that represents all length 3 permuted strings constructed from n natural numbers (n is greater than or equal to one). The order of each permuted string must be observed.

    >>> permuted_str(1)
    '111 '

    >>> permuted_str(2)
    '111 112 121 122 211 212 221 222 '

    >>> permuted_str(3)
    '111 112 113 121 122 123 131 132 133 211 212 213 221 222 223 231 232 233 311 312 313 321 322 323 331 332 333 '

    >>> permuted_str(4)
    '111 112 113 114 121 122 123 124 131 132 133 134 141 142 143 144 211 212 213 214 221 222 223 224 231 232 233 234 241 242 243 244 311 312 313 314 321 322 323 324 331 332 333 334 341 342 343 344 411 412 413 414 421 422 423 424 431 432 433 434 441 442 443 444 '
    
    """
    pstr = ''
    first = range(1,n+1)
    second = range(1,n+1)
    third = range(1,n+1)
    for i in first:
        for j in second:
            for k in third:
                pstr += f'{str(i)}{str(j)}{str(k)} '
    return pstr
    

# Example that shows how to sort a list of list
def take_first(elem):
    return elem[0]

# random list
random = [[2, 2], [3, 4], [4, 1], [1, 3]]

# sort list with key
random.sort(key=take_first)

# print list
print('Sorted list:', random)

def flatten(list_input):
    result = []
    for i in list_input:
        for j in i:
            result.append(j)
    return(result)

def count_int_element(int_array_2d):
    """ Return a list of [element, frequency] where element is a member of int_array_2d and frequency is the number of times that element occurs in int_array_2d. The returned list must be sorted by element. See the example of how to sort a list of list above

    >>> count_int_element([[3, 3, 2], [1, 1, 0], [1, 3, 1]])
    [[0, 1], [1, 4], [2, 1], [3, 3]]

    >>> count_int_element([[2, 6, 2], [3, 3, 5], [4, 6, 1]])
    [[1, 1], [2, 2], [3, 2], [4, 1], [5, 1], [6, 2]]

    >>> count_int_element([[3, 4, 4, 0, 0, 3], [4, 0, 4, 4, 2, 1], [3, 0, 1, 4, 4, 4], [2, 0, 4, 3, 2, 2], [4, 3, 2, 1, 2, 3]])
    [[0, 5], [1, 3], [2, 6], [3, 6], [4, 10]]

    """
    l = []
    l = flatten(int_array_2d)
    histogram = {}
    for element in l:
        if element not in histogram:
            histogram[element] = 1
        else:
            histogram[element] += 1
    l = []
    for key in histogram:
        l.append([key,histogram[key]])
    l.sort(key=lambda x: x[0])
    return l
