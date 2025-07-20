import json
from datetime import datetime, timedelta
from agents import function_tool

@function_tool
async def checkin_scheduler_tool(user_id: int, frequency: str) -> str:
    """Schedules recurring weekly progress checks"""
    try:
        schedule = {
            "user_id": user_id,
            "frequency": frequency,
            "next_checkin": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
            "reminder_message": f"Time for your weekly progress check! How are you doing with your fitness goals?"
        }
        
        return json.dumps(schedule)
    except Exception as e:
        return json.dumps({
            "user_id": user_id,
            "frequency": "weekly",
            "next_checkin": "Error scheduling",
            "reminder_message": "Progress check reminder"
        }) 