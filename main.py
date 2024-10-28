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


def main():
    file_path = 'C:\\Users\\semen\\PycharmProjects\\pythonProject\\dishes.txt'
    recipes = read_recipes(file_path)
    print(recipes)


if __name__ == "__main__":
    main()
