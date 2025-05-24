def is_matching(opening, closing):
    pairs = {'(': ')', '[': ']', '{': '}'}
    return pairs[opening] == closing


def max_correct_expr_length(text):
    max_len = 0
    stack = []
    last_invalid = -1  # Индекс последнего некорректного символа

    for i, ch in enumerate(text):
        if ch in '([{':
            stack.append((ch, i))
        elif ch in ')]}':
            if stack and is_matching(stack[-1][0], ch):
                stack.pop()
                if stack:
                    # Выражение между последним открытием и текущей позицией
                    length = i - stack[-1][1]
                else:
                    # Всё сбалансировано от последнего сбоя
                    length = i - last_invalid
                max_len = max(max_len, length)
            else:
                # Некорректная закрывающая скобка
                last_invalid = i
                stack.clear()
    return max_len


with open('txt/24-303.txt') as file:
    st = file.readline()

print(max_correct_expr_length(st))
