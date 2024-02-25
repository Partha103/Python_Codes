def are_binary_anagrams(a, b):
    binary_a = bin(a)[2:]  # convert a to binary string
    binary_b = bin(b)[2:]  # convert b to binary string
    if len(binary_a) != len(binary_b):
        return False  # if lengths are not equal, they cannot be anagrams
    freq = {}  # create empty dictionary to store frequencies of 0's and 1's
    for bit in binary_a:
        freq[bit] = freq.get(bit, 0) + 1  # increment frequency count for bit
    for bit in binary_b:
        if bit not in freq:
            return False  # if bit not in freq, they cannot be anagrams
        freq[bit] -= 1  # decrement frequency count for bit
        if freq[bit] == 0:
            del freq[bit]  # remove key if frequency count is 0
    return len(freq) == 0  # return True if all frequency counts are 0

# example usage
a = 4
b = 4
if are_binary_anagrams(a, b):
    print("Yes")
else:
    print("No")
