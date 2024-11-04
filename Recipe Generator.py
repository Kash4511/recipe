def ing ():
    dishes = [
        "Butter Chicken",
            "Paneer Butter Masala",
            "Chole",
            "Rajma",
            "Palak Paneer",
            "Biryani",
            "Aloo Paratha",
            "Daal Makhani",
            "Tandoori Chicken",
            "Dosa",
            "Idli",
            "Sambar",]
    print("||Dishes||")
    for dish in dishes:
        print(f"- {dish}")
    print("\n")
    dish_rep = input("enter the dish: ").lower()
    print(f"||{dish_rep.capitalize()}||")
    if dish_rep.lower() == 'butter chicken':
        recipes ={
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
            "Add cream, simmer for 5 mins, and garnish with coriander."]}
        print("||Ingrediants||")
        for ing in recipes["Ingredients"]:
            print(f"- {ing}")
        print("\n")
        print("||Steps||")
        for steps in recipes["Steps"]:
            print(f"{steps}")
        print("\n")
        
    

ing()