def make_dict(char, char_list):
    if len(char) == 5:
        return [""]
    result = []
    for element in char_list:
        temp = char + element
        child_char = make_dict(temp, char_list)
        if len(child_char) == 1:
            result += [temp]
        else:
            result += [temp] + child_char
    return result

def solution(word):
    '''
    AA = A + A,
    AAAAE = AAAA + E,
    AAAA = AAA + A
    AAA = AA + A
    AA = A
    '''
    start_char = word[0]
    char_list = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for char in char_list:
        if ord(char) > ord(start_char):
            break
        dictionary += [char] + make_dict(char, char_list)
    answer = dictionary.index(word) + 1
    return answer

examples = [
    "AAAAE",
    "AAAE",
    "I",
    "EIO"
]

for example in examples:
    print(solution(example))