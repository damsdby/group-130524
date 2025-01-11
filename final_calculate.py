from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.FoodData
collection = db.ManualInputFood

user_data = {
    'weight': None,
    'goal': None,
    'daily_recommendations': None,
    'nutrition': {
        'total_calories': 0,
        'total_protein': 0,
        'total_fat': 0,
        'total_carbs': 0,
        'Сніданок': {'calories': 0, 'protein': 0, 'fat': 0, 'carbs': 0},
        'Обід': {'calories': 0, 'protein': 0, 'fat': 0, 'carbs': 0},
        'Вечеря': {'calories': 0, 'protein': 0, 'fat': 0, 'carbs': 0}
    }
}


def get_male_recommendations(weight, goal):
    """
    запит на отримання подальшої інформації для чоловіків
    :param weight: вага в кг
    :param goal: мета
    :return: рекомендованне значення
    """
    base_calories = 2000
    if goal == "схуднення":
        recommended_calories = base_calories - 200
        protein = 2.5 * weight
        fat = 0.7 * weight
        carbs = 2.5 * weight
    elif goal == "підтримка ваги":
        recommended_calories = base_calories
        protein = 2 * weight
        fat = 1 * weight
        carbs = 3 * weight
    else:
        recommended_calories = base_calories + 300
        protein = 3 * weight
        fat = 1.2 * weight
        carbs = 4 * weight

    return recommended_calories, protein, fat, carbs


def get_female_recommendations(weight, goal):
    """
    запит на отримання подальшої інформації для жінок
    :param weight: вага в кг
    :param goal: мета
    :return: рекомендації згідно мети
    """
    base_calories = 1800
    if goal == "схуднення":
        recommended_calories = base_calories - 200
        protein = 2.5 * weight
        fat = 0.7 * weight
        carbs = 2.5 * weight
    elif goal == "підтримка ваги":
        recommended_calories = base_calories
        protein = 2 * weight
        fat = 1 * weight
        carbs = 3 * weight
    else:
        recommended_calories = base_calories + 300
        protein = 2.8 * weight
        fat = 1 * weight
        carbs = 3.5 * weight

    return recommended_calories, protein, fat, carbs


def calculate_nutrition(food_name, weight_grams):
    """
    розрахунок цінності продукту з дб
    :param food_name: назва страви
    :param weight_grams: вага у грамах
    :return: бжу та калораж
    """
    food = collection.find_one({'name': {'$regex': food_name, '$options': 'i'}})

    if food:
        calories = (food['calories'] * weight_grams) / 100
        protein = (food['protein'] * weight_grams) / 100
        fat = (food['fat'] * weight_grams) / 100
        carbs = (food['carbs'] * weight_grams) / 100
        return calories, protein, fat, carbs
    else:
        return None, None, None, None

def add_food_to_database(food_name, calories, protein, fat, carbs):
    """
    додає страву до бази даних, якщо такої нема
    :param food_name: назва страви
    :param calories: калораж
    :param protein: білки на 100 г
    :param fat: жири на 100 г
    :param carbs: вуглеводи на 100 г
    :return:
    """
    new_food = {
        'name': food_name,
        'calories': calories,
        'protein': protein,
        'fat': fat,
        'carbs': carbs
    }
    collection.insert_one(new_food)
    print(f"Продукт {food_name} додано в базу даних.")


def initialize_user_data():
    """
    Ініціалізація даних користувача
    :return: рекомендованні значення
    """
    print("Введіть вашу вагу в кг:")
    weight = float(input().strip())

    while weight <= 0:
        print("Вага не може бути меншою або рівною нулю. Введіть правильну вагу.")
        weight = float(input().strip())

    goal = input("Виберіть ціль: схуднення (схуднення), підтримка ваги (підтримка ваги), набір ваги (набір ваги): ").strip().lower()

    while goal not in ['схуднення', 'підтримка ваги', 'набір ваги']:
        print("Невірний вибір. Виберіть ціль з: схуднення (схуднення), підтримка ваги (підтримка ваги), набір ваги (набір ваги).")
        goal = input().strip().lower()

    user_data['weight'] = weight
    user_data['goal'] = goal

    gender = input("Оберіть стать: чоловіча (чоловіча) або жіноча (жіноча): ").strip().lower()

    while gender not in ["чоловіча", "жіноча"]:
        print("Невірний вибір. Виберіть стать: чоловіча (male) або жіноча (female).")
        gender = input("Оберіть стать: чоловіча (male) або жіноча (female): ").strip().lower()

    if gender == "чоловіча":
        recommended_calories, protein, fat, carbs = get_male_recommendations(weight, goal)
    else:
        recommended_calories, protein, fat, carbs = get_female_recommendations(weight, goal)

    user_data['daily_recommendations'] = {
        "calories": recommended_calories,
        "protein": protein,
        "fat": fat,
        "carbs": carbs
    }

    print("\nВаші рекомендації:")
    print(f"Калорійність: {recommended_calories} ккал")
    print(f"Білки: {protein} г")
    print(f"Жири: {fat} г")
    print(f"Вуглеводи: {carbs} г")
    print("\nНатисніть Enter, щоб продовжити...")
    input()


