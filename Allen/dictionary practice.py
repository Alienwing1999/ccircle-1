import operator

def sort_by_key(dict):
    return sorted(dict.items())
def reverse_sort_by_key(dict):
    return sorted(dict.items(), reverse = True)
def sort_by_value(dict):
    return sorted(dict.items(), key = operator.itemgetter(1))


d = {
    1: 'hi',
    3: 'roses',
    2:'bye',
}

print(reverse_sort_by_key(d))

print(sort_by_value(d))