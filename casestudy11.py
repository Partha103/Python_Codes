def find_pairs(arr, sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                pairs.append((arr[i], arr[j]))
    return pairs

# example usage
arr = [5, 4, 6, 2, 3, 5]
sum = int(input("Enter the sum: "))
pairs = find_pairs(arr, sum)
for pair in pairs:
    print(pair[0], pair[1])
