from textwrap import dedent
from crewai import Task
from crewai_tools import SerperDevTool
tool = SerperDevTool()

from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup
import requests


class WebDev():
    def evaluation_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Evaluate an existing website for improvements and enhancements.
                    Project Idea: {project_idea}
                    Tasks:
                     Analyze the current website's user experience and performance metrics.
                     Identify areas for improvement in design, functionality, and responsiveness.
                     Develop a plan for implementing enhancements and optimizations.
                     Implement the planned changes and improvements.
                     Test the updated website thoroughly to ensure functionality and performance.
                     Deploy the enhanced website and monitor user feedback and analytics.
                """),
            expected_output="An enhanced and optimized website with improved user experience and performance.",
            agent=agent
        )
    
    def scrape_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                Based on the project idea: {project_idea} scrape data from the web. 
                
                """),
            expected_output="",
            agent=agent
        )
    
    def code_development_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Develop a fully functional website with a modern and intuitive user interface.
                    Project Idea: {project_idea}
                    Tasks:write error free code fro the requested project
                    
                    """),
            expected_output='A high-quality, responsive, and well-tested website.',
            agent=agent
        )
    
    def testing_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Test the functionality, performance, and compatibility of a website.
                    Project Idea: {project_idea}
                    Tasks:
                    Conduct functional testing to ensure all features work as intended.
                     Perform performance testing to measure website speed and responsiveness.
                     Test compatibility across different browsers, devices, and screen sizes.
                     Identify and fix any bugs or issues discovered during testing.
                     Document test results and prepare a test report with recommendations.
                """),
            expected_output="A thoroughly tested website with documented test results and recommendations.",
            agent=agent
        )
    
    
    
    
    
    
    
class AppDev():
    def evaluation_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Evaluate an existing mobile application for improvements and enhancements.
                    Project Idea: {project_idea}
                    Tasks:
                     Analyze the current app's user experience and performance metrics.
                     Identify areas for improvement in design, functionality, and usability.
                     Develop a plan for implementing enhancements and optimizations.
                     Implement the planned changes and improvements.
                     Test the updated app thoroughly to ensure functionality and usability.
                     Deploy the enhanced app and monitor user feedback and analytics.
                """),
            expected_output="An enhanced and optimized mobile application with improved user experience and performance.",
            agent=agent
        )
        
    def scrape_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                Based on the project idea: {project_idea} scrape data from the web. 
                
                """),
            expected_output="",
            agent=agent
        )    
    
    def code_development_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Develop a feature-rich and user-friendly mobile application.
                    Project Idea: {project_idea}
                    Tasks:
                     Gather requirements from stakeholders and define the app's functionality.
                     Design the user interface (UI) and user experience (UX) for mobile devices.
                     Develop the frontend components and features for the mobile app using frameworks like React Native.
                     Develop the backend systems and APIs using technologies like Node.js or Firebase.
                     Integrate frontend and backend components for seamless functionality.
                     Perform thorough testing on various devices and platforms to ensure app quality.
                     Deploy the app to app stores (e.g., Google Play Store, Apple App Store) and optimize for performance.
                    

                    export default LoginScreen;
                """),
            expected_output='A high-quality, user-friendly, and well-tested mobile application.',
            agent=agent
        )
    
    def testing_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Test the functionality, usability, and performance of a mobile application.
                    Project Idea: {project_idea}
                    Tasks:
                     Conduct functional testing to ensure all features work as intended.
                     Perform usability testing to evaluate user experience and interface design.
                     Test performance on various devices and platforms for speed and responsiveness.
                     Identify and fix any bugs or issues discovered during testing.
                     Document test results and prepare a test report with recommendations.
                """),
            expected_output="A thoroughly tested mobile application with documented test results and recommendations.",
            agent=agent
        )
    
class GameDev():
    def evaluation_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Evaluate an existing game for improvements and enhancements.
                    Project Idea: {project_idea}
                    Tasks:
                     Analyze the current game's gameplay, mechanics, and user experience.
                     Identify areas for improvement in graphics, sound, controls, and gameplay flow.
                     Develop a plan for implementing enhancements and optimizations.
                     Implement the planned changes and improvements in the game code.
                     Test the updated game thoroughly to ensure enhanced gameplay and user experience.
                     Deploy the enhanced game and gather feedback from players for further improvements.
                """),
            expected_output="An enhanced and optimized game with improved gameplay and user experience.",
            agent=agent
        )
    
    def scrape_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                Based on the project idea: {project_idea} scrape data from the web. 
                Based on the project idea: {project_idea}, scrape data from the web. 
        The data to be scraped includes article titles and URLs from a news website, reddit, youtube videos , medium, hashnode blogs. Give it in tabular form

                """),
            expected_output="A tabular data of the available resources scraped, urls of youtube videos, medium, hashnode blogs, reddit posts etc",
            agent=agent,
            tool=tool
            
        )
    def code_development_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Develop an engaging and immersive game experience.
                    Project Idea: {project_idea}
                    Tasks:
                    1. Define the game concept, storyline, mechanics, and levels in collaboration with game designers.
                    2. Design the game graphics, animations, and user interfaces (UI) for an immersive experience.
                    3. Develop the game features, mechanics, and components using game engines like Unity or Unreal Engine.
                    4. Integrate game assets, animations, and sound effects for a captivating gameplay experience.
                    5. Optimize game performance for various platforms (PC, mobile, consoles) and ensure cross-platform compatibility.
                    6. Perform thorough testing (functional, performance, compatibility) to identify and fix bugs and issues.
                    7. Deploy the game to distribution platforms (Steam, App Store, Google Play) and promote it through marketing channels.
                    
                """),
            expected_output='A high-quality, engaging, and well-tested game.',
            agent=agent
        )
    
    def testing_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Test the functionality, performance, and compatibility of a game.
                    Project Idea: {project_idea}
                    Tasks:
                    1. Conduct functional testing to ensure all game features work as intended.
                    2. Perform performance testing to measure game speed, graphics quality, and responsiveness.
                    3. Test compatibility across different gaming platforms (PC, mobile, consoles).
                    4. Identify and fix any bugs or issues discovered during testing.
                    5. Document test results and prepare a test report with recommendations.
                """),
            expected_output="A thoroughly tested game with documented test results and recommendations.",
            agent=agent
        )
