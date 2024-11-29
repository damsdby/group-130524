import pprint

from pywebio.input import input as input_pw
from pywebio.output import put_text , put_html , put_image

put_html("<h1>Нарешті канікули!😉</h1>")

put_html("""<h2>Літнє сонце сяє ясно,
зеленіє все навкруг.
Час канікул, час прекрасний,
спів пташок і квітів луг.</h2>""")

summer_plans = input_pw("Розкажіть про ваші плани на це літо").title()

symbols_calculation = len(summer_plans)
put_text(f"Кількість символів у вашому повідомлені: {symbols_calculation}")

img = open("image.webp", "rb").read()
put_image(img, width="500px")
