beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(wordList[0][1])
m = 0
t = {}
q = {}
for i in range(5):
    for j in range(3):
        if beginWord[j] == wordList[i][j]:
            m += 1
        if j == 2:
            t[wordList[i]] = m
            m = 0
print(t)
for i in range(5):
    for j in range(3):
        if endWord[j] == wordList[i][j]:
            m += 1
        if j == 2:
            q[wordList[i]] = m
            m = 0
print(q)
print(m)
