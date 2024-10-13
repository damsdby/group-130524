def open_file(file_path: str) -> str:
    '''
    This function opens and read file (input_8)
    :param file_path: The path to the file
    :return: The content of the file in lowercase
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    return text


def say_which_symbol(text: str) -> dict:
    '''
     This function determines the type of symbol
    :return: dict with quanity of each  (letters, digits, whitespaces, and other symbols)
    '''
    result = {'letters': 0, 'digits': 0, 'whitespaces': 0, 'other': 0}

    for symbol in text:
        key = ('letters' if symbol.isalpha() else
               'digits' if symbol.isdigit() else
               'whitespaces' if symbol.isspace() else
               'other')

        result[key] += 1

    return result


def counter_vowels_consonants(text: str) -> tuple:
    '''
    this function counts quanity of vowels and consonaants in text
    :param text: string containing the text to analyze vowels, consonants
    :return: quanity of each
    '''
    vowels = 'aeiouаеёиоуыэюя'
    consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'

    v_counter = {}
    c_counter = {}

    for letter in text:
        if letter in vowels:
            v_counter[letter] = v_counter.get(letter, 0) + 1
        elif letter in consonants:
            c_counter[letter] = c_counter.get(letter, 0) + 1

    return v_counter, c_counter


def counter_and_creator(v_counter: dict, c_counter: dict) -> str:
    '''
     This function compares the counts of vowels and consonants and says wich is bigger
     :param v_counter:object containing vowel counts
     :param c_counter: object containing consonant counts
     :return: A string that shows most common letters based on the counts
     '''

    v_count = sum(v_counter.values())
    c_count = sum(c_counter.values())

    if c_count > v_count:
        most_common = max(c_counter.items(), key=lambda x: x[1])
        output = f"most common consonant: {most_common[0]} (quanity: {most_common[1]})"
    else:
        most_common = sorted(v_counter.items(), key=lambda x: x[1], reverse=True)[:3]
        output = "three vowels:\n"
        for v, count in most_common:
            output += f"{v} (quanity: {count})\n"

    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(output)

    return output


file_path = r"C:\Users\tio\Downloads\input_8.txt"
text = open_file(file_path)

res = say_which_symbol(text)
print(res)

v_counter, c_counter = counter_vowels_consonants(text)
result = counter_and_creator(v_counter, c_counter)

print(result)
