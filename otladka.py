# Запас ингридиентов в кофе-машине
stock_w = int(input('Сколько в запасе воды?\n'))
stock_m = int(input('Сколько в запасе молока?\n'))
stock_coffee = int(input('Сколько в запасе кофе?\n'))

# Запрос необходимого количества чашек кофе
need_cups = int(input('Сколько нужно приготовить чашек кофе?\n'))

# Расчет необходимого количества ингридиентов для приготовления запрошенного количесва чашек кофе
needs_w = need_cups * 200
needs_m = need_cups * 50
needs_c = need_cups * 15

if stock_w // needs_w == 1 and stock_m // needs_m == 1 and stock_coffee // needs_c == 1:
    print('Пожалуйста, ваш кофе!')
elif stock_w // needs_w == 0 and stock_m // needs_m == 0 and stock_coffee // needs_c == 0:
    print('К сожалению, ингридиентов не хватит на такой заказ...')

else:
    # Расчет остатка ингридиентов
    can_cook_w = (stock_w - needs_w) // 200
    can_cook_m = (stock_m - needs_m) // 50
    can_cook_c = (stock_coffee - needs_c) // 15

    n = min(can_cook_c, can_cook_m, can_cook_w)
    pass
    print("Пожалуйста, ваш кофе! Ещё можно приготовить", n, " чашек кофе.")