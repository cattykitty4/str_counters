def find_less_in_alph_order(input_string: str) -> str:
    fragmented_string = input_string.split()
    dct = {}
    lst = []
    max_number = 0

    for el in fragmented_string:
        if el not in dct:
            dct[el] = 1
        else:
            dct[el] += 1

    for value in dct:
        if dct[value] >= max_number:
            max_number = dct[value]
            lst.append(value)
    lst.sort()
    return lst[0]
