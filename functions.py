def greet_someone(username):
    return f"Вітаємо тебе, шановний {username}"


username = input("Введіть ваше ім'я: ").title()
html_user = greet_someone(username)
print(html_user)


# geometry_function
def rectangle_calculation(length, width):
    length = int(length)
    width = int(width)
    return length * width


length = input("Введіть довжину прямокутника:")
width = input("Введіть ширину прямокутника:")

result = rectangle_calculation(length, width)
print(f"Площа прямокутника: {result}")
