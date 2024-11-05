
def ing():

    dishes = ["Butter Chicken", "Palak Paneer", "Biryani", "Tiramisu", "Fettuccine Alfredo", "Bruschetta"]
    print("|| Dishes ||")
    for dish in dishes:
        print(f"- {dish}")
    print("\n")

    
    dish_rep = input("Enter the dish: ").lower() 
    print(f"\n|| {dish_rep.capitalize()} ||")

    if dish_rep == "butter chicken":
        butter_chicken_recipe = {
            "Ingredients": [
                "500g chicken, boneless",
                "2 tablespoons butter",
                "1 onion, chopped",
                "2 tomatoes, pureed",
                "1/2 cup cream",
                "1 tablespoon ginger-garlic paste",
                "2 teaspoons garam masala",
                "Salt to taste",
                "Fresh coriander for garnish"
            ],
            "Steps": [
                "Sauté onions in butter until golden, then add ginger-garlic paste.",
                "Add chicken and cook until no longer pink.",
                "Stir in tomato puree, salt, and garam masala; cook for 15 mins.",
                "Add cream, simmer for 5 mins, and garnish with coriander."
            ],
            "Cooking Time": "30 minutes"
        }
        
        print("\n|| Ingredients ||")
        for ing in butter_chicken_recipe["Ingredients"]:
            print(f"- {ing}")
        
        print("\n|| Steps ||")
        for step in butter_chicken_recipe["Steps"]:
            print(step)
        
        print("\nCooking Time:", butter_chicken_recipe["Cooking Time"])

    elif dish_rep == "palak paneer":
        palak_paneer_recipe = {
            "Ingredients": [
                "250g paneer, cubed",
                "2 cups fresh spinach leaves, washed and chopped",
                "1 tablespoon oil or ghee",
                "1 tablespoon butter",
                "1 onion, finely chopped",
                "1 tomato, finely chopped",
                "1 green chili, chopped (optional)",
                "1 tablespoon ginger-garlic paste",
                "1/4 teaspoon turmeric powder",
                "1/2 teaspoon cumin seeds",
                "1/2 teaspoon garam masala",
                "1/2 teaspoon coriander powder",
                "Salt to taste",
                "2-3 tablespoons cream (optional, for richness)"
            ],
            "Steps": [
                "Blanch spinach leaves in hot water for 2-3 minutes, then cool and blend into a smooth puree.",
                "Heat oil and butter in a pan, add cumin seeds, and let them sizzle.",
                "Add chopped onions and sauté until golden brown.",
                "Add ginger-garlic paste and green chili; cook for a minute until fragrant.",
                "Add chopped tomatoes and cook until they turn soft.",
                "Stir in turmeric, coriander powder, and salt; cook for 2 minutes.",
                "Pour in the spinach puree and mix well. Simmer for 5 minutes.",
                "Add paneer cubes, garam masala, and cream (if using); mix gently and cook for another 3-4 minutes.",
                "Serve hot with naan or rice."
            ],
            "Cooking Time": "30 minutes"
        }

        print("\n|| Ingredients ||")
        for ing in palak_paneer_recipe["Ingredients"]:
            print(f"- {ing}")
        
        print("\n|| Steps ||")
        for step in palak_paneer_recipe["Steps"]:
            print(step)
        
        print("\nCooking Time:", palak_paneer_recipe["Cooking Time"])

    elif dish_rep == "biryani":
        biryani_recipe = {
            "Ingredients": [
                "500g basmati rice",
                "500g chicken or lamb, cut into pieces",
                "1 cup yogurt",
                "2 onions, thinly sliced",
                "2 tomatoes, chopped",
                "2 tablespoons ginger-garlic paste",
                "1/4 cup oil or ghee",
                "1/2 cup chopped fresh coriander leaves",
                "1/2 cup chopped fresh mint leaves",
                "2-3 green chilies, slit",
                "1/2 teaspoon turmeric powder",
                "1 teaspoon red chili powder",
                "1 teaspoon garam masala powder",
                "4-5 cloves",
                "2-3 cardamom pods",
                "1 cinnamon stick",
                "2-3 bay leaves",
                "Salt to taste",
                "Water as required for cooking rice"
            ],
            "Steps": [
                "Wash and soak basmati rice for 30 minutes. Drain and set aside.",
                "In a large pot, heat oil or ghee. Add cloves, cardamom, cinnamon, and bay leaves; sauté until aromatic.",
                "Add sliced onions and cook until golden brown.",
                "Add ginger-garlic paste and green chilies; cook for a minute until fragrant.",
                "Add chopped tomatoes, turmeric powder, red chili powder, and salt; cook until tomatoes soften.",
                "Add chicken or lamb pieces and cook until they are no longer pink.",
                "Stir in yogurt, coriander leaves, and mint leaves; cook for 5-10 minutes until meat is tender.",
                "In a separate pot, boil water with salt. Add the soaked rice and cook until 70% done, then drain.",
                "Layer the partially cooked rice over the meat mixture in the large pot.",
                "Sprinkle garam masala powder and some additional coriander and mint leaves on top.",
                "Cover the pot tightly and cook on low heat (dum) for 20-25 minutes.",
                "Serve hot with raita or your choice of side dish."
            ],
            "Cooking Time": "45 minutes (plus 30 minutes soaking)"
        }

        print("\n|| Ingredients ||")
        for ing in biryani_recipe["Ingredients"]:
            print(f"- {ing}")
        
        print("\n|| Steps ||")
        for step in biryani_recipe["Steps"]:
            print(step)
        
        print("\nCooking Time:", biryani_recipe["Cooking Time"])

    elif dish_rep == "tiramisu":
        tiramisu_recipe = {
            "Ingredients": [
                "6 egg yolks",
                "3/4 cup granulated sugar",
                "1 cup mascarpone cheese",
                "1 1/2 cups heavy cream",
                "2 cups brewed espresso or strong coffee, cooled",
                "1/4 cup coffee liqueur (optional)",
                "24-30 ladyfinger cookies",
                "Cocoa powder, for dusting",
                "Chocolate shavings (optional, for garnish)"
            ],
            "Steps": [
                "In a mixing bowl, whisk egg yolks and sugar together until smooth and pale.",
                "Add mascarpone cheese and blend until smooth and creamy.",
                "In a separate bowl, whip the heavy cream to soft peaks, then gently fold it into the mascarpone mixture.",
                "Combine the coffee and liqueur (if using) in a shallow dish.",
                "Dip each ladyfinger quickly into the coffee mixture, then layer them in the bottom of a rectangular dish.",
                "Spread half of the mascarpone mixture over the ladyfingers.",
                "Add another layer of dipped ladyfingers on top, then spread the remaining mascarpone mixture over them.",
                "Cover and refrigerate for at least 4 hours (preferably overnight) to allow flavors to develop.",
                "Before serving, dust the top with cocoa powder and garnish with chocolate shavings if desired."
            ],
            "Chill Time": "4 hours (overnight recommended)"
        }

        print("\n|| Ingredients ||")
        for ing in tiramisu_recipe["Ingredients"]:
            print(f"- {ing}")
        
        print("\n|| Steps ||")
        for step in tiramisu_recipe["Steps"]:
            print(step)
        
        print("\nChill Time:", tiramisu_recipe["Chill Time"])

    elif dish_rep == "fettuccine alfredo":
        fettuccine_alfredo_recipe = {
            "Ingredients": [
                "300g fettuccine pasta",
                "1 cup heavy cream",
                "1/2 cup unsalted butter",
                "1 cup grated Parmesan cheese",
                "Salt to taste",
                "Freshly ground black pepper, to taste",
                "Fresh parsley, chopped (for garnish)"
            ],
            "Steps": [
                "Cook the fettuccine pasta in a large pot of salted boiling water according to package instructions. Drain and set aside.",
                "In a large skillet over medium heat, melt the butter and pour in the heavy cream. Stir to combine.",
                "Simmer the mixture for about 5 minutes, until it thickens slightly.",
                "Gradually whisk in the Parmesan cheese until the sauce is smooth and creamy.",
                "Season with salt and pepper to taste.",
                "Add the cooked fettuccine to the sauce, tossing to coat the pasta thoroughly.",
                "Garnish with fresh parsley and serve immediately."
            ],
            "Cooking Time": "20 minutes"
        }

        print("\n|| Ingredients ||")
        for ing in fettuccine_alfredo_recipe["Ingredients"]:
            print(f"- {ing}")
        
        print("\n|| Steps ||")
        for step in fettuccine_alfredo_recipe["Steps"]:
            print(f"{step}")

        

    elif dish_rep == "bruschetta":
        bruschetta_recipe = {
            "Ingredients": [
                "1 baguette, sliced",
                "3-4 ripe tomatoes, diced",
                "2 cloves garlic, minced",
                "1/4 cup fresh basil leaves, chopped",
                "2 tablespoons olive oil",
                "Salt and pepper to taste",
                "Balsamic glaze (optional)"
            ],
            "Steps": [
                "Toast baguette slices in the oven or on a grill until golden and crisp.",
                "In a bowl, mix diced tomatoes, minced garlic, basil, olive oil, salt, and pepper.",
                "Top each toasted baguette slice with the tomato mixture.",
                "Drizzle with balsamic glaze if desired.",
                "Serve immediately as an appetizer or snack."
            ],
            "Preparation Time": "15 minutes"
        }

        print("\n|| Ingredients ||")
        for ing in bruschetta_recipe["Ingredients"]:
            print(f"- {ing}")
        
        print("\n|| Steps ||")
        for step in bruschetta_recipe["Steps"]:
            print(step)
        
        print("\nPreparation Time:", bruschetta_recipe["Preparation Time"])

    else:
        print("Sorry, recipe not available for the entered dish.")

ing()

