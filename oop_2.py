with open('oop.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for j in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recepie_name] = ingredients

def get_shop_list_by_dishes(dishes,person_count):
    new_cook = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_cook[ingredient['product']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity'])*person_count}
    print(new_cook)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


                

