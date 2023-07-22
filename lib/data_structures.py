spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    returne_names = []
    for food in spicy_foods:
        returne_names.append(food["name"])
    return returne_names

def get_spiciest_foods(spicy_foods):
    spiciest_list = []
    
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_list.append(food)
    
    return spiciest_list

def print_spicy_foods(spicy_foods):
  
  for food in spicy_foods:
    list = []
    for i in range(food["heat_level"]): 
     list.append('🌶')
    string = ''.join(list)
    print(f"{food['name']} ({food['cuisine']}) | Heat Level: {string}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
       if food['cuisine'] == cuisine:
          return food 
    return None 

def print_spiciest_foods(spicy_foods):
   function1 = get_spiciest_foods(spicy_foods)
   print_spicy_foods(function1)

def get_average_heat_level(spicy_foods):
  total_heat = 0
  num = len(spicy_foods)
  for food in spicy_foods: 
     total_heat += food["heat_level"]
  return total_heat/num

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
