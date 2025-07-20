import json
import re
from agents import function_tool

@function_tool
async def goal_analyzer_tool(user_input: str) -> str:
    """Converts user goals into structured format"""
    try:
        # Simple goal parsing logic
        goal_data = {
            "goal_type": "general_fitness",
            "target_value": 0.0,
            "duration_weeks": 8,
            "is_realistic": True,
            "reasoning": "Default goal analysis",
            "fitness_level": "beginner",
            "equipment": "none",
            "workout_preference": "general"
        }
        
        input_lower = user_input.lower()
        
        # Parse weight loss goals
        if "lose" in input_lower and ("weight" in input_lower or "kg" in input_lower or "pound" in input_lower):
            goal_data["goal_type"] = "weight_loss"
            # Extract number (simple regex-like logic)
            numbers = re.findall(r'\d+', user_input)
            if numbers:
                goal_data["target_value"] = float(numbers[0])
            
            # Parse time duration
            if "day" in input_lower:
                time_units = "days"
                time_value = 1  # Default to 1 day
                if numbers and len(numbers) > 1:
                    time_value = int(numbers[1])
                goal_data["duration_weeks"] = max(1, time_value // 7)  # Convert days to weeks
            elif "week" in input_lower:
                time_units = "weeks"
                if numbers and len(numbers) > 1:
                    goal_data["duration_weeks"] = int(numbers[1])
            elif "month" in input_lower:
                time_units = "months"
                time_value = 1  # Default to 1 month
                if numbers and len(numbers) > 1:
                    time_value = int(numbers[1])
                goal_data["duration_weeks"] = time_value * 4  # Convert months to weeks
            else:
                time_units = "weeks"
                goal_data["duration_weeks"] = 8  # Default to 8 weeks
            
            # Calculate weekly weight loss rate
            weekly_rate = goal_data["target_value"] / goal_data["duration_weeks"]
            
            # Check if realistic (losing more than 1kg/week is unsafe, more than 0.5kg/week is optimal)
            if weekly_rate > 1.0:
                goal_data["is_realistic"] = False
                goal_data["reasoning"] = f"Losing {weekly_rate:.1f}kg per week is unsafe. Maximum safe rate is 1kg per week."
            elif weekly_rate > 0.5:
                goal_data["is_realistic"] = True
                goal_data["reasoning"] = f"Losing {weekly_rate:.1f}kg per week is achievable but aggressive. Consider a more gradual approach."
            else:
                goal_data["is_realistic"] = True
                goal_data["reasoning"] = f"Losing {weekly_rate:.1f}kg per week is a healthy and sustainable goal."
        
        # Parse muscle gain goals
        elif "gain" in input_lower and ("muscle" in input_lower or "strength" in input_lower):
            goal_data["goal_type"] = "muscle_gain"
            goal_data["reasoning"] = "Muscle building goal identified"
        
        # Parse fitness level
        if "beginner" in input_lower:
            goal_data["fitness_level"] = "beginner"
        elif "intermediate" in input_lower:
            goal_data["fitness_level"] = "intermediate"
        elif "advanced" in input_lower:
            goal_data["fitness_level"] = "advanced"
        
        # Parse equipment
        if "no equipment" in input_lower or "no available" in input_lower or "no equipment" in input_lower:
            goal_data["equipment"] = "none"
        elif "dumbbells" in input_lower:
            goal_data["equipment"] = "dumbbells"
        elif "gym" in input_lower:
            goal_data["equipment"] = "gym"
        
        return json.dumps(goal_data)
    except Exception as e:
        return json.dumps({
            "goal_type": "general_fitness",
            "target_value": 0.0,
            "duration_weeks": 8,
            "is_realistic": True,
            "reasoning": f"Error in analysis: {str(e)}",
            "fitness_level": "beginner",
            "equipment": "none",
            "workout_preference": "general"
        }) 