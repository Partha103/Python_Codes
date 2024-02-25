def add_commas(num):
    num_str = str(num)
    result = ''
    for i in range(len(num_str)):
        if i != 0 and (len(num_str) - i) % 3 == 0:
            result += ','
        result += num_str[i]
    return result

# example usage
num = 1000000
result_str = add_commas(num)
print(result_str)
