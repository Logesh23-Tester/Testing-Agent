import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RegistrationForm:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_address(self, address):
        address_field = self.driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
        address_field.clear()
        address_field.send_keys(address)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.XPATH, "//input[@type='email']")
        email_field.clear()
        email_field.send_keys(email)

    def enter_phone(self, phone):
        phone_field = self.driver.find_element(By.XPATH, "//input[@type='tel']")
        phone_field.clear()
        phone_field.send_keys(phone)

    def select_gender(self, gender):
        if gender.lower() == 'male':
            male_radio = self.driver.find_element(By.XPATH, "//input[@value='Male']")
            male_radio.click()
        elif gender.lower() == 'female':
            female_radio = self.driver.find_element(By.XPATH, "//input[@value='FeMale']")
            female_radio.click()

    def select_hobbies(self, hobbies):
        if 'cricket' in hobbies:
            cricket_checkbox = self.driver.find_element(By.ID, "checkbox1")
            if not cricket_checkbox.is_selected():
                cricket_checkbox.click()
        if 'movies' in hobbies:
            movies_checkbox = self.driver.find_element(By.ID, "checkbox2")
            if not movies_checkbox.is_selected():
                movies_checkbox.click()
        if 'hockey' in hobbies:
            hockey_checkbox = self.driver.find_element(By.ID, "checkbox3")
            if not hockey_checkbox.is_selected():
                hockey_checkbox.click()

    def select_skills(self, skill):
        try:
            skills_dropdown = Select(self.driver.find_element(By.ID, "Skills"))
            skills_dropdown.select_by_visible_text(skill)
        except:
            pass # Optional field

    def select_country(self, country):
        # This is the 'Country' dropdown, not 'Select Country'
        try:
            country_dropdown = Select(self.driver.find_element(By.ID, "countries"))
            country_dropdown.select_by_visible_text(country)
        except:
            pass

    def select_country_search(self, country):
        # This is the searchable dropdown
        try:
            span = self.driver.find_element(By.XPATH, "//span[@role='combobox']")
            span.click()
            # This part is tricky without more inspection, skipping for now or assuming simple click
        except:
            pass

    def select_date_of_birth(self, year, month, day):
        try:
            year_dropdown = Select(self.driver.find_element(By.ID, "yearbox"))
            year_dropdown.select_by_visible_text(year)

            month_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@placeholder='Month']"))
            month_dropdown.select_by_visible_text(month)

            day_dropdown = Select(self.driver.find_element(By.ID, "daybox"))
            day_dropdown.select_by_visible_text(day)
        except:
            pass

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "firstpassword")
        password_field.clear()
        password_field.send_keys(password)

    def confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element(By.ID, "secondpassword")
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)

    def click_submit(self):
        submit_button = self.driver.find_element(By.ID, "submitbtn")
        submit_button.click()

    def click_refresh(self):
        refresh_button = self.driver.find_element(By.ID, "Button1")
        refresh_button.click()

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("http://demo.automationtesting.in/Register.html")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def registration_form(driver):
    return RegistrationForm(driver)

def test_p1_successful_registration(driver, registration_form):
    """P1: Successful Registration with Valid Data"""
    logger.info("Starting P1: Successful Registration with Valid Data")
    registration_form.enter_first_name("John")
    registration_form.enter_last_name("Doe")
    registration_form.enter_address("123 Main St")
    registration_form.enter_email("john.doe@example.com")
    registration_form.enter_phone("1234567890")
    registration_form.select_gender("male")
    registration_form.select_hobbies(['cricket', 'movies'])
    registration_form.select_skills("Java")
    registration_form.select_country("India")
    registration_form.select_date_of_birth("1990", "January", "1")
    registration_form.enter_password("P@$$wOrd")
    registration_form.confirm_password("P@$$wOrd")
    registration_form.click_submit()
    time.sleep(2)
    # Add assertion here if possible, e.g., check URL change or success message

def test_p2_registration_min_fields(driver, registration_form):
    """P2: Registration with Minimum Required Fields Only"""
    logger.info("Starting P2: Registration with Minimum Required Fields Only")
    registration_form.enter_first_name("Jane")
    registration_form.enter_last_name("Doe")
    registration_form.enter_address("456 Elm St")
    registration_form.enter_email("jane.doe@example.com")
    registration_form.enter_phone("9876543210")
    registration_form.select_gender("female")
    registration_form.select_country("United States of America")
    registration_form.select_date_of_birth("1985", "February", "15")
    registration_form.enter_password("AnotherP@ss")
    registration_form.confirm_password("AnotherP@ss")
    registration_form.click_submit()
    time.sleep(2)

def test_n1_missing_email(driver, registration_form):
    """N1: Missing Required Fields (Email)"""
    logger.info("Starting N1: Missing Required Fields (Email)")
    registration_form.enter_first_name("Test")
    registration_form.enter_last_name("User")
    registration_form.enter_address("789 Oak St")
    registration_form.enter_phone("1122334455")
    registration_form.select_gender("male")
    registration_form.select_country("Australia")
    registration_form.select_date_of_birth("2000", "March", "10")
    registration_form.enter_password("ShortPass")
    registration_form.confirm_password("ShortPass")
    registration_form.click_submit()
    time.sleep(2)
    # Check for validation error if possible

def test_f1_refresh_functionality(driver, registration_form):
    """F1: Refresh Button Functionality"""
    logger.info("Starting F1: Refresh Button Functionality")
    registration_form.enter_first_name("Before")
    registration_form.enter_last_name("Refresh")
    registration_form.click_refresh()
    first_name_field = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    assert first_name_field.get_attribute("value") == "", "First Name field was not cleared after refresh"
