def counting_index(input_line: str) -> list:
    user = input_line.split()
    lst = [-1] * len(user)
    dct = {}

    for i, el in enumerate(user):
        if el not in dct:
            dct[el] = i
        else:
            lst[i] = dct[el]
            dct[el] = i
    return lst
