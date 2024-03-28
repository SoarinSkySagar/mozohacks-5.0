from crewai import Crew

from .tasks import AppDev, GameDev, WebDev
from .agents import ProjectAgents

agents = ProjectAgents()

input_agent = agents.input_agent()
ui_ux_agent = agents.ui_ux_agent()
junior_scraper_agent = agents.junior_scraper_agent()
senior_scraper_agent = agents.senior_scraper_agent()
cto_agent = agents.cto_agent()
ceo_agent = agents.ceo_agent()
devrel_agent = agents.devrel_agent()
frontend_junior_agent = agents.frontend_junior_agent()
frontend_senior_agent = agents.frontend_senior_agent()
lead_frontend_agent = agents.lead_frontend_agent()
backend_junior_agent = agents.backend_junior_agent()
main_backend_agent = agents.main_backend_agent()
integration_dev_agent = agents.integration_dev_agent()
tester_agent = agents.tester_agent()
senior_developer_agent = agents.senior_developer_agent()
junior_fe_agent = agents.junior_fe_agent()
senior_fe_agent = agents.senior_fe_agent()
backend_dev_agent = agents.backend_dev_agent()
app_tester_agent = agents.app_tester_agent()
junior_game_dev_agent = agents.junior_game_dev_agent()
senior_game_dev_agent = agents.senior_game_dev_agent()
game_tester_agent = agents.game_tester_agent()

def create_project(project_type, project_idea):

    if project_type == "website":
        tasks = WebDev()
    elif project_type == "app":
        tasks = AppDev()
    elif project_type == "game":
        tasks = GameDev()

    evaluation_task = tasks.evaluation_task(senior_scraper_agent, project_idea)

    if project_type == "website":
        code_task = tasks.code_development_task(frontend_senior_agent, project_idea)
        testing_task = tasks.testing_task(tester_agent, project_idea)
        agentsArr = [senior_scraper_agent, frontend_senior_agent, tester_agent]
    elif project_type == "app":
        code_task = tasks.code_development_task(senior_fe_agent, project_idea)
        testing_task = tasks.testing_task(app_tester_agent, project_idea)
        agentsArr = [senior_scraper_agent, senior_fe_agent, app_tester_agent]
    else:
        code_task = tasks.code_development_task(senior_game_dev_agent, project_idea)
        testing_task = tasks.testing_task(game_tester_agent, project_idea)
        agentsArr = [senior_scraper_agent, senior_game_dev_agent, game_tester_agent]

    crew = Crew(
        agents= agentsArr,
        tasks= [
            evaluation_task,
            code_task,
            testing_task
        ],
        verbose=True
    )

    project = crew.kickoff()
    return project