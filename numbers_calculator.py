quantity_people = 4
ticket_price_per_person = 500
taxi_from_park = 600
taxi_to_park = taxi_from_park * 1.2  # 20% more expensive
pizzas_price = 250
number_of_pizzas = 2
pizzas_discount = 0.15
hockey_play = 80
number_of_plays = 8

#calculations
total_ticket_price = quantity_people * ticket_price_per_person
total_taxi_price = (taxi_from_park + taxi_to_park)
total_pizzas_discount = (pizzas_price * number_of_pizzas) * pizzas_discount
total_pizzas_price = (pizzas_price * number_of_pizzas) - total_pizzas_discount
total_hockey_price = hockey_play * number_of_plays

#total_cost
total_cost = (total_ticket_price + total_taxi_price + total_pizzas_price + total_hockey_price)

#total price per person
total_price_per_person = total_cost / quantity_people

print(f"Each person should pay: {total_price_per_person:.2f} UAH")
