def greet_someone(username):
    return f"Вітаємо тебе, шановний {username}"


username = input("Введіть ваше ім'я: ").title()
html_user = greet_someone(username)
print(html_user)


# geometry_function
def count_square(length, width):
    result = length * width
    return result

area = count_square(length=10, width=5)
print(f"Площа прямокутника: {area}")
