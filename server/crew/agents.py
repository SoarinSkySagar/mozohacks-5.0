from dotenv import load_dotenv
load_dotenv()

from textwrap import dedent
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model='gemini-pro', verbose=True, temperature=0.9,google_api_key="AIzaSyAh-36X7c0aMzbxQB0B_CxPZ8UcctQqzHA")

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
            backstory='Skilled in user experience design and ensuring optimal usability can make figma files or coode css  based on the website.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )
    
    def junior_scraper_agent(self):
        return Agent(
            role='Junior Scraper Agent',
            goal='Scrape the internet for relevant information',
            backstory='Proficient in web scraping and gathering data from various sources.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def senior_scraper_agent(self):
        return Agent(
            role='Senior Scraper Agent',
            goal='Evaluate and filter scraped information',
            backstory='Experienced in analyzing and curating relevant data from various sources.',
            verbose=True,
            allow_delegation=True,
            llm=llm
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
            allow_delegation=True,
            llm=llm
        )

    def devrel_agent(self):
        return Agent(
            role='Senior Developer Engineer',
            goal='Write code and ensure best practices are followed',
            backstory='Skilled in developer  practices and write best quality code while maintaining their quality.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    # Website Development Agents
    def frontend_junior_agent(self):
        return Agent(
            role='Frontend Junior Developer',
            goal='Develop basic frontend components and features',
            backstory=' developer  with knowledge of HTML, CSS, and JavaScript who can write code for the website.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def frontend_senior_agent(self):
        return Agent(
            role='Frontend Senior Developer',
            goal='Lead frontend development and ensure best practices',
            backstory='Experienced frontend developer with  knowledge of HTML, CSS, and JavaScript expertise in modern frameworks and toolsand can evaluate and correct the code.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )


    def backend_junior_agent(self):
        return Agent(
            role='Backend Junior Developer',
            goal='Develop basic backend components and APIs',
            backstory='Junior developer with knowledge of server-side programming languages like node jjs who can write quality code without error and databases.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def main_backend_agent(self):
        return Agent(
            role='Main Backend Developer',
            goal='Develop and maintain the core backend systems',
            backstory='Experienced backend developer with expertise in server architecture and scalability can read and evaluuate code which is written then can correct it or optimise it.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )

    def integration_dev_agent(self):
        return Agent(
            role='Integration Developer',
            goal='Integrate frontend and backend components',
            backstory='Developer skilled in connecting the frontend and backend of the website code which he is provided with.',
            verbose=True,
            allow_delegation=True,
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
            goal='evaluate and write code for the project',
            backstory='Highly skilled developer with expertise in software engineering and can write and optimise quality code.',
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