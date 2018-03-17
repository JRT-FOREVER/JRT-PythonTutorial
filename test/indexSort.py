def index_sort(seq):
    seq = enumerate(seq)  # 返回列表的索引-值对
    seq_index = []
    seq_value = []
    for i, j in seq:
        seq_index.append(i)
        seq_value.append(j)
    return sorted(seq_index, key=lambda x:seq_value[x])


if __name__ == '__main__':
    print(index_sort((1, -2, 3, 99, 0, 22)))
