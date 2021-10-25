function solution(participant, completion) {
    participant.sort()
    completion.sort()
    var idx = 0
    for (idx; idx < participant.length;idx++) {
        if (participant[idx] != completion[idx]) {
            break;
        }
    }
    var answer = participant[idx];
    return answer;
}