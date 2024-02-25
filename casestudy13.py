def tuple_to_dict(tuple, keys):
    dict_list = []
    for tup in tuple:
        dict = {}
        for i in range(len(keys)):
            dict[keys[i]] = tup[i]
        dict_list.append(dict)
    return dict_list

# example usage
tuple = ((1, 'X'), (2, 3))
keys = ['key', 'value']
dict_list = tuple_to_dict(tuple, keys)
print(dict_list)
