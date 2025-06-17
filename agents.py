from crewai import Agent, LLM
from tools import PlaywrightLoginTool
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"Gemini API Key loaded: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"Key starts with: {api_key[:10]}...")

playwright_login_tool = PlaywrightLoginTool()

try:
    gemini_llm = LLM(
        model="gemini/gemini-1.5-flash",
        api_key=api_key,
        temperature=0.7
    )
    print("CrewAI LLM initialized successfully")
except Exception as e:
    print(f"LLM initialization failed: {e}")
    raise

login_agent = Agent(
    role='Notion Login Automator',
    goal='Log in to Notion using Google authentication and verify successful access to the dashboard.',
    backstory=(
        'Expert in web automation, specifically skilled in using Playwright to handle '
        'complex login flows, including OAuth providers like Google. '
        'Capable of navigating popups and ensuring the final logged-in state is reached.'
    ),
    tools=[playwright_login_tool], 
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm 
)
