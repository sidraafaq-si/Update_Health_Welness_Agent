import asyncio
from dotenv import load_dotenv
import os
from utils.streaming import run_cli

# Load environment variables
load_dotenv()

# Set model choice
model = os.getenv('LLM_MODEL_NAME', 'gpt-4o-mini')

if __name__ == "__main__":
    asyncio.run(run_cli()) 