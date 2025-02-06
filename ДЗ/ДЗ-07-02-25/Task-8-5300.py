from itertools import permutations

answer = 0
for sentence in set(permutations('ХОЧУ В ВУЗ')):
    sentence = ''.join(sentence)
    if len(sentence.split())>=2:
        cnt = 0
        for word in sentence.split():
            if word[0]=='У':
                cnt += 1
        if cnt == 0:
            answer += 1
print(answer)



