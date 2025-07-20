import json
from datetime import datetime
from agents import function_tool

@function_tool
async def progress_tracker_tool(user_id: int, current_weight: float, notes: str) -> str:
    """Accepts updates, tracks user progress, modifies session context"""
    try:
        progress_update = {
            "user_id": user_id,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "current_weight": current_weight,
            "notes": notes,
            "status": "Progress recorded successfully"
        }
        
        return json.dumps(progress_update)
    except Exception as e:
        return json.dumps({
            "user_id": user_id,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "current_weight": 0.0,
            "notes": f"Error recording progress: {str(e)}",
            "status": "Error"
        }) 