from dotenv import load_dotenv
load_dotenv()
from crewai_tools import SerperDevTool

from textwrap import dedent
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model='gemini-pro', verbose=True, temperature=0.1)
tool = SerperDevTool()

class ProjectAgents():
    def input_agent(self):
        return Agent(
            role='Input Agent',
            goal=f'Decide which development crew should work on the project',
            backstory='Experienced in assessing project requirements and allocating resources.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )
    
    def ui_ux_agent(self):
        return Agent(
            role='UI/UX Agent',
            goal='Design intuitive and engaging user interfaces',
            backstory='Skilled in user experience design and ensuring optimal usability.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    
    def junior_scraper_agent(self):
        return Agent(
            role='Junior Scraper Agent',
            goal='Scrape the internet for relevant information',
            backstory='Proficient in web scraping and gathering data from various sources.',
            verbose=True,
            allow_delegation=False,
            llm=llm,
            tool=tool
        )

    def senior_scraper_agent(self):
        return Agent(
            role='Senior Scraper Agent',
            goal='Evaluate and filter scraped information',
            backstory='Experienced in analyzing and curating relevant data from various sources.',
            verbose=True,
            allow_delegation=False,
            llm=llm,
            tool=tool
        )

    def cto_agent(self):
        return Agent(
            role='Chief Technology Officer',
            goal='Oversee and verify the technical aspects of the project',
            backstory='Seasoned technology leader with expertise in project management and quality assurance.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def ceo_agent(self):
        return Agent(
            role='Chief Executive Officer',
            goal='Manage customer relations and ensure project delivery',
            backstory='Experienced in leading organizations, building relationships, and delivering successful projects.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def devrel_agent(self):
        return Agent(
            role='Developer Relations',
            goal='Facilitate communication and collaboration between developers',
            backstory='Skilled in fostering developer communities and promoting best practices.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    # Website Development Agents
    def frontend_junior_agent(self):
        return Agent(
            role='Frontend Junior Developer',
            goal='Develop basic frontend components and features',
            backstory='Junior developer with knowledge of HTML, CSS, and JavaScript.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def frontend_senior_agent(self):
        return Agent(
            role='Frontend Senior Developer',
            goal='Lead frontend development and ensure best practices',
            backstory='Experienced frontend developer with expertise in modern frameworks and tools.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def lead_frontend_agent(self):
        return Agent(
            role='Lead Frontend Developer',
            goal='Oversee and coordinate frontend development efforts',
            backstory='Highly skilled frontend developer with leadership and project management experience.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def backend_junior_agent(self):
        return Agent(
            role='Backend Junior Developer',
            goal='Develop basic backend components and APIs',
            backstory='Junior developer with knowledge of server-side programming languages and databases.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def main_backend_agent(self):
        return Agent(
            role='Main Backend Developer',
            goal='Develop and maintain the core backend systems',
            backstory='Experienced backend developer with expertise in server architecture and scalability.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def integration_dev_agent(self):
        return Agent(
            role='Integration Developer',
            goal='Integrate frontend and backend components',
            backstory='Developer skilled in connecting various systems and ensuring seamless communication.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def tester_agent(self):
        return Agent(
            role='Tester',
            goal='Ensure application quality through thorough testing',
            backstory='Experienced in testing software applications and identifying bugs and issues.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def senior_developer_agent(self):
        return Agent(
            role='Senior Developer',
            goal='Oversee development efforts and ensure best practices',
            backstory='Highly skilled developer with expertise in software architecture and team leadership.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    # App Development Agents
    def junior_fe_agent(self):
        return Agent(
            role='Junior Frontend Developer',
            goal='Develop basic frontend components for mobile apps',
            backstory='Junior developer with knowledge of mobile app frameworks and UI/UX design.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def senior_fe_agent(self):
        return Agent(
            role='Senior Frontend Developer',
            goal='Lead frontend development and ensure best practices for mobile apps',
            backstory='Experienced frontend developer with expertise in mobile app development and performance optimization.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def backend_dev_agent(self):
        return Agent(
            role='Backend Developer',
            goal='Develop and maintain backend systems for mobile apps',
            backstory='Developer skilled in server-side programming and integration with mobile app frameworks.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def app_tester_agent(self):
        return Agent(
            role='App Tester',
            goal='Ensure mobile app quality through thorough testing',
            backstory='Experienced in testing mobile applications on various devices and platforms.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    # Game Development Agents
    def junior_game_dev_agent(self):
        return Agent(
            role='Junior Game Developer',
            goal='Develop basic game features and components',
            backstory='Junior developer with knowledge of game engines and programming languages.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def senior_game_dev_agent(self):
        return Agent(
            role='Senior Game Developer',
            goal='Lead game development and ensure best practices',
            backstory='Experienced game developer with expertise in game design, mechanics, and optimization.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def game_tester_agent(self):
        return Agent(
            role='Game Tester',
            goal='Ensure game quality through thorough testing',
            backstory='Experienced in testing games across various platforms and identifying bugs and issues.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )