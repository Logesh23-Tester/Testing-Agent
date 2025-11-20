from crewai.tools import BaseTool
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class SeleniumScrapeTool(BaseTool):
    name: str = "Selenium Scraper"
    description: str = "Scrapes the text content of a webpage using Selenium."

    def _run(self, url: str) -> str:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            time.sleep(2) # Wait for page load
            text = driver.find_element(By.TAG_NAME, "body").text
            driver.quit()
            return text
        except Exception as e:
            return f"Error scraping {url}: {str(e)}"


class PythonScriptExecutor(BaseTool):
    name: str = "Python Script Executor"
    description: str = "Executes a Python script given its file path and returns the standard output and standard error."

    def _run(self, script_path: str) -> str:
        if not os.path.exists(script_path):
            return f"Error: File '{script_path}' not found."
        
        try:
            # Capture both stdout and stderr
            result = subprocess.run(
                ["python", script_path],
                capture_output=True,
                text=True
            )
            output = f"Exit Code: {result.returncode}\n"
            output += f"Standard Output:\n{result.stdout}\n"
            if result.stderr:
                output += f"Standard Error:\n{result.stderr}\n"
            return output
        except Exception as e:
            return f"Exception occurred while executing script: {str(e)}"

class FileReadTool(BaseTool):
    name: str = "File Read Tool"
    description: str = "Reads the content of a file."

    def _run(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' not found."
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"

class FileWriteTool(BaseTool):
    name: str = "File Write Tool"
    description: str = "Writes content to a file. Overwrites if exists."

    def _run(self, file_path: str, content: str) -> str:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Successfully wrote to {file_path}"
        except Exception as e:
            return f"Error writing to file: {str(e)}"
