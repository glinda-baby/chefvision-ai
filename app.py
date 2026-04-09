from src.recipe_search import search_recipe
from src.ingredient_recommend import recommend_recipe
from src.nutrition_info import get_nutrition
from src.dish_detection import detect_dish


def main():

    print("ChefVision AI")
    print("1 Image to Recipe")
    print("2 Dish Name Search")
    print("3 Ingredients to Recipe")

    option = input("Select option: ")

    # OPTION 1 — Image to Recipe
    if option == "1":

        image_path = input("Enter image path: ")

        dish = detect_dish(image_path)

        if dish:

            print("\nDetected Dish:", dish)

            recipe = search_recipe(dish)

            if recipe:

                print("\nRecipe Found")

                print("Title:", recipe["title"])

                print("\nIngredients:")
                print(recipe["ingredients"])

                print("\nInstructions:")
                print(recipe["instructions"])

            else:
                print("Recipe not found")

            nutrition = get_nutrition(dish)

            if nutrition:

                print("\nNutrition Information (per 100g)")
                print("Calories:", nutrition["calories"])
                print("Protein:", nutrition["protein"])
                print("Carbs:", nutrition["carbs"])
                print("Fat:", nutrition["fat"])

            else:
                print("Nutrition information not found")

        else:
            print("Dish could not be detected")


    # OPTION 2 — Dish Name Search
    elif option == "2":

        dish = input("Enter dish name: ")

        recipe = search_recipe(dish)

        if recipe:

            print("\nRecipe Found")

            print("Title:", recipe["title"])

            print("\nIngredients:")
            print(recipe["ingredients"])

            print("\nInstructions:")
            print(recipe["instructions"])

        else:
            print("Recipe not found")

        nutrition = get_nutrition(dish)

        if nutrition:

            print("\nNutrition Information (per 100g)")
            print("Calories:", nutrition["calories"])
            print("Protein:", nutrition["protein"])
            print("Carbs:", nutrition["carbs"])
            print("Fat:", nutrition["fat"])

        else:
            print("Nutrition information not found")


    # OPTION 3 — Ingredients to Recipe
    elif option == "3":

        ingredients = input("Enter ingredients separated by comma: ")

        ingredients_list = ingredients.split(",")

        recipe = recommend_recipe(ingredients_list)

        if recipe:

            print("\nRecommended Recipe")

            print("Title:", recipe["title"])

            print("\nIngredients:")
            print(recipe["ingredients"])

            print("\nInstructions:")
            print(recipe["instructions"])

        else:
            print("No recipe found")


    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
