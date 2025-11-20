from crewai import Task

class TestingTasks:
    def requirement_analysis_task(self, agent, url):
        return Task(
            description=f'Analyze the webpage at {url}. Identify all input fields, buttons, and functionalities. Summarize the testing requirements.',
            expected_output='A detailed requirement document summarizing the page functionality and testing needs.',
            agent=agent
        )

    def test_scenario_task(self, agent):
        return Task(
            description='Based on the requirements provided by the previous agent, create a list of test scenarios. Include positive, negative, and boundary scenarios.',
            expected_output='A list of test scenarios.',
            agent=agent
        )

    def test_case_task(self, agent):
        return Task(
            description='Convert the test scenarios into detailed test cases. Save them to `test_cases.md`.',
            expected_output='A file `test_cases.md` containing detailed test cases.',
            agent=agent
        )

    def ui_automation_task(self, agent):
        return Task(
            description='Write Python Selenium code to automate the UI test cases. Save the code to `ui_automation.py`. Ensure the code is complete and runnable. Use `webdriver_manager` to manage the driver.',
            expected_output='A Python file `ui_automation.py` containing the Selenium code.',
            agent=agent
        )

    def api_automation_task(self, agent):
        return Task(
            description='Write Python code to automate API tests if applicable. Save the code to `api_automation.py`. If no API is found, create a file stating that.',
            expected_output='A Python file `api_automation.py`.',
            agent=agent
        )

    def db_automation_task(self, agent):
        return Task(
            description='Write Python code to automate Database tests if applicable. Save the code to `db_automation.py`. If no DB is found, create a file stating that.',
            expected_output='A Python file `db_automation.py`.',
            agent=agent
        )

    def code_review_task(self, agent):
        return Task(
            description='Review the generated `ui_automation.py`, `api_automation.py`, and `db_automation.py`. Provide feedback on code style, potential bugs, and improvements.',
            expected_output='A code review report.',
            agent=agent
        )

    def code_quality_task(self, agent):
        return Task(
            description='Check the generated code for PEP8 compliance and other quality standards. Provide a quality report.',
            expected_output='A code quality report.',
            agent=agent
        )

    def runner_task(self, agent):
        return Task(
            description='Execute the `ui_automation.py` script using the Python execution tool. Capture the output and any errors. Generate a final report `final_report.md` summarizing the execution results.',
            expected_output='A final report `final_report.md` and the execution output.',
            agent=agent
        )
