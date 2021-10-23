function solution(s) {
    let numAlphabetObj = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    };
    var answer = 0;
    var stack = [];
    var startIdx = -1;
    for (let i=0; i < s.length; i++) {
        if (Object.keys(numAlphabetObj).includes(s.substring(startIdx, i))) {
            stack.push(numAlphabetObj[s.substring(startIdx, i)]);
            startIdx = -1;
        }
        if (isNaN(s[i])) {
            if (startIdx == -1) startIdx = i;
        }
        else {
            startIdx = -1;
            stack.push(s[i]);
        }
    }
    if (startIdx != -1) stack.push(numAlphabetObj[s.substring(startIdx)]);
    answer = Number(stack.join(""));
    return answer;
}


examples = [
    "one4seveneight",
    "23four5six7",
    "2three45sixseven",
    "123",
];

for (let example of examples) {
    console.log(solution(example));
}
