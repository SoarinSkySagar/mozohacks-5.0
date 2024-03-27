from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Crew, Process

from tasks import DevelopmentTasks
from agents import DevelopmentAgents

# Set up the language model
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.5,
                             google_api_key="AIzaSyAh-36X7c0aMzbxQB0B_CxPZ8UcctQqzHA")

tasks = DevelopmentTasks()
agents = DevelopmentAgents()

print("## Welcome to the Development Crew")
print('-------------------------------')

project_type = input("What type of project do you want to develop? (website, app, game): ")

# Ask for project idea
project_idea = input("Please describe your project idea: ")
input_agent = agents.input_agent(project_idea)
ui_ux_agent = agents.ui_ux_agent(project_idea)
junior_scraper_agent = agents.junior_scraper_agent()
senior_scraper_agent = agents.senior_scraper_agent()
cto_agent = agents.cto_agent()
ceo_agent = agents.ceo_agent()
devrel_agent = agents.devrel_agent()

# Create Tasks
if project_type == "website":
    development_task = tasks.website_development_task(cto_agent, project_idea)
    development_agents = [ui_ux_agent, agents.frontend_junior_agent(), agents.frontend_senior_agent(),
                          agents.lead_frontend_agent(), agents.backend_junior_agent(), agents.main_backend_agent(),
                          agents.integration_dev_agent(), agents.tester_agent(), agents.senior_developer_agent()]
elif project_type == "app":
    development_task = tasks.app_development_task(cto_agent, project_idea)
    development_agents = [agents.junior_fe_agent(), agents.senior_fe_agent(), agents.backend_dev_agent(), agents.app_tester_agent()]
elif project_type == "game":
    development_task = tasks.game_development_task(cto_agent, project_idea)
    development_agents = [agents.junior_game_dev_agent(), agents.senior_game_dev_agent(), agents.game_tester_agent()]
else:
    print("Invalid project type. Please try again.")
    exit()

# Create Crew
development_crew = Crew(
    agents=development_agents + [input_agent, ui_ux_agent, junior_scraper_agent, senior_scraper_agent, cto_agent, ceo_agent, devrel_agent],
    tasks=[development_task],
    verbose=True,
    process=Process.sequential
)

print(f"Input Agent: Assigning {project_type.capitalize()} Development Crew")
development_result = development_crew.kickoff()

# Print results
print("\n\n################################################")
print("## Development Result")
print("################################################\n")
print(development_result)