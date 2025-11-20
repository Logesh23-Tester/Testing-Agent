import os
import datetime
import subprocess
import sys

def run_tests():
    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create report directories
    base_report_dir = "reports"
    run_dir = os.path.join(base_report_dir, timestamp)
    screenshot_dir = os.path.join(run_dir, "screenshots")
    
    os.makedirs(screenshot_dir, exist_ok=True)
    
    print(f"Starting test run. Reports will be saved to: {run_dir}")
    
    # Set environment variable for conftest.py to read
    os.environ["SCREENSHOT_DIR"] = os.path.abspath(screenshot_dir)
    
    # Define report path
    report_path = os.path.join(run_dir, "report.html")
    
    # Run pytest
    cmd = [
        sys.executable, "-m", "pytest",
        "test_ui_automation.py",
        f"--html={report_path}",
        "--self-contained-html"
    ]
    
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("Tests passed successfully.")
    else:
        print("Tests failed.")
        
    print(f"Report generated: {report_path}")

if __name__ == "__main__":
    run_tests()
