import chainlit as cl
from agent import health_wellness_agent
from context import UserSessionContext
from agents import Runner, InputGuardrailTripwireTriggered

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set(
        "user_context",
        UserSessionContext(
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
    )

@cl.on_message
async def main(message: cl.Message):
    user_context = cl.user_session.get("user_context")

    try:
        result = Runner.run_streamed(
            health_wellness_agent,
            input=message.content,
            context=user_context
        )

        full_response = ""
        msg = cl.Message(content="")  # Message object to stream into
        await msg.send()  # Send placeholder to enable streaming

        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, "delta"):
                token = event.data.delta  # assuming delta is a string
                full_response += token
                await msg.stream_token(token)

        # Fallback in case nothing was streamed
        if not full_response:
            await cl.Message(content="🤖 No response received.").send()

    except InputGuardrailTripwireTriggered as e:
        await cl.Message(content=f"⚠️ Guardrail triggered: {str(e)}", author="Agent").send()
    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}", author="Agent").send()
