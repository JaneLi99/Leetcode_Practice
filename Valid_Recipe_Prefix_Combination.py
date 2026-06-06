# You are given an array of strings ingredients and an array of strings recipes.
# A recipe is considered valid if it can be formed by concatenating the first several elements of ingredients in order.
# In other words, a recipe is valid if there exists an integer k such that:
# recipe = ingredients[0] + ingredients[1] + ... + ingredients[k]
# for some 0 <= k < len(ingredients).
# Return a boolean array answer where answer[i] is true if recipes[i] is a valid recipe prefix combination, and false otherwise.
#
# Example 1
# Input:
# ingredients = ["ab", "c", "def"]
# recipes = ["ab", "abc", "abcdef", "ac", "abcdefg"]
# Output:
# [true, true, true, false, false]
# Explanation:
# "ab" = ingredients[0] → valid
# "abc" = "ab" + "c" → valid
# "abcdef" = "ab" + "c" + "def" → valid
# "ac" cannot be formed by concatenating a prefix of ingredients → invalid
# "abcdefg" is longer than any prefix concatenation → invalid
#
# Example 2
# Input:
# ingredients = ["x", "yz", "m"]
# recipes = ["x", "xyz", "xyzm", "yz", "xm"]
# Output:
# [true, true, true, false, false]

from typing import List


def validateRecipes(ingredients: List[str], recipes: List[str]) -> List[bool]:
    prefixes = set()
    current = ""

    # Build all prefix combinations
    for ing in ingredients:
        current += ing
        prefixes.add(current)

    # Check each recipe
    result = []
    for recipe in recipes:
        result.append(recipe in prefixes)

    return result

def validateRecipesAnotherWay(ingredients, recipes):
    output = []

    for recipe in recipes:
        remaining = recipe
        matched = False
        i = 0

        while i < len(ingredients):
            if remaining.startswith(ingredients[i]):
                remaining = remaining.removeprefix(ingredients[i])
                matched = True
                if remaining == "":
                    break
            else:
                break
            i += 1

        if remaining == "" and matched:
            output.append(True)
        else:
            output.append(False)

    return output

def main():
    # Test Case 1
    ingredients = ["ab", "c", "def"]
    recipes = ["ab", "abc", "abcdef", "ac", "abcdefg"]

    print("Test Case 1")
    print("ingredients:", ingredients)
    print("recipes:", recipes)
    print("output:", validateRecipes(ingredients, recipes))
    print()

    # Test Case 2
    ingredients = ["x", "yz", "m"]
    recipes = ["x", "xyz", "xyzm", "yz", "xm"]

    print("Test Case 2")
    print("ingredients:", ingredients)
    print("recipes:", recipes)
    print("output:", validateRecipes(ingredients, recipes))
    print()

    # Test Case 3
    ingredients = ["a", "bc", "d", "ef"]
    recipes = ["a", "abcd", "abcdef", "ab", "bcdef"]

    print("Test Case 3")
    print("ingredients:", ingredients)
    print("recipes:", recipes)
    print("output:", validateRecipes(ingredients, recipes))


if __name__ == "__main__":
    main()