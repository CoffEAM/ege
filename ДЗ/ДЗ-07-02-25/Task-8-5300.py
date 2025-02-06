from itertools import permutations

answer = 0
for sentence in set(permutations('ХОЧУ В ВУЗ')):
    sentence = ''.join(sentence)
    if len(sentence.split())==3:
        cnt = sum(1 for word in sentence.split() if word[0]=='У')
        if cnt == 0:
            answer += 1
    if sentence=='ХОЧУ В ВУЗ':
        print('god damn it не хочу в вуз')
print(answer)



