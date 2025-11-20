import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


class RegistrationForm:
    def __init__(self, driver):
        self.driver = driver

    def enter_full_name(self, full_name):
        full_name_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Full Name']")
        full_name_field.send_keys(full_name)

    def enter_address(self, address):
        address_field = self.driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
        address_field.send_keys(address)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.XPATH, "//input[@type='email']")
        email_field.send_keys(email)

    def enter_phone(self, phone):
        phone_field = self.driver.find_element(By.XPATH, "//input[@type='tel']")
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
            cricket_checkbox.click()
        if 'movies' in hobbies:
            movies_checkbox = self.driver.find_element(By.ID, "checkbox2")
            movies_checkbox.click()
        if 'hockey' in hobbies:
            hockey_checkbox = self.driver.find_element(By.ID, "checkbox3")
            hockey_checkbox.click()

    def select_languages(self, languages):
        # This part requires more precise identification, as the element identification is missing.
        pass

    def select_skills(self, skill):
        skills_dropdown = Select(self.driver.find_element(By.ID, "Skills"))
        skills_dropdown.select_by_visible_text(skill)

    def select_country(self, country):
        country_dropdown = Select(self.driver.find_element(By.ID, "countries"))
        country_dropdown.select_by_visible_text(country)

    def select_date_of_birth(self, year, month, day):
        year_dropdown = Select(self.driver.find_element(By.ID, "yearbox"))
        year_dropdown.select_by_visible_text(year)

        month_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@placeholder='Month']"))
        month_dropdown.select_by_visible_text(month)

        day_dropdown = Select(self.driver.find_element(By.ID, "daybox"))
        day_dropdown.select_by_visible_text(day)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "firstpassword")
        password_field.send_keys(password)

    def confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element(By.ID, "secondpassword")
        confirm_password_field.send_keys(confirm_password)

    def click_submit(self):
        submit_button = self.driver.find_element(By.ID, "submitbtn")
        submit_button.click()

    def click_refresh(self):
        refresh_button = self.driver.find_element(By.ID, "Button1")
        refresh_button.click()


def main():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    # Set up the Chrome driver using webdriver_manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the registration page
    driver.get("http://demo.automationtesting.in/Register.html")
    driver.maximize_window()

    # Create an instance of the registration form
    registration_form = RegistrationForm(driver)

    # --- Positive Test Scenarios ---
    print("Running Positive Test Scenarios...")

    # P1: Successful Registration with Valid Data
    print("P1: Successful Registration with Valid Data")
    registration_form.enter_full_name("John Doe")
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
    time.sleep(2)  # Allow time for the page to load

    # Verify successful registration (add assertion here - e.g., check for a success message)
    # For example:
    # success_message = driver.find_element(By.XPATH, "//div[@class='success-message']").text
    # assert "Success!\" in success_message

    driver.get("http://demo.automationtesting.in/Register.html") #navigate back to registration for next test case

    # P2: Registration with Minimum Required Fields Only
    print("P2: Registration with Minimum Required Fields Only")
    registration_form.enter_full_name("Jane Doe")
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

    # Add verification for successful registration here

    # --- Negative Test Scenarios ---
    print("Running Negative Test Scenarios...")

    driver.get("http://demo.automationtesting.in/Register.html")
    # N1: Missing Required Fields (Email)
    print("N1: Missing Required Fields (Email)")
    registration_form.enter_full_name("Test User")
    registration_form.enter_address("789 Oak St")
    registration_form.enter_phone("1122334455")
    registration_form.select_gender("male")
    registration_form.select_country("Australia")
    registration_form.select_date_of_birth("2000", "March", "10")
    registration_form.enter_password("ShortPass")
    registration_form.confirm_password("ShortPass")
    registration_form.click_submit()
    time.sleep(2)

    # Add verification for error message display here (e.g., check for an email error message)
    # Example:
    # error_message = driver.find_element(By.ID, "email-error").text
    # assert "Invalid email address" in error_message

    # F1: Refresh button functionality
    print("F1: Refresh Button Functionality")
    driver.get("http://demo.automationtesting.in/Register.html")
    registration_form.enter_full_name("Before Refresh")
    registration_form.click_refresh()
    full_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Full Name']")
    assert full_name_field.text == "", "Full Name field was not cleared after refresh"


    # Close the driver
    driver.quit()


if __name__ == "__main__":
    main()
