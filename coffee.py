"""print("For ", number_of_cups, " cups of coffee you will need:\n",
      number_of_cups * 200, " ml of water\n", number_of_cups * 50,
     " ml of milk\n", number_of_cups * 15, " g of coffee beans")
"""
# Запрос запаса ингридиентов
stock_water = int(input('Write how many ml of water the coffee machine has:'))
stock_milk = int(input('Write how many ml of milk the coffee machine has:'))
stock_coffee = int(input('Write how many grams of coffee beans the coffee machine has:'))

# Запрос необходимого количества чашек кофе
number_of_cups = int(input("Write how many cups of coffee you will need:\n"))

# Расчет количества чашек кофе, которое можно приготовить из наличествующих запасов ингридиентов
make_only = min(stock_water // 200, stock_milk // 50, stock_coffee // 15)

# Расчет необходимого количества ингридиентов для приготовления запрошенного количесва чашек кофе
needs_water = number_of_cups * 200
needs_milk = number_of_cups * 50
needs_coffee = number_of_cups * 15

# Расчет остатка ингридиентов
can_cook_w = (stock_water - needs_water) // 200
can_cook_m = (stock_milk - needs_milk) // 50
can_cook_c = (stock_coffee - needs_coffee) // 15
n = min(can_cook_c, can_cook_m, can_cook_w)

if stock_water // needs_water == 1 and stock_milk // needs_milk == 1 and stock_coffee // needs_coffee == 1:
    print('Yes, I can make that amount of coffee')

elif stock_water // needs_water == 0 and stock_milk // needs_milk == 0 and stock_coffee // needs_coffee == 0:
    if make_only > 0:
        print('No, I can make only', make_only, ' cups of coffee')
    else:
        print('No, I can make only 0 cups of coffee')

elif make_only < number_of_cups:
    print('No, I can make only', make_only, ' cups of coffee')

else:
    print("Yes, I can make that amount of coffee (and even", n, " more than that)")

# if n > 0:
# print("Yes, I can make that amount of coffee (and even", n, " more than that)")
# else:
#    print("Yes, I can make that amount of coffee (and even 0  more than that)")
