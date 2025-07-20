from agents import Runner, InputGuardrailTripwireTriggered
from context import UserSessionContext
from agent import health_wellness_agent
from openai.types.responses import ResponseTextDeltaEvent

async def run_cli():
    """Run the Health & Wellness Planner with streaming CLI interface"""
    print("🏥 Health & Wellness Planner Agent")
    print("=" * 50)
    print("Type 'quit' to exit")
    print()
    
    # Initialize user context
    user_context = UserSessionContext(
        name="User",
        uid=1,
        goal=None,
        diet_preferences=None,
        workout_plan=None,
        meal_plan=None,
        injury_notes=None,
        handoff_logs=[],
        progress_logs=[]
    )
    
    while True:
        try:
            # Get user input
            user_input = input("\n💬 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n👋 Thank you for using the Health & Wellness Planner!")
                break
            
            if not user_input:
                continue
            
            print("\n🤖 Agent: ", end="", flush=True)
            
            # Run the agent
            try:
                result = Runner.run_streamed(
                    health_wellness_agent,
                    input=user_input,
                    context=user_context
                )

                async for event in result.stream_events():
                    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                        print(event.data.delta, end="", flush=True)
                

                    
            except InputGuardrailTripwireTriggered as e:
                print(f"⚠️ Guardrail triggered: {str(e)}")
            
            print()  # New line after response
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}") 