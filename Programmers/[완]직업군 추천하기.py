def solution(table, languages, preference):
    '''
    1. make table as dict: {jobs:{language: score, ...}, ...}
    2. get score according to languages and preference
    3. compare score each job
    4. get job of highest score
    '''
    table_dict = {
        col.split()[0]: {
            language: 5-idx for idx, language in enumerate(col.split()[1:])
        } for col in table
    }

    # calculate socre
    scores = []
    for job in table_dict.keys():
        score = 0
        for idx, language in enumerate(languages):
            if language in table_dict[job].keys():
                score += table_dict[job][language]*preference[idx]
        scores.append((score, job))
    scores = sorted(scores, key=lambda x: (-x[0], x[1]))

    answer= scores[0][1]
    
    return answer


examples = [
    {
        'table': ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
        'languages': ["PYTHON", "C++", "SQL"],
        'preference': [7,5,5],
    },
    {
        'table': ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
        'languages': ["JAVA", "JAVASCRIPT"],
        'preference': [7, 5],
    },
]


for example in examples:
    print(solution(example["table"], example["languages"], example["preference"]))