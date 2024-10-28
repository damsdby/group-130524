str_1 = "ghg"
lst = ['two', 'kd', 'lambda', 'spinat', 'gut']
numbers_list = [34, 10, 5, 60, 8, 25]

pal_str = lambda str: str == str[::-1]

only_not_even = lambda num: num % 2 != 0

average_length = sum(len(word) for word in lst) / len(lst)

short_words = lambda lst: [word for word in lst if len(word) <= average_length]

res = [num for num in numbers_list if only_not_even(num)]
short_word_list = short_words(lst)

print(pal_str(str_1))
print(res)
print(short_word_list)
