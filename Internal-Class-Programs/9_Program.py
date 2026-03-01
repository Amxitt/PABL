def union_arrays(a, b):
    s = set()

    for i in a:
        s.add(i)

    for i in b:
        s.add(i)

    return list(s)


a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

result = union_arrays(a, b)
print(result)
