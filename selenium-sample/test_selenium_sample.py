from selenium import webdriver
from urllib.parse import unquote
from selenium.webdriver.common.by import By

def test_selenium_sample(driver):
    # Navigate to the URL
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo?my%20message=Tests%20are%20covering%2097%%20of%20the%20scope.%20Total%20cost%20of%20testing%20activities%20this%20sprint%20was%20$1299.55%20(US%20Dollar)")

    # Maximize browser window
    driver.maximize_window()

    # Get and print the current browser URL
    current_url = driver.current_url
    print("\nCurrent URL:", current_url)

    # Decode the URL
    decoded_url = unquote(current_url)

    # Interact with the web page
    message_field = driver.find_element(By.ID, "user-message")
    message_field.send_keys(decoded_url)
    
    show_button = driver.find_element(By.ID, "showInput")
    show_button.click()

    # Verify the output
    displayed_message = driver.find_element(By.ID, "message").text
    assert decoded_url == displayed_message, "The message displayed does not match the expected message."

    # Print the decoded URL
    print("\nDecoded URL:", decoded_url)
