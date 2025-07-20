from agents import GuardrailFunctionOutput

async def goal_input_guardrail(ctx, agent, input_data):
    """Validate goal input format and safety"""
    try:
        # Check for goal-related keywords
        goal_keywords = ['lose', 'gain', 'build', 'improve', 'increase', 'decrease', 'maintain']
        has_goal = any(keyword in input_data.lower() for keyword in goal_keywords)
        
        # Check for quantity and time indicators
        has_quantity = any(char.isdigit() for char in input_data)
        time_indicators = ['week', 'month', 'day', 'year']
        has_time = any(indicator in input_data.lower() for indicator in time_indicators)
        
        # Check for dangerous/extreme keywords
        dangerous_keywords = ['extreme', 'intense', 'maximum', 'fast', 'quick', 'rapid', 'crash', 'fad']
        has_dangerous = any(keyword in input_data.lower() for keyword in dangerous_keywords)
        
        # Check for unrealistic timeframes
        input_lower = input_data.lower()
        if 'lose' in input_lower and 'weight' in input_lower:
            import re
            numbers = re.findall(r'\d+', input_data)
            if numbers and len(numbers) >= 2:
                try:
                    weight_goal = float(numbers[0])
                    time_value = float(numbers[1])
                    
                    # Check for unrealistic combinations
                    if 'week' in input_lower and weight_goal > 2:
                        return GuardrailFunctionOutput(
                            output_info={"is_valid": False, "reasoning": f"Losing {weight_goal}kg in {time_value} week(s) is unsafe"},
                            tripwire_triggered=True
                        )
                    elif 'day' in input_lower and weight_goal > 0.5:
                        return GuardrailFunctionOutput(
                            output_info={"is_valid": False, "reasoning": f"Losing {weight_goal}kg in {time_value} day(s) is extremely unsafe"},
                            tripwire_triggered=True
                        )
                except:
                    pass
        
        is_valid = has_goal and has_quantity and has_time and not has_dangerous
        
        return GuardrailFunctionOutput(
            output_info={"is_valid": is_valid, "reasoning": "Goal validation check"},
            tripwire_triggered=not is_valid
        )
    except Exception as e:
        return GuardrailFunctionOutput(
            output_info={"is_valid": True, "reasoning": f"Error in validation: {str(e)}"},
            tripwire_triggered=False
        )

async def dietary_input_guardrail(ctx, agent, input_data):
    """Validate dietary input"""
    try:
        dietary_keywords = ['vegetarian', 'vegan', 'gluten', 'dairy', 'nut', 'diabetic', 'allergy']
        has_dietary = any(keyword in input_data.lower() for keyword in dietary_keywords)
        
        return GuardrailFunctionOutput(
            output_info={"has_dietary": has_dietary, "reasoning": "Dietary preference check"},
            tripwire_triggered=False  # Don't block, just track
        )
    except Exception as e:
        return GuardrailFunctionOutput(
            output_info={"has_dietary": False, "reasoning": f"Error in validation: {str(e)}"},
            tripwire_triggered=False
        ) 