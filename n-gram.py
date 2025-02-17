n = int(input('Enter n: '))
string = input('String: ')
st = string.split()  # Splitting the string into words
ans = []

for word in st:
    if len(word) < n:
        continue  # Skip words that are smaller than n

    ans.append("$" + word[:n-1])  # Add the prefix n-gram with '$'
    
    for j in range(len(word) - n + 1):  # Iterate over valid n-grams
        ans.append(word[j:j+n])
    
    ans.append(word[-n+1:] + "$")  # Add the suffix n-gram with '$'

print(ans)
