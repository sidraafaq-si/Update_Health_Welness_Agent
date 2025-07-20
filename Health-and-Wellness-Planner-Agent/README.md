# Health & Wellness Planner Agent

A comprehensive AI-powered health and wellness planning system that helps users achieve their fitness and health goals through personalized recommendations, meal planning, workout routines, and progress tracking.

## Features

- **Goal Analysis**: Intelligent parsing and validation of user fitness goals
- **Meal Planning**: Personalized 7-day meal plans based on dietary preferences and goals
- **Workout Recommendations**: Tailored workout routines for different fitness levels and equipment availability
- **Progress Tracking**: Weekly check-ins and progress monitoring
- **Safety Guardrails**: Built-in safety checks to prevent unrealistic or dangerous goals
- **Specialized Agents**: Handoff to nutrition experts, injury support specialists, and human coaching escalation
- **Streaming Interface**: Real-time CLI interface with streaming responses

## Project Structure

```
health_wellness_agent/
├── main.py                 # Entry point
├── agent.py               # Main health & wellness agent
├── context.py             # User session context models
├── guardrails.py          # Input validation and safety checks
├── tools/                 # Function tools
│   ├── goal_analyzer.py   # Goal parsing and analysis
│   ├── meal_planner.py    # Meal plan generation
│   ├── workout_recommender.py # Workout routine creation
│   ├── scheduler.py       # Progress check-in scheduling
│   └── tracker.py         # Progress tracking
├── agents/                # Specialized agents
│   ├── escalation_agent.py # Human coaching handoff
│   ├── nutrition_expert_agent.py # Dietary specialist
│   └── injury_support_agent.py # Injury support specialist
├── utils/                 # Utilities
│   └── streaming.py       # CLI streaming interface
└── README.md             # This file
```

## Installation

1. Install required dependencies:
```bash
pip install openai-agents pydantic python-dotenv
```

2. Set up environment variables:
```bash
# Create .env file
LLM_MODEL_NAME=gpt-4o-mini
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the application:
```bash
python main.py
```

### Example Interactions

**Goal Setting:**
```
💬 You: I want to lose 5kg in 8 weeks
🤖 Agent: [Analyzes goal and provides workout plan]
```

**Meal Planning:**
```
💬 You: I need a vegetarian meal plan for weight loss
🤖 Agent: [Generates 7-day vegetarian meal plan]
```

**Injury Support:**
```
💬 You: I have knee pain, what exercises can I do?
🤖 Agent: [Hands off to injury support specialist]
```

## Safety Features

- **Goal Validation**: Checks for unrealistic weight loss targets
- **Input Guardrails**: Validates user input for safety
- **Medical Disclaimers**: Recommends consulting healthcare professionals
- **Gradual Progression**: Emphasizes safe, sustainable approaches

## Agent Handoffs

The system automatically hands off to specialized agents when:

- **Nutrition Expert**: Diabetes, allergies, complex dietary needs
- **Injury Support**: Pain, injuries, physical limitations
- **Human Coach**: Requests for personal training or real coaching

## Contributing

1. Follow the existing code structure
2. Add appropriate error handling
3. Include safety checks for new features
4. Update documentation for any changes

## License

This project is for educational and personal use. Please consult healthcare professionals for medical advice. 
