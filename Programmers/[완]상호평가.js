function get_averages(scores) {
    var average = 0
    let result = []
    let score = []
    for (var i=0; i < scores.length; i++) {
        score = []
        for (var idx=0; idx < scores.length; idx++) {
            score.push(scores[idx][i]);
        }
        var max_score = Math.max(...score)
        var min_score = Math.min(...score)
        if ((score[i] == max_score && score.filter(s => s == max_score).length == 1) || (score[i] == min_score && score.filter(s => s == min_score).length == 1)) {
            console.log(score)
            average = (score.reduce((a, b) => a+ b, 0) - score[i])/(score.length - 1)
        }
        else {
            average = score.reduce(function add (sum, currValue) {
                return sum + currValue;
            }, 0)/score.length;
        }
        // console.log(score)
        result.push(average)
    }
    return result
}

function solution(scores) {
    var answer = '';
    var averages = get_averages(scores);
    for (let average of averages) {
        if (average >= 90) {
            answer += "A";
        }
        else if (average >= 80 && average < 90) {
            answer += "B";
        }
        else if (average >= 70 && average < 80) {
            answer += "C";
        }
        else if (average >= 50 && average < 70) {
            answer += "D"
        }
        else {
            answer += "F"
        }
    }
    return answer;
}

let examples = [
    [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]],
    [[50,90],[50,87]],
    [[70,49,90],[68,50,38],[73,31,100]]
]

for (example of examples) {
    console.log(solution(example));
}
