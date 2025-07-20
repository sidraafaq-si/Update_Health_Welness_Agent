import json
from agents import function_tool

@function_tool
async def workout_recommender_tool(goal_type: str, fitness_level: str, available_equipment: str) -> str:
    """Suggests workout plan based on parsed goals and experience"""
    try:
        workout_plan = {
            "focus_area": "general_fitness",
            "difficulty": "beginner",
            "weekly_schedule": {},
            "equipment_needed": [],
            "safety_notes": [],
            "immediate_recommendations": []
        }
        
        # Set focus area based on goal
        if goal_type == "weight_loss":
            workout_plan["focus_area"] = "cardio_and_strength"
        elif goal_type == "muscle_gain":
            workout_plan["focus_area"] = "strength_training"
        elif goal_type == "endurance":
            workout_plan["focus_area"] = "cardio"
        
        # Set difficulty
        workout_plan["difficulty"] = fitness_level.lower()
        
        # Generate weekly schedule based on equipment
        equipment_lower = available_equipment.lower()
        
        if "none" in equipment_lower or "no equipment" in equipment_lower:
            # No equipment workouts
            if workout_plan["focus_area"] == "cardio_and_strength":
                workout_plan["weekly_schedule"] = {
                    "Monday": ["30 min brisk walking", "Push-ups 3x10", "Bodyweight squats 3x15"],
                    "Tuesday": ["Rest day"],
                    "Wednesday": ["30 min jogging", "Planks 3x30s", "Lunges 3x10 each leg"],
                    "Thursday": ["Rest day"],
                    "Friday": ["30 min walking", "Burpees 3x10", "Mountain climbers 3x20"],
                    "Saturday": ["Rest day"],
                    "Sunday": ["Light stretching", "Yoga or walking"]
                }
                workout_plan["immediate_recommendations"] = [
                    "Start with 30 minutes of brisk walking daily",
                    "Do 3 sets of 10 push-ups every other day",
                    "Include bodyweight squats and lunges",
                    "Focus on consistency over intensity"
                ]
            elif workout_plan["focus_area"] == "strength_training":
                workout_plan["weekly_schedule"] = {
                    "Monday": ["Push-ups 3x10", "Diamond push-ups 3x5", "Wall handstand practice"],
                    "Tuesday": ["Pull-ups 3x5", "Inverted rows 3x10", "Superman holds 3x30s"],
                    "Wednesday": ["Rest day"],
                    "Thursday": ["Squats 3x15", "Lunges 3x10 each", "Calf raises 3x20"],
                    "Friday": ["Planks 3x30s", "Side planks 3x20s each", "Russian twists 3x20"],
                    "Saturday": ["Rest day"],
                    "Sunday": ["Light cardio", "Stretching"]
                }
                workout_plan["immediate_recommendations"] = [
                    "Focus on bodyweight exercises",
                    "Practice push-ups and pull-ups",
                    "Include core exercises daily",
                    "Build strength gradually"
                ]
        else:
            # With equipment workouts
            if workout_plan["focus_area"] == "cardio_and_strength":
                workout_plan["weekly_schedule"] = {
                    "Monday": ["30 min cardio", "Push-ups 3x10", "Squats 3x15"],
                    "Tuesday": ["Rest day"],
                    "Wednesday": ["30 min cardio", "Pull-ups 3x5", "Lunges 3x10"],
                    "Thursday": ["Rest day"],
                    "Friday": ["30 min cardio", "Planks 3x30s", "Burpees 3x10"],
                    "Saturday": ["Rest day"],
                    "Sunday": ["Light stretching", "Yoga or walking"]
                }
        
        # Set equipment based on available equipment
        if "dumbbells" in equipment_lower:
            workout_plan["equipment_needed"].append("Dumbbells")
        if "barbell" in equipment_lower:
            workout_plan["equipment_needed"].append("Barbell")
        if "resistance bands" in equipment_lower:
            workout_plan["equipment_needed"].append("Resistance bands")
        
        # Add safety notes
        workout_plan["safety_notes"] = [
            "Always warm up before exercising",
            "Start with lighter weights and increase gradually",
            "Listen to your body and stop if you feel pain",
            "Stay hydrated throughout your workout"
        ]
        
        return json.dumps(workout_plan)
    except Exception as e:
        return json.dumps({
            "focus_area": "general_fitness",
            "difficulty": "beginner",
            "weekly_schedule": {"Monday": ["Error generating workout"]},
            "equipment_needed": [],
            "safety_notes": ["Consult a professional before starting"],
            "immediate_recommendations": ["Start with basic bodyweight exercises"]
        }) 