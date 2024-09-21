def is_palindrome(s):
    s_lower = s.lower()
    return s_lower == s_lower[::-1]


str_1 = "SOme texttt  with     2367d d jd"
no_space = str_1.replace(' ', '')
print(no_space)

if is_palindrome(str_1):
    print("Так")
else:
    print("Нє")
