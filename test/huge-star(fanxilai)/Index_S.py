def index_sort(l):
    o = []
    m = list(zip(l, range(3)))
    m.sort()
    for (i, value) in m:
        o.append(value)
    return o

print(index_sort([12,56,33,78]))
