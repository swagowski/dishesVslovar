def read_recipes(files_path):
    recipes = {}
    with open(files_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                name, quantity, unit = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'unit': unit
                })
            recipes[dish_name] = ingredients
    return recipes

def get_shop_list_by_dishes(dishes, person_count,recipes):
    """Возвращает список ингредиентов для заданных блюд и количества персон."""
    shop_list = {}

    for dish in dishes:
        if dish in recipes:
            for ingredient in recipes[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['unit']
                quantity = ingredient['quantity'] * person_count

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'unit': measure, 'quantity': quantity}

    return shop_list


def main():
    file_path = 'C:\\Users\\semen\\PycharmProjects\\pythonProject\\dishes.txt'
    recipes = read_recipes(file_path)
    print(recipes)

    result = get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 3, recipes)
    print(result)
if __name__ == "__main__":
    main()