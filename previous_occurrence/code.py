def find_previous_occurrence(input_line: str) -> list:
    dct = {}
    lst = []
    converted_input = list(input_line.split())

    for word in converted_input:
        if word not in dct:
            dct[word] = 0
            lst.append(dct[word])
        else:
            dct[word] += 1
            lst.append(dct[word])
    return lst
