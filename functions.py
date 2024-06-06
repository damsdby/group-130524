def greet_user_with_h1(username):
    result = f"<h1>Вітаємо тебе, шановний {username}</h1>"
    return result


username = input("Введіть ваше ім'я: ").title()
html_user = greet_user_with_h1(username)
print(html_user)


# geometry_function
def calculations_area_the_rectangle(length, width):
    result = length * width
    return result


area = calculations_area_the_rectangle(length=10, width=5)
print(f"<h1> Площа прямокутника: {area}</h1>")
