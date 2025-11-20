# 🤖 Autonomous Multi-Agent Testing Framework

A powerful, self-healing automated testing system powered by **CrewAI**, **Selenium**, and **Pytest**. This framework uses a team of AI agents to autonomously analyze web applications, generate test cases, write automation code, and execute tests with detailed reporting.

## 🚀 Key Features

*   **Multi-Agent Architecture**: 9 specialized AI agents handle everything from requirement gathering to reporting.
*   **Autonomous Code Generation**: Automatically generates Page Object Model (POM) based Selenium scripts.
*   **Self-Healing Capabilities**: Agents can detect selector issues and regenerate code to fix broken tests.
*   **Comprehensive Reporting**: Generates timestamped HTML reports with embedded logs and screenshots.
*   **Visual Debugging**: Automatically captures screenshots for every test step (passed or failed).
*   **Model Agnostic**: Supports both Google Gemini and OpenAI models.

## 🏗️ Architecture

The system is orchestrated by **CrewAI** and consists of the following agents:

1.  **Requirement Understander**: Analyzes the target webpage to understand form fields and logic.
2.  **Test Scenario Builder**: Creates high-level test scenarios (Positive, Negative, Boundary).
3.  **Test Case Builder**: Converts scenarios into detailed test steps.
4.  **UI Automation Coder**: Writes Python Selenium code using the Page Object Model.
5.  **Code Reviewer**: Reviews the generated code for best practices.
6.  **Runner & Reporter**: Executes the tests and compiles the final report.

## 🛠️ Prerequisites

*   Python 3.10+
*   Google Chrome (latest version)
*   Git

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Logesh23-Tester/Testing-Agent.git
    cd Testing-Agent
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    Create a `.env` file in the root directory and add your API keys:
    ```ini
    # Choose your model provider
    MODEL=gemini/gemini-1.5-pro-latest
    # MODEL=gpt-4o

    # API Keys
    GOOGLE_API_KEY=your_google_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

## ▶️ Usage

### Run the Full Agent Workflow
To start the agents and generate new tests from scratch:
```bash
python main.py
```

### Run Existing Tests
To execute the generated test suite without re-running the agents:
```bash
python run_tests.py
```
This will:
1.  Execute `test_ui_automation.py`.
2.  Create a timestamped folder in `reports/`.
3.  Save the HTML report and screenshots.

## 📊 Reporting

Reports are generated in the `reports/` directory. Open the `report.html` file in any browser to view:
*   Test Execution Status (Pass/Fail)
*   Detailed Execution Logs
*   Screenshots of the application state

## 📁 Project Structure

```
Testing-Agent/
├── agents.py           # Agent definitions and configurations
├── tasks.py            # Task definitions for each agent
├── tools.py            # Custom tools (File I/O, Selenium)
├── main.py             # Entry point for the CrewAI system
├── run_tests.py        # Script to run generated tests with reporting
├── test_ui_automation.py # Generated Selenium test script (Pytest)
├── conftest.py         # Pytest configuration (Screenshots, Hooks)
├── requirements.txt    # Python dependencies
├── reports/            # Generated test reports
└── .env                # Environment variables (Not committed)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
