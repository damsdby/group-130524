from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider
from pywebio.output import put_success, put_error, put_warning, put_image, put_html
from pywebio.session import run_js
from pywebio import start_server

good_review = ["Цікавий", "захоплюючий"]
bad_review = ["Нудний", "переоцінений"]
film_review_options = good_review + bad_review


film_genre = ["Комедія", "Мелодрама", ]
film_genre_two = ["Детектив", "Документальний", ]
film_genre_selection = film_genre_two + film_genre


user_rec = ["Так, рекомендую"]
user_not_rec = ["Ні, не рекомендую"]
user_variaty = user_rec + user_not_rec

reviews_info = []

def main():
    put_html("<h1>Вас вітає аналітика фильмів!</h1>")
    user_name = input_pw("Введіть ім'я користувача: ").title()
    greet_user = (f"<h2>Вітаємо, {user_name}</h2>")
    put_html(greet_user)

    film_name = input_pw("Введіть назву фільму:").title()
    put_html(f"<h3>Назва фільму: {film_name}</h3>")

    film_genre_option = select("Виберіть жанр фільму", options=film_genre_selection)


    film_review_slider = slider("Оцініть від одного до десяти для подальшого рейтингу", min_value=1, max_value=10)

    film_review = select("Яке у вас враження від цього фільму?", options=film_review_options)

    film_recommendation = radio("Чи рекомендуєте ви цей фільм іншим?", options=user_variaty)

    if film_review_slider >= 7:
        put_html("<h3>За останніми оцінками від користувачів, фільм рекомендується до перегляду</h3>")
        img = open("five_stars.jpeg", "rb").read()
        put_image(img, width="500px")
    run_js('setTimeout(function(){location.reload();}, 4000)')

    reviews_info.append({
        "ім'я_користувача": user_name,
        "назва_фільму": film_name,
        "жанр": film_genre_option,
        "оцінка_від_1_до_10": film_review_slider,
        "відгук": film_review,
        "рекомендація": film_recommendation
    })




if __name__ == '__main__':
    start_server(main, port=14000)










