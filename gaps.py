def is_right_written(string: str) -> bool:
    """
    this func checks if all gaps in the string are correctly opened and closed

    :param string: str with only gaps
    :return: True if all gaps are right due to py rules else False
    """
    stack = []
    gaps = {')': '(', ']': '[', '}': '{'}

    for symbol in string:
        if symbol in "({[":
            stack.append(symbol)
        elif symbol in ")}]":
            if stack and stack[-1] == gaps[symbol]:
                stack.pop()
            else:
                return False

    return not stack

def is_valid_brackets_with_text(s: str) -> bool:
    """
    this func  check if all gaps in the string  opened and closed due to py rules (ignoring non-bracket characters)

    :param s: input str that has various characters with gaps
    :return: True if all brackets are right due to py rules else False
    """
    stack = []
    brackets_pairs = {')': '(', ']': '[', '}': '{'}

    for symbol in s:
        if symbol in "({[":
            stack.append(symbol)
        elif symbol in ")}]":
            if stack and stack[-1] == brackets_pairs[symbol]:
                stack.pop()
            else:
                return False


    return not stack

str_1 = "(){}[]{}}"
str_2 = "()()({[]})"
str_3 = "(77){9h}{[88]}"
str_4 = "((99df{}{ff)"
print(is_right_written(str_1))
print(is_right_written(str_2))
print(is_valid_brackets_with_text(str_3))
print(is_valid_brackets_with_text(str_4))