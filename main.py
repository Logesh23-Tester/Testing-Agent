from crewai import Crew, Process
from agents import TestingAgents
from tasks import TestingTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run():
    url = "https://demo.automationtesting.in/Register.html"
    
    agents = TestingAgents()
    tasks = TestingTasks()

    # Instantiate Agents
    req_agent = agents.requirement_agent()
    scenario_agent = agents.scenario_agent()
    case_agent = agents.test_case_agent()
    ui_agent = agents.ui_automation_agent()
    api_agent = agents.api_automation_agent()
    db_agent = agents.db_automation_agent()
    reviewer_agent = agents.code_reviewer_agent()
    quality_agent = agents.code_quality_agent()
    runner_agent = agents.runner_agent()

    # Instantiate Tasks
    req_task = tasks.requirement_analysis_task(req_agent, url)
    scenario_task = tasks.test_scenario_task(scenario_agent)
    case_task = tasks.test_case_task(case_agent)
    ui_task = tasks.ui_automation_task(ui_agent)
    api_task = tasks.api_automation_task(api_agent)
    db_task = tasks.db_automation_task(db_agent)
    review_task = tasks.code_review_task(reviewer_agent)
    quality_task = tasks.code_quality_task(quality_agent)
    run_task = tasks.runner_task(runner_agent)

    # Form the Crew
    crew = Crew(
        agents=[
            req_agent, scenario_agent, case_agent, 
            ui_agent, api_agent, db_agent, 
            reviewer_agent, quality_agent, runner_agent
        ],
        tasks=[
            req_task, scenario_task, case_task, 
            ui_task, api_task, db_task, 
            review_task, quality_task, run_task
        ],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print("######################")
    print("## Crew Execution Result ##")
    print("######################")
    print(result)

if __name__ == "__main__":
    run()
