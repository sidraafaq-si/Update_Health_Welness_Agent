from agents import Agent,OpenAIChatCompletionsModel,set_tracing_disabled
from context import UserSessionContext
from tools.meal_planner import meal_planner_tool
import os

from openai import AsyncOpenAI




set_tracing_disabled(True)



client = AsyncOpenAI(api_key=os.getenv('GEMINI_API_KEY'),base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

nutrition_expert_agent = Agent[UserSessionContext](
    name="Nutrition Expert",
    handoff_description="Handles complex dietary needs like diabetes or allergies",
    instructions="""
    You are a nutrition expert specializing in complex dietary needs.
    Handle cases involving diabetes, food allergies, medical conditions,
    or other specialized nutrition requirements.
    
    CRITICAL: When user mentions diabetes, IMMEDIATELY use meal_planner_tool to provide a diabetic-friendly meal plan.
    Don't ask for more information - provide immediate, actionable nutrition advice.
    
    For diabetes and weight loss:
    - Focus on low glycemic index foods
    - Emphasize portion control
    - Include regular meal timing
    - Monitor carbohydrate intake
    - Provide specific meal suggestions
    
    Always provide complete meal plans and recommendations without asking for additional information.
    """,
    model=model,
    tools=[meal_planner_tool]
) 