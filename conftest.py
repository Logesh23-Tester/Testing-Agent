import pytest
from datetime import datetime
import pytest_html
import os

def pytest_html_report_title(report):
    report.title = "Automation Test Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        # Check if driver fixture is present
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            try:
                screenshot_base64 = driver.get_screenshot_as_base64()
                
                # Save to file if SCREENSHOT_DIR is set
                screenshot_dir = os.environ.get("SCREENSHOT_DIR")
                if screenshot_dir:
                    timestamp = datetime.now().strftime("%H-%M-%S")
                    filename = f"{item.name}_{timestamp}.png"
                    filepath = os.path.join(screenshot_dir, filename)
                    driver.save_screenshot(filepath)
                
                # Embed screenshot directly in report
                extra.append(pytest_html.extras.image(screenshot_base64, "Screenshot"))
            except Exception as e:
                extra.append(pytest_html.extras.text(f"Failed to capture screenshot: {e}"))
        
        report.extra = extra
