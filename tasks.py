from crewai import Task
from agents import login_agent

login_task = Task(
    description=(
        "Use the 'playwright_login_tool' to log in to Notion. "
        "The Notion URL is '{notion_url}'. "
        "Use the username '{notion_email}' and password '{notion_password}' for the Google login flow. "
        "Carefully follow the steps to navigate the main page, click the 'Log in' link, "
        "handle the 'Continue with Google' popup, input credentials in the Google popup, "
        "and wait for the final Notion dashboard to load. "
        "Report the final status of the login, including the URL if successful or any errors encountered."
    ),
    expected_output=(
        "A clear message indicating 'Successfully logged into Notion' along with the final URL, "
        "or a detailed error message explaining why the login failed, including any Google-specific errors."
    ),
    agent=login_agent
)