from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider, \
    input_group
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table
from pywebio.session import run_js
from pywebio import start_server
from pprint import pprint

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

students["Максим Хижняк"] = {
    "Пошта": "Maksim@gmail.com",
    "Вік": 17,
    "Номер телефону": "096123123123",
    "Середній бал": 89,
}
student_result = 0
number_of_students = len(students)

for student_name, info in students.items():
    if info["Середній бал"]  > 90:
        print(f"Студенти, отримавші оцінку з відзнакою: {student_name}")
        print(info["Середній бал"])

    student_result += info["Середній бал"]
    student_phone = info["Номер телефону"]
    if student_phone is None:
        info["Номер телефону"] = (f"Номер батьків: 098777777")

student_avarage_result = student_result / number_of_students
print(f"students_avarage_result: {student_avarage_result}")

