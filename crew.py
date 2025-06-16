from crewai import Crew
from agents import login_agent
from tasks import login_task
from dotenv import load_dotenv
import os

load_dotenv()

notion_crew = Crew(
    agents=[login_agent],
    tasks=[login_task],
    verbose=True,
    max_rpm=None 
)

inputs = {
    'notion_url': os.getenv("NOTION_URL"),
    'notion_email': os.getenv("GOOGLE_EMAIL"),
    'notion_password': os.getenv("GOOGLE_PASSWORD")
}

print("Attempting to log in to Notion...")
result = notion_crew.kickoff(inputs=inputs)
print("\n--- Login Automation Result ---")
print(result)