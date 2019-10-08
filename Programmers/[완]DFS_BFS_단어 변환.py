import queue

def isPossible(word1, word2):
    n = len(word1)
    flag = 0
    for i in range(n):
        if word1[i] != word2[i]:
            flag += 1
        if flag == 2:
            return False
    return True



def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    else:
        n = len(words)
        table = [100 for _ in range(n+1)]   # table[0] = begin이 되는 수
        visited = [False for _ in range(n+1)]
        bfs = queue.Queue()
        bfs.put(begin)
        visited[0] = True
        table[0] = 0

        while(not bfs.empty()):
            temp = bfs.get()
            if temp == begin:
                idx = 0
            else:
                idx = words.index(temp) + 1
            if temp == target:
                break
            for i in range(n):
                if isPossible(temp, words[i]) and visited[i+1] == False:
                    bfs.put(words[i])
                    visited[i+1] = True
                    table[i+1] = table[idx] + 1
    answer = table[idx]
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))