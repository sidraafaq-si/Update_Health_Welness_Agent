import json
from agents import function_tool

@function_tool
async def meal_planner_tool(dietary_preferences: str, goal_type: str) -> str:
    """Async tool to suggest 7-day meal plan honoring dietary preferences"""
    try:
        # Generate meal plan based on preferences and goals
        meal_plan = {
            "daily_calories": 1800,
            "dietary_restrictions": [],
            "weekly_meals": {},
            "shopping_list": [],
            "quick_meal_ideas": []
        }
        
        # Adjust calories based on goal
        if goal_type == "weight_loss":
            meal_plan["daily_calories"] = 1500
        elif goal_type == "muscle_gain":
            meal_plan["daily_calories"] = 2200
        
        # Handle dietary preferences
        prefs_lower = dietary_preferences.lower()
        
        # Quick meal ideas for busy people
        meal_plan["quick_meal_ideas"] = [
            "Overnight oats with berries (5 min prep)",
            "Greek yogurt with granola and honey",
            "Smoothie with protein powder and banana",
            "Hard-boiled eggs with whole grain toast",
            "Canned tuna with mixed greens",
            "Hummus with carrot sticks and pita",
            "Protein shake with almond milk",
            "Apple with peanut butter",
            "Cottage cheese with pineapple",
            "Turkey and cheese roll-ups"
        ]
        
        if "vegetarian" in prefs_lower:
            meal_plan["dietary_restrictions"].append("vegetarian")
            meal_plan["weekly_meals"] = {
                "Monday": ["Oatmeal with berries", "Quinoa salad", "Lentil soup"],
                "Tuesday": ["Greek yogurt parfait", "Chickpea wrap", "Vegetable stir-fry"],
                "Wednesday": ["Smoothie bowl", "Bean burrito", "Pasta primavera"],
                "Thursday": ["Avocado toast", "Falafel pita", "Stuffed bell peppers"],
                "Friday": ["Chia pudding", "Hummus plate", "Mushroom risotto"],
                "Saturday": ["Fruit salad", "Veggie burger", "Cauliflower curry"],
                "Sunday": ["Granola with milk", "Tofu scramble", "Vegetable lasagna"]
            }
        elif "vegan" in prefs_lower:
            meal_plan["dietary_restrictions"].append("vegan")
            meal_plan["weekly_meals"] = {
                "Monday": ["Oatmeal with almond milk", "Chickpea salad", "Lentil curry"],
                "Tuesday": ["Smoothie with plant milk", "Tofu wrap", "Vegetable stir-fry"],
                "Wednesday": ["Chia pudding", "Bean burrito", "Pasta with tomato sauce"],
                "Thursday": ["Avocado toast", "Falafel pita", "Stuffed mushrooms"],
                "Friday": ["Fruit bowl", "Veggie burger", "Cauliflower rice"],
                "Saturday": ["Granola with plant milk", "Tempeh scramble", "Vegetable curry"],
                "Sunday": ["Smoothie bowl", "Hummus plate", "Mushroom pasta"]
            }
        else:
            # Standard meal plan
            meal_plan["weekly_meals"] = {
                "Monday": ["Eggs and toast", "Chicken salad", "Grilled salmon"],
                "Tuesday": ["Greek yogurt", "Turkey sandwich", "Beef stir-fry"],
                "Wednesday": ["Oatmeal", "Tuna wrap", "Pork chops"],
                "Thursday": ["Smoothie", "Ham sandwich", "Chicken breast"],
                "Friday": ["Cereal with milk", "Egg salad", "Fish tacos"],
                "Saturday": ["Pancakes", "Deli meat wrap", "Steak and vegetables"],
                "Sunday": ["French toast", "Chicken soup", "Roast chicken"]
            }
        
        # Generate shopping list
        meal_plan["shopping_list"] = [
            "Fresh vegetables", "Fruits", "Lean proteins", "Whole grains",
            "Healthy fats", "Dairy or alternatives", "Herbs and spices"
        ]
        
        return json.dumps(meal_plan)
    except Exception as e:
        return json.dumps({
            "daily_calories": 1800,
            "dietary_restrictions": [],
            "weekly_meals": {"Monday": ["Error generating meal plan"]},
            "shopping_list": ["Basic groceries"],
            "quick_meal_ideas": ["Overnight oats", "Greek yogurt", "Smoothie"]
        }) 