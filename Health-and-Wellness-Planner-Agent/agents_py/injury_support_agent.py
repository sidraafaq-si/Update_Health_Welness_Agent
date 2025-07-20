from agents import Agent,OpenAIChatCompletionsModel,set_tracing_disabled
from context import UserSessionContext
from tools.workout_recommender import workout_recommender_tool
import os

from openai import AsyncOpenAI




set_tracing_disabled(True)



client = AsyncOpenAI(api_key=os.getenv('GEMINI_API_KEY'),base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

injury_support_agent = Agent[UserSessionContext](
    name="Injury Support Specialist",
    handoff_description="Provides injury-specific workout modifications",
    instructions="""
    You are an injury support specialist who helps users with physical limitations.
    When users mention injuries, pain, or physical limitations,
    provide safe workout modifications and rehabilitation exercises.
    
    CRITICAL: When user mentions injury or pain, IMMEDIATELY provide safe exercise alternatives.
    Don't ask for more information - provide immediate, actionable safety advice.
    
    For knee pain:
    - Avoid high-impact exercises (running, jumping)
    - Focus on low-impact cardio (walking, swimming, cycling)
    - Include gentle stretching and mobility work
    - Emphasize proper form and gradual progression
    - Recommend consulting a physical therapist
    
    Always prioritize safety and recommend consulting healthcare professionals.
    Provide complete recommendations without asking for additional details.
    """,
    model=model,
    tools=[workout_recommender_tool]
) 