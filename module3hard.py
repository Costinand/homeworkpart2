data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

summa = []


def test_list(i):
    for l in i:
        if isinstance(l, int):
            summa.append(l)
        if isinstance(l, str):
            summa.append(len(l))
        if isinstance(l, dict):
            i = l
            test_dict(l)
        if isinstance(l, tuple):
            test_list(l)
        if isinstance(l, set):
            test_list(l)
        if isinstance(l, list):
            test_list(l)


def test_dict(i):
    for d in i:
        summa.append(i[d])
    for key in i:
        summa.append(len(key))


def summa_arg(data):
    print(sum(summa))


for i in data_structure:
    if isinstance(i, int):
        summa.append(i)
    if isinstance(i, str):
        summa.append(len(i))
    if isinstance(i, list):
        test_list(i)
    if isinstance(i, tuple):
        test_list(i)
    if isinstance(i, dict):
        test_dict(i)

print(summa)

summa_arg(data_structure)
