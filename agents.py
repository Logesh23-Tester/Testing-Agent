from crewai import Agent
from tools import PythonScriptExecutor, FileReadTool, FileWriteTool, SeleniumScrapeTool
import os
from dotenv import load_dotenv

load_dotenv()

model_name = os.getenv("MODEL", "gemini/gemini-1.5-pro-latest")
api_key = os.getenv("GOOGLE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Use string model names for CrewAI to leverage LiteLLM directly
if "gpt" in model_name.lower():
    llm = model_name
else:
    # Ensure gemini/ prefix for LiteLLM
    if not model_name.startswith("gemini/"):
        llm = f"gemini/{model_name}"
    else:
        llm = model_name

# Tools
scrape_tool = SeleniumScrapeTool()
file_read_tool = FileReadTool()
file_write_tool = FileWriteTool()
python_executor = PythonScriptExecutor()

class TestingAgents:
    def requirement_agent(self):
        return Agent(
            role='Requirement Understander',
            goal='Analyze the webpage and understand the testing requirements.',
            backstory='You are an expert business analyst. Your job is to visit the given URL, understand the page content, and derive high-level testing requirements.',
            tools=[scrape_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def scenario_agent(self):
        return Agent(
            role='Test Scenario Builder',
            goal='Create comprehensive test scenarios based on requirements.',
            backstory='You are a QA Lead. You take high-level requirements and break them down into detailed test scenarios covering positive, negative, and edge cases.',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def test_case_agent(self):
        return Agent(
            role='Test Case Builder',
            goal='Create detailed test cases from scenarios.',
            backstory='You are a QA Engineer. You convert test scenarios into step-by-step test cases with expected results. You MUST save the test cases to a file named `test_cases.md`.',
            tools=[file_write_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def ui_automation_agent(self):
        return Agent(
            role='UI Automation Coder',
            goal='Write Python Selenium code to automate the UI test cases.',
            backstory='You are a Senior SDET specializing in Selenium and Python. You write robust, clean, and executable code to automate web interactions. You MUST save the code to a file named `ui_automation.py`. Ensure the code uses `webdriver_manager` and runs in headless mode if possible, or standard mode.',
            tools=[file_write_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def api_automation_agent(self):
        return Agent(
            role='API Automation Coder',
            goal='Write Python code to automate API tests if applicable.',
            backstory='You are a Backend SDET. You write Python scripts using `requests` to test APIs. If no API is explicitly found, you state that. If you write code, save it to `api_automation.py`.',
            tools=[file_write_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def db_automation_agent(self):
        return Agent(
            role='DB Automation Coder',
            goal='Write Python code to automate Database tests if applicable.',
            backstory='You are a Database QA Engineer. You write Python scripts to verify database states. If no DB access is provided, you state that. If you write code, save it to `db_automation.py`.',
            tools=[file_write_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def code_reviewer_agent(self):
        return Agent(
            role='Code Reviewer',
            goal='Review the generated automation code for best practices and errors.',
            backstory='You are a Tech Lead. You review code for style, efficiency, and potential bugs. You provide feedback to improve the code.',
            tools=[file_read_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def code_quality_agent(self):
        return Agent(
            role='Code Quality Checker',
            goal='Ensure the code meets quality standards (PEP8, etc.).',
            backstory='You are a Code Quality Specialist. You check for formatting, docstrings, and overall maintainability.',
            tools=[file_read_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def runner_agent(self):
        return Agent(
            role='Runner and Reporter',
            goal='Execute the automation code and generate a final report.',
            backstory='You are a DevOps Engineer. You run the approved scripts using the executor tool, capture the output, and compile a comprehensive report with a dashboard summary. You MUST save the report to `final_report.md`.',
            tools=[python_executor, file_write_tool, file_read_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
