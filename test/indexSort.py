def index_sort1(seq):
    seq = enumerate(seq)  # 返回列表的索引-值对
    seq_index = []
    seq_value = []
    for i, j in seq:
        seq_index.append(i)
        seq_value.append(j)
    return sorted(seq_index, key=lambda x: seq_value[x])



def index_sort2(seq):
    seq = enumerate(seq)
    seq_sorted = sorted(seq, key=lambda x: x[1])
    dict_sorted = dict(seq_sorted)
    dict_key = dict_sorted.keys()
    dict_value = dict_sorted.values()
    return dict_key, dict_value
if __name__ == '__main__':
    print(index_sort1((1, -2, 3, 99, 0, 22)))
    # print(index_sort2((1, -2, 3, 99, 0, 22)))
    a, b = index_sort2((1, -2, 3, 99, 0, 22))
    print(a)
    print(b)
