from textwrap import dedent
from crewai import Task

from dotenv import load_dotenv
load_dotenv()

class WebDev():
    def evaluation_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Evaluate an existing website for improvements and enhancements.
                    Project Idea: {project_idea}
                    Tasks:
                    1. Analyze the current website's user experience and performance metrics.
                    2. Identify areas for improvement in design, functionality, and responsiveness.
                    3. Develop a plan for implementing enhancements and optimizations.
                    4. Implement the planned changes and improvements.
                    5. Test the updated website thoroughly to ensure functionality and performance.
                    6. Deploy the enhanced website and monitor user feedback and analytics.
                """),
            expected_output="An enhanced and optimized website with improved user experience and performance.",
            agent=agent
        )
    
    def code_development_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Develop a fully functional website with a modern and intuitive user interface.
                    Project Idea: {project_idea}
                    Tasks:
                    1. Conduct user research and gather requirements.
                    2. Design the user interface and user experience (UI/UX).
                    3. Develop the frontend components and features using HTML, CSS, and JavaScript.
                    4. Develop the backend systems and APIs using a backend framework like Django or Flask.
                    5. Integrate frontend and backend components for seamless communication.
                    6. Thoroughly test the website using automated and manual testing methods.
                    7. Deploy the website to a hosting platform (e.g., AWS, Heroku) and optimize for performance.
                    
                    Example Code:
                    # HTML code for a basic webpage
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <title>My Website</title>
                        </head>
                        <body>
                            <h1>Welcome to My Website</h1>
                            <p>This is a sample webpage.</p>
                        </body>
                    </html>
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
                    1. Conduct functional testing to ensure all features work as intended.
                    2. Perform performance testing to measure website speed and responsiveness.
                    3. Test compatibility across different browsers, devices, and screen sizes.
                    4. Identify and fix any bugs or issues discovered during testing.
                    5. Document test results and prepare a test report with recommendations.
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
                    1. Analyze the current app's user experience and performance metrics.
                    2. Identify areas for improvement in design, functionality, and usability.
                    3. Develop a plan for implementing enhancements and optimizations.
                    4. Implement the planned changes and improvements.
                    5. Test the updated app thoroughly to ensure functionality and usability.
                    6. Deploy the enhanced app and monitor user feedback and analytics.
                """),
            expected_output="An enhanced and optimized mobile application with improved user experience and performance.",
            agent=agent
        )
    
    def code_development_task(self, agent, project_idea):
        return Task(
            description=dedent(f"""\
                    Develop a feature-rich and user-friendly mobile application.
                    Project Idea: {project_idea}
                    Tasks:
                    1. Gather requirements from stakeholders and define the app's functionality.
                    2. Design the user interface (UI) and user experience (UX) for mobile devices.
                    3. Develop the frontend components and features for the mobile app using frameworks like React Native.
                    4. Develop the backend systems and APIs using technologies like Node.js or Firebase.
                    5. Integrate frontend and backend components for seamless functionality.
                    6. Perform thorough testing on various devices and platforms to ensure app quality.
                    7. Deploy the app to app stores (e.g., Google Play Store, Apple App Store) and optimize for performance.
                    

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
                    1. Conduct functional testing to ensure all features work as intended.
                    2. Perform usability testing to evaluate user experience and interface design.
                    3. Test performance on various devices and platforms for speed and responsiveness.
                    4. Identify and fix any bugs or issues discovered during testing.
                    5. Document test results and prepare a test report with recommendations.
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
                    1. Analyze the current game's gameplay, mechanics, and user experience.
                    2. Identify areas for improvement in graphics, sound, controls, and gameplay flow.
                    3. Develop a plan for implementing enhancements and optimizations.
                    4. Implement the planned changes and improvements in the game code.
                    5. Test the updated game thoroughly to ensure enhanced gameplay and user experience.
                    6. Deploy the enhanced game and gather feedback from players for further improvements.
                """),
            expected_output="An enhanced and optimized game with improved gameplay and user experience.",
            agent=agent
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
