from pywebio.input import input as input_pw
from pywebio.input import NUMBER, FLOAT, DATE
from pywebio.output import put_text, put_html, put_image
from pywebio import start_server
from pywebio.session import run_js


greet_message = "<h1>Вас вітає щоденна вікторина</h1>"

def main():
    put_html(greet_message)
    total_score = 0

    user_name = input_pw("Введіть ваше ім'я:").title()
    put_text(f"Вітаємо, {user_name}!")

    question_one = input_pw("Яка дата народження Наполеона Буонапарте?")
    if question_one == "15.08.1796":
        total_score += 1
        put_html("<h3>Відповідь правильна, так тримати</h3>")
    question_two = input_pw("""Скільки років тривала "столітня війна"?""")
    if question_two == "116":
        total_score += 1
        put_html("<h3>Відповідь правильна, так тримати</h3>")
    question_three = input_pw("столиця Східної Римської імперії")
    if question_three == "Константинополь":
        total_score += 1
        put_html("<h3>Відповідь правильна, так тримати</h3>")
    question_four = input_pw("Яка дата вибуху на ЧАЕС?")
    if question_four == "26.04.1986":
        total_score += 1
        put_html("<h3>Відповідь правильна, так тримати</h3>")
    question_five = input_pw("55+2")
    if question_five == "57":
        total_score += 1
        put_html("<h3>Відповідь правильна, так тримати</h3>")



    put_html(f"Кількість балів становить: {total_score}")
    if total_score == 5:
        img = open("five_stars.jpeg", "rb").read()
        put_image(img, width="500px")

    run_js('setTimeout(function(){location.reload();}, 6000)')


if __name__ == '__main__':
    start_server(main, port=11000)
