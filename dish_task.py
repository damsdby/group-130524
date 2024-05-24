header_footer = "~" * 50
print(header_footer)

dish_name = input("Введіть назву страви, рецепт якої вам подобається:").strip().upper()
decoration_dish_name = f"{'*' * 10}{dish_name}{'*' * 10}"

recipe = input("Введіть рецепт зазначеної страви:").strip().lower()

print(decoration_dish_name)

formatted_recipe = f"{recipe}😊"
print(formatted_recipe)

meat_count = recipe.count("мясо")
print(f"кількість слів 'мясо' у рецепті: {meat_count}")

print(header_footer)

