# Test Cases for Automation Demo Site Registration

## I. Positive Scenarios

| Test Case ID | Test Scenario | Steps | Expected Result |
|---|---|---|---|
| P1 | Successful Registration with Valid Data | 1. Open the registration page.<br>2. Enter valid data in all required fields (Full Name, Address, Email, Phone, Gender, Country, Date of Birth, Password, Confirm Password).<br>3. Select Hobbies, Languages, and Skills.<br>4. Click "Submit." | Successful registration message/page is displayed. User is registered successfully. |
| P2 | Registration with Minimum Required Fields Only | 1. Open the registration page.<br>2. Enter valid data only in the required fields (Full Name, Address, Email, Phone, Gender, Country, Date of Birth, Password, Confirm Password). Leave optional fields (Hobbies, Languages, Skills) blank.<br>3. Click "Submit." | Successful registration message/page is displayed. User is registered successfully. |
| P3 | Registration with Maximum Length Data | 1. Open the registration page.<br>2. Enter data with maximum allowed characters in all fields that have length restrictions (e.g., Full Name, Address, Password).<br>3. Select multiple hobbies, skills and languages.<br>4. Click "Submit." | Successful registration message/page is displayed. User is registered successfully. |
| P4 | Registration with Special Characters | 1. Open the registration page.<br>2. Enter valid data in all fields, including special characters in fields like Address, Full Name, and Password.<br>3. Click "Submit." | Successful registration message/page is displayed. User is registered successfully. Special characters are handled correctly. |
| P5 | Registration with Alternate Email Formats | 1. Open the registration page.<br>2. Use different valid email formats (e.g., name@domain.co.in, name.surname@domain.com).<br>3. Click "Submit." | Successful registration message/page is displayed. User is registered successfully. Email format is accepted. |
| P6 | Registration After Refreshing the Page | 1. Open the registration page.<br>2. Fill in all the required fields.<br>3. Refresh the page before submitting.<br>4. Click "Submit." | Successful registration message/page is displayed. User is registered successfully. Data entered should remain after the refresh. |

## II. Negative Scenarios

| Test Case ID | Test Scenario | Steps | Expected Result |
|---|---|---|---|
| N1 | Missing Required Fields | 1. Open the registration page.<br>2. Leave one or more required fields blank (Full Name, Address, Email, Phone, Gender, Country, Date of Birth, Password, Confirm Password).<br>3. Click "Submit." | Appropriate error messages are displayed for each missing field. Registration fails. |
| N2 | Invalid Email Format | 1. Open the registration page.<br>2. Enter an invalid email address (e.g., missing @ symbol, missing domain).<br>3. Click "Submit." | Error message indicating invalid email format is displayed. Registration fails. |
| N3 | Invalid Phone Number | 1. Open the registration page.<br>2. Enter an invalid phone number (e.g., incorrect length, non-numeric characters).<br>3. Click "Submit." | Error message indicating invalid phone number format is displayed. Registration fails. |
| N4 | Password Mismatch | 1. Open the registration page.<br>2. Enter different values in the "Password" and "Confirm Password" fields.<br>3. Click "Submit." | Error message indicating password mismatch is displayed. Registration fails. |
| N5 | Weak Password | 1. Open the registration page.<br>2. Enter a password that does not meet complexity requirements (e.g., too short, only letters, no special characters). (If password complexity is defined)<br>3. Click "Submit." | Error message indicating password strength requirements is displayed. Registration fails. |
| N6 | Invalid Date of Birth | 1. Open the registration page.<br>2. Select an invalid date of birth (e.g., future date, invalid date like February 30th).<br>3. Click "Submit." | Error message or appropriate handling of invalid date is displayed. Registration fails. |
| N7 | Submitting without selecting Gender | 1. Open the registration page.<br>2. Attempt registration without selecting any gender.<br>3. Click "Submit." | Error message appears. Registration fails. |
| N8 | Country Not Selected | 1. Open the registration page.<br>2. Attempt registration without selecting any country. The default "Select Country" option should not be a valid selection.<br>3. Click "Submit." | Error message appears. Registration fails. |
| N9 | Using an Already Registered Email Address | 1. Open the registration page.<br>2. Attempt registration using an email address that already exists in the system.<br>3. Click "Submit." | Error message indicating email address already registered is displayed. Registration fails. |
| N10 | HTML Injection | 1. Open the registration page.<br>2. Attempt to inject HTML code into Full Name or Address field.<br>3. Click "Submit." | The HTML is not rendered and is properly escaped/sanitized. Registration may still succeed if other validations pass. |
| N11 | SQL Injection | 1. Open the registration page.<br>2. Attempt to inject SQL queries in Full Name or Address field.<br>3. Click "Submit." | Proper error handling and that the application remains stable. The SQL query is not executed. Registration fails or succeeds depending on other validation, but the application should remain secure. |