def main_menu():
    """
    меню программи
    :return: одну з обраних опцій
    """
    print("\n1. Розрахувати калорійність продукту")
    print("2. Перевірка спожитих калорій")
    print("3. Змінити ціль")
    print("4. Вийти")


def choose_meal_time():
    """
    додає вибір часу для прийому їжі
    :return: одну з опцій
    """
    print("\nОберіть час прийому їжі:")
    print("1. Сніданок")
    print("2. Обід")
    print("3. Вечеря")
    print("4. Назад")


def add_food_to_meal(meal_time):
    """
    додає страву до певного прийому
    :param meal_time: сніданок,обід та вечеря
    :return: бжу та калораж або одну з перевірок на неправильні значення
    """
    meal = user_data['nutrition'][meal_time]

    food_name = input("Введіть назву продукту: ").strip().lower()
    weight_grams = float(input("Кількість(у грамах): ").strip())

    if weight_grams <= 0:
        print("Кількість продукту не може бути меншою або рівною нулю!")
        return

    calories, protein, fat, carbs = calculate_nutrition(food_name, weight_grams)

    if calories is not None:
        print(f"{food_name.capitalize()} (на {weight_grams} г):")
        print(f"Калорії: {calories} ккал")
        print(f"Білки: {protein} г")
        print(f"Жири: {fat} г")
        print(f"Вуглеводи: {carbs} г")


        meal['calories'] += calories
        meal['protein'] += protein
        meal['fat'] += fat
        meal['carbs'] += carbs

        user_data['nutrition']['total_calories'] += calories
        user_data['nutrition']['total_protein'] += protein
        user_data['nutrition']['total_fat'] += fat
        user_data['nutrition']['total_carbs'] += carbs


        if meal['calories'] > user_data['daily_recommendations']['calories']:
            print(
                f"Перевищено на {meal['calories'] - user_data['daily_recommendations']['calories']} ккал у {meal_time.capitalize()}.")
        if meal['protein'] > user_data['daily_recommendations']['protein']:
            print(f"Перевищено на {meal['protein'] - user_data['daily_recommendations']['protein']} г білків.")
        if meal['fat'] > user_data['daily_recommendations']['fat']:
            print(f"Перевищено на {meal['fat'] - user_data['daily_recommendations']['fat']} г жирів.")
        if meal['carbs'] > user_data['daily_recommendations']['carbs']:
            print(f"Перевищено на {meal['carbs'] - user_data['daily_recommendations']['carbs']} г вуглеводів.")

        print(f"\nЗагальні калорії за {meal_time.capitalize()}: {meal['calories']} ккал")
        print(f"Загальні білки за {meal_time.capitalize()}: {meal['protein']} г")
        print(f"Загальні жири за {meal_time.capitalize()}: {meal['fat']} г")
        print(f"Загальні вуглеводи за {meal_time.capitalize()}: {meal['carbs']} г")
    else:
        print("Продукт не знайдено в базі даних.")
        add_new = input("Бажаєте додати цей продукт в базу даних? (так/ні): ").strip().lower()
        if add_new == "так":
            calories = float(input("Введіть кількість калорій на 100 г: ").strip())
            protein = float(input("Введіть кількість білків на 100 г: ").strip())
            fat = float(input("Введіть кількість жирів на 100 г: ").strip())
            carbs = float(input("Введіть кількість вуглеводів на 100 г: ").strip())
            add_food_to_database(food_name, calories, protein, fat, carbs)

def meal_select():
    choose_meal_time()
    choice = int(input("Ваш вибір: ").strip())

    if choice == 1:
        add_food_to_meal('Сніданок')
    elif choice == 2:
        add_food_to_meal('Обід')
    elif choice == 3:
        add_food_to_meal('Вечеря')


def start():
    """
    Головний цикл програми
    :return: результат обраної опції
    """
    initialize_user_data()
    while True:
        main_menu()
        choice = int(input("Ваш вибір: ").strip())

        if choice == 1:
            meal_select()
        elif choice == 2:
            print(f"Загальні калорії: {user_data['nutrition']['total_calories']} ккал")
            print(f"Загальні білки: {user_data['nutrition']['total_protein']} г")
            print(f"Загальні жири: {user_data['nutrition']['total_fat']} г")
            print(f"Загальні вуглеводи: {user_data['nutrition']['total_carbs']} г")
        elif choice == 3:
            print("Виберіть нову мету для користувача.")
            initialize_user_data()
        elif choice == 4:
            break

start()
