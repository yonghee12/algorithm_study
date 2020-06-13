alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

array = list(input())

result = ''
index = -1

for letter in array:
    if letter != " ":
        index = alphabets.index(letter)
        result += alphabets[index-3]    
    else:
        result += " "

print(result)