## III. Boundary Scenarios

| Test Case ID | Test Scenario | Steps | Expected Result |
|---|---|---|---|
| B1 | Minimum and Maximum Lengths for Text Fields | 1. Open the registration page.<br>2. Test the boundaries of the Full Name, Address, and Password fields (if limits are specified). For example, if Full Name allows 50 characters, test with 0, 1, 49, 50, and 51 characters.<br>3. Click "Submit." | Fields behave as expected based on requirements. Error messages are shown when exceeding maximum limit, and empty/min lengths are handled according to requirements. |
| B2 | Date Range for Date of Birth | 1. Open the registration page.<br>2. Test with the oldest and newest possible dates of birth.<br>3. Click "Submit." | Registration is allowed within the valid date range and not allowed outside the range. |
| B3 | Number of Selections for Hobbies/Skills/Languages | 1. Open the registration page.<br>2. If there's a limit on how many hobbies, skills or languages can be selected, test with zero, one, the maximum limit, and one more than the maximum.<br>3. Click "Submit." | The application handles the boundary conditions correctly. Error message if the number of selections exceeds limit. |
| B4 | Phone Number Length | 1. Open the registration page.<br>2. Test with phone numbers of minimum and maximum allowed length (if specified).<br>3. Click "Submit." | The application handles the boundary conditions correctly. Registration proceeds if the number is within limit, else it displays an error. |

## IV. Functional Scenarios

| Test Case ID | Test Scenario | Steps | Expected Result |
|---|---|---|---|
| F1 | Refresh Button Functionality | 1. Open the registration page.<br>2. Enter some data into the registration form.<br>3. Click on the "Refresh" button. | All the input fields are cleared. |
| F2 | Photo Upload Functionality | 1. Open the registration page.<br>2. Upload a photo using the 'Photo' upload button.<br>3. Submit the form.<br>4. Test with different image formats (jpg, png, gif).<br>5. Test with large image file sizes. | The photo is uploaded successfully and linked to the user account, if applicable. The application should handle various image formats and file sizes without crashing. |

## V. Usability Scenarios

| Test Case ID | Test Scenario | Steps | Expected Result |
|---|---|---|---|
| U1 | Label association with input fields | 1. Open the registration page.<br>2. Check if labels are correctly associated with input elements using `for` and `id` attributes.<br>3. Clicking on a label. | Clicking on a label should focus the associated input field. |
| U2 | Readability and Visibility of error messages | 1. Open the registration page.<br>2. Trigger error messages by submitting invalid data.<br>3. Observe the error messages. | Error messages are clear, concise, and easily understandable. Error messages should be displayed close to the corresponding input fields. |
| U3 | Accessibility testing | 1. Open the registration page.<br>2. Test the registration form using screen readers.<br>3. Use keyboard navigation. | All form elements are properly labeled and can be accessed using keyboard navigation. Screen reader can read all fields and instructions clearly. |

## VI. Other Considerations

| Test Case ID | Test Scenario | Steps | Expected Result |
|---|---|---|---|
| O1 | Database Verification | 1. Complete a successful registration.<br>2. Check the database. | After successful registration, verify that the data is correctly stored in the database. |
| O2 | Cross-Browser Compatibility | 1. Open the registration page on different browsers (Chrome, Firefox, Safari, Edge).<br>2. Perform various registration scenarios. | Test the registration process on different browsers (Chrome, Firefox, Safari, Edge) to ensure consistent behavior. |
| O3 | Mobile Device Compatibility | 1. Open the registration page on different mobile devices (smartphones, tablets).<br>2. Perform various registration scenarios. | Test the registration process on different mobile devices (smartphones, tablets) to ensure responsiveness and usability. |
| O4 | Performance Testing | 1. Open the registration page.<br>2. Measure the time it takes to complete the registration process under normal and high load conditions. | Measure the time it takes to complete the registration process under normal and high load conditions. The response time should be within acceptable limits. |
