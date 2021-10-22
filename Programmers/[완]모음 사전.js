function make_dict(char, char_arr) {
    if (char.length == 5) {
        return [""];
    }

    var result = []
    for (let element of char_arr) {
        var temp = char + element;
        var child_char = make_dict(temp, char_arr);
        if (child_char.length == 1) {
            result.push(temp);
        }
        else {
            child_char.unshift(temp)
            result.push(...child_char);
        }
    }
    return result;
}

function solution(word) {
    var start_char = word[0];
    var char_arr = ['A', 'E', 'I', 'O', 'U'];
    var dictionary = [];
    var temp;
    for (let char of char_arr) {
        if (char.charCodeAt(0) > start_char.charCodeAt(0)) {
            break;
        }
        temp = make_dict(char, char_arr)
        temp.unshift(char)
        dictionary.push(...temp);
    }
    console.log(dictionary)
    var answer = dictionary.indexOf(word) + 1;
    return answer;
}

var examples = [
    "AAAAE",
    "AAAE",
    "I",
    "EIO"
]

for (example of examples){
    console.log(solution(example));
}
