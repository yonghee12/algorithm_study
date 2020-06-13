# 함수를 작성하시오.
# input으로 받은 스트링을 역순 스트링으로 만들어 출력하는 함수를 작성하시오.

# /Input/: "1234abcd"
# /Output/ : "dcba4321"

def reverse(string):
    result = ''
    for letter in string:
        result = letter + result
    return result

print(reverse('hello'))