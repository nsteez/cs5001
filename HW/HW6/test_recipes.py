from recipes import validate_ingredients, recipe_to_file


def test_validate_ingredients():
    assert(validate_ingredients([]) is False)
    assert(validate_ingredients(["cheese", "sauce", "bread"]) is True)
    assert(validate_ingredients(["cheese  ", "  sauce", "  bread"]) is True)
    assert(validate_ingredients(["che  ese", "sau  ce", "b read"]) is True)


def test_recipe_to_file():
    assert(recipe_to_file("PIZZA") == "pizza.txt")
    assert(recipe_to_file("PIZZ A") == "pizz_a.txt")
    assert(recipe_to_file("Pizz A1") == "pizz_a1.txt")
    assert(recipe_to_file(" sAnd wich 1  ") == "sand_wich_1.txt")
    assert(recipe_to_file("PIZZ?A") == "pizza.txt")
