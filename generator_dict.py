from collections import defaultdict


def open_and_read(file_path: str) -> str:
    """
    this function reads file and gets info for next steps to work
    :param file_path: file
    :return: text
    """
    with open(file_path, 'r', encoding='utf8') as file:
        text = file.read()
        return text


file_path = r'C:\Users\tio\Downloads\input_1.txt'
text = open_and_read(file_path)


def count_and_return(text: str) -> dict:
    """
    this function says how many capital words and lowercase words contain the text
    :param text: capitalized words, lowercase words
    :return: dict with two of them(capital words and lowercase words) and their count
    """
    text_words = text.split()
    capitalized_count = 0
    lowercase_count = 0
    for word in text_words:
        if word[0].isupper():
            capitalized_count += 1

        if word.islower():
            lowercase_count += 1

    res = {'capitalized_words': capitalized_count, 'lowercase_words': lowercase_count}
    return res


def find_the_shortest_and_common(text: str) -> str:
    """
    this function finds the shortest and most common text word
    :param text: text
    :return: shortest and most common text word
    """
    fr = defaultdict(int)

    for word in text.lower().split():
        fr[word] += 1

    return min((word for word in fr if fr[word] == max(fr.values())), key=len)


def replace_most_common_in_capslock(text: str, word_to_replace: str) -> str:
    """
    this function replace the shortest and most common word to capital version
    :param text: most common and shortest word
    :param word_to_replace: as(the shortest and most common word)
    :return: text with replaced word
    """
    return ' '.join([word.upper() if word.lower().strip('.,!?') ==

                                     word_to_replace else word for word in text.split()])


most_common_short_word = find_the_shortest_and_common(text)
res = find_the_shortest_and_common(text)

updated_text = replace_most_common_in_capslock(text, most_common_short_word)
result = count_and_return(text)
print(res)
print(result)
print(updated_text)
