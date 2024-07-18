# Task 1

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu.update({"Beverages": {"Cola": 2.99, "Lemonade": 3.49}})
restaurant_menu.get("Main Course").update({"Steak": 17.99})
restaurant_menu.get("Starters").pop("Bruschetta")
print(restaurant_menu)