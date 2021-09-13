def get_averages(scores):
    average = 0
    result = []
    for i in range(len(scores)):
        score = [scores[idx][i] for idx in range(len(scores))]
        max_score = max(score)
        min_score = min(score)
        if (score[i] == max_score and score.count(max_score) == 1) or \
            (score[i] == min_score and score.count(min_score)==1):
            average = (sum(score) - score[i])/(len(score)-1)
        else:
            average = sum(score)/len(score)
        result.append(average)
    return result

def solution(scores):
    answer = ''
    averages = get_averages(scores)
    for average in averages:
        if average >= 90:
            answer += "A"
        elif 80 <= average < 90:
            answer += "B"
        elif 70 <= average < 80:
            answer += "C"
        elif 50 <= average < 70:
            answer += "D"      
        else:
            answer += "F"
    return answer


examples = [
    [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]],
    [[50,90],[50,87]],
    [[70,49,90],[68,50,38],[73,31,100]]
]

for example in examples:
    print(solution(example